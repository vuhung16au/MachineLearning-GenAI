"""
Train XGBoost model for dog behavior classification.

This script trains a model to predict whether a dog will bark at a person
based on various human and dog attributes.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import xgboost as xgb
import joblib
import json
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Any, Tuple
import warnings
warnings.filterwarnings('ignore')


class DogBehaviorClassifier:
    """XGBoost classifier for dog behavior prediction."""
    
    def __init__(self, random_state: int = 42):
        """Initialize the classifier."""
        self.random_state = random_state
        self.model = None
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.feature_columns = []
        self.target_column = 'barks'
        
    def prepare_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Prepare features for training."""
        df = df.copy()
        
        # Select relevant features
        feature_columns = [
            # Human attributes
            'human_race', 'human_gender', 'human_skin_color', 'human_age_group',
            'human_clothing_style', 'human_height', 'human_voice_pitch',
            'human_age_years', 'human_has_glasses', 'human_has_hat', 'human_is_smiling',
            'human_movement_speed', 'human_body_language',
            
            # Dog attributes  
            'dog_breed', 'dog_age_months', 'dog_training_level', 'dog_temperament',
            'dog_size', 'dog_energy_level', 'dog_socialization_score',
            'dog_previous_negative_experiences', 'dog_owner_race', 'dog_living_environment',
            'dog_daily_exercise_hours',
            
            # Interaction context
            'distance_meters', 'human_approach_speed', 'dog_was_sleeping',
            'other_dogs_present', 'weather', 'time_of_day'
        ]
        
        # Filter to available columns
        available_features = [col for col in feature_columns if col in df.columns]
        self.feature_columns = available_features
        
        # Encode categorical variables
        categorical_columns = [col for col in available_features 
                             if df[col].dtype == 'object' or col in ['human_has_glasses', 'human_has_hat', 'human_is_smiling', 'dog_was_sleeping', 'other_dogs_present']]
        
        for col in categorical_columns:
            if col not in self.label_encoders:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))
                self.label_encoders[col] = le
            else:
                df[col] = self.label_encoders[col].transform(df[col].astype(str))
        
        # Handle missing values
        df[available_features] = df[available_features].fillna(df[available_features].median())
        
        return df[available_features]
    
    def train(self, X: pd.DataFrame, y: pd.Series, 
              test_size: float = 0.2, optimize_hyperparams: bool = True) -> Dict[str, Any]:
        """Train the XGBoost model."""
        print("🐕 Training Dog Behavior Classifier...")
        print("=" * 50)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.random_state, stratify=y
        )
        
        print(f"Training set size: {len(X_train)}")
        print(f"Test set size: {len(X_test)}")
        print(f"Positive class ratio: {y.mean():.2%}")
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        if optimize_hyperparams:
            print("\n🔧 Optimizing hyperparameters...")
            # Define parameter grid
            param_grid = {
                'n_estimators': [100, 200, 300],
                'max_depth': [3, 4, 5, 6],
                'learning_rate': [0.01, 0.1, 0.2],
                'subsample': [0.8, 0.9, 1.0],
                'colsample_bytree': [0.8, 0.9, 1.0]
            }
            
            # Grid search with cross-validation
            xgb_model = xgb.XGBClassifier(
                random_state=self.random_state,
                eval_metric='logloss'
            )
            
            grid_search = GridSearchCV(
                xgb_model, param_grid, cv=3, scoring='roc_auc', 
                n_jobs=-1, verbose=1
            )
            
            grid_search.fit(X_train_scaled, y_train)
            
            print(f"Best parameters: {grid_search.best_params_}")
            print(f"Best CV score: {grid_search.best_score_:.4f}")
            
            self.model = grid_search.best_estimator_
        else:
            # Use default parameters
            self.model = xgb.XGBClassifier(
                n_estimators=200,
                max_depth=4,
                learning_rate=0.1,
                random_state=self.random_state,
                eval_metric='logloss'
            )
            self.model.fit(X_train_scaled, y_train)
        
        # Make predictions
        y_pred = self.model.predict(X_test_scaled)
        y_pred_proba = self.model.predict_proba(X_test_scaled)[:, 1]
        
        # Calculate metrics
        auc_score = roc_auc_score(y_test, y_pred_proba)
        
        print(f"\n📊 Model Performance:")
        print(f"AUC Score: {auc_score:.4f}")
        print(f"Accuracy: {(y_pred == y_test).mean():.4f}")
        
        # Classification report
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred, target_names=['No Bark', 'Bark']))
        
        # Feature importance
        feature_importance = pd.DataFrame({
            'feature': self.feature_columns,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print(f"\n🔍 Top 10 Most Important Features:")
        for i, (_, row) in enumerate(feature_importance.head(10).iterrows()):
            print(f"{i+1:2d}. {row['feature']:<30} {row['importance']:.4f}")
        
        # Store results
        results = {
            'model': self.model,
            'scaler': self.scaler,
            'label_encoders': self.label_encoders,
            'feature_columns': self.feature_columns,
            'auc_score': auc_score,
            'accuracy': (y_pred == y_test).mean(),
            'feature_importance': feature_importance,
            'confusion_matrix': confusion_matrix(y_test, y_pred),
            'classification_report': classification_report(y_test, y_pred, output_dict=True)
        }
        
        return results
    
    def predict(self, X: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        """Make predictions on new data."""
        if self.model is None:
            raise ValueError("Model not trained yet!")
        
        X_processed = self.prepare_features(X)
        X_scaled = self.scaler.transform(X_processed)
        
        predictions = self.model.predict(X_scaled)
        probabilities = self.model.predict_proba(X_scaled)[:, 1]
        
        return predictions, probabilities
    
    def save_model(self, filepath: str):
        """Save the trained model and preprocessors."""
        model_data = {
            'model': self.model,
            'scaler': self.scaler,
            'label_encoders': self.label_encoders,
            'feature_columns': self.feature_columns
        }
        joblib.dump(model_data, filepath)
        print(f"✅ Model saved to {filepath}")
    
    def load_model(self, filepath: str):
        """Load a trained model and preprocessors."""
        model_data = joblib.load(filepath)
        self.model = model_data['model']
        self.scaler = model_data['scaler']
        self.label_encoders = model_data['label_encoders']
        self.feature_columns = model_data['feature_columns']
        print(f"✅ Model loaded from {filepath}")


def analyze_bias_patterns(df: pd.DataFrame, model_results: Dict[str, Any]):
    """Analyze bias patterns in the model predictions."""
    print("\n🔍 Bias Analysis:")
    print("=" * 50)
    
    # Analyze by race
    print("\nBarking predictions by race:")
    race_analysis = df.groupby('human_race')['barks'].agg(['count', 'sum', 'mean'])
    race_analysis['prediction_rate'] = df.groupby('human_race').apply(
        lambda x: model_results['model'].predict_proba(
            model_results['scaler'].transform(
                model_results['model'].get_booster().get_dump()
            )
        )[:, 1].mean() if len(x) > 0 else 0
    )
    
    for race in race_analysis.index:
        actual_rate = race_analysis.loc[race, 'mean']
        count = race_analysis.loc[race, 'count']
        print(f"  {race:<15}: {actual_rate:.2%} actual ({race_analysis.loc[race, 'sum']}/{count})")
    
    # Analyze by gender
    print("\nBarking predictions by gender:")
    gender_analysis = df.groupby('human_gender')['barks'].agg(['count', 'sum', 'mean'])
    for gender in gender_analysis.index:
        actual_rate = gender_analysis.loc[gender, 'mean']
        count = gender_analysis.loc[gender, 'count']
        print(f"  {gender:<15}: {actual_rate:.2%} actual ({gender_analysis.loc[gender, 'sum']}/{count})")
    
    # Analyze by age group
    print("\nBarking predictions by age group:")
    age_analysis = df.groupby('human_age_group')['barks'].agg(['count', 'sum', 'mean'])
    for age in age_analysis.index:
        actual_rate = age_analysis.loc[age, 'mean']
        count = age_analysis.loc[age, 'count']
        print(f"  {age:<15}: {actual_rate:.2%} actual ({age_analysis.loc[age, 'sum']}/{count})")


def create_visualizations(df: pd.DataFrame, model_results: Dict[str, Any], output_dir: Path):
    """Create visualization plots."""
    print("\n📊 Creating visualizations...")
    
    # Set style
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    
    # 1. Feature importance plot
    plt.figure(figsize=(12, 8))
    top_features = model_results['feature_importance'].head(15)
    sns.barplot(data=top_features, x='importance', y='feature')
    plt.title('Top 15 Most Important Features for Dog Barking Prediction')
    plt.xlabel('Feature Importance')
    plt.tight_layout()
    plt.savefig(output_dir / 'feature_importance.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Bias analysis by race
    plt.figure(figsize=(12, 6))
    race_bias = df.groupby('human_race')['barks'].mean().sort_values(ascending=False)
    sns.barplot(x=race_bias.index, y=race_bias.values)
    plt.title('Barking Rate by Human Race')
    plt.xlabel('Race')
    plt.ylabel('Barking Rate')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_dir / 'bias_by_race.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Bias analysis by gender
    plt.figure(figsize=(8, 6))
    gender_bias = df.groupby('human_gender')['barks'].mean().sort_values(ascending=False)
    sns.barplot(x=gender_bias.index, y=gender_bias.values)
    plt.title('Barking Rate by Human Gender')
    plt.xlabel('Gender')
    plt.ylabel('Barking Rate')
    plt.tight_layout()
    plt.savefig(output_dir / 'bias_by_gender.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Confusion matrix
    plt.figure(figsize=(8, 6))
    cm = model_results['confusion_matrix']
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=['No Bark', 'Bark'], 
                yticklabels=['No Bark', 'Bark'])
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.tight_layout()
    plt.savefig(output_dir / 'confusion_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✅ Visualizations saved to {output_dir}/")


def main():
    """Main training function."""
    # Load data
    data_path = Path("data/dog_behavior_dataset.csv")
    if not data_path.exists():
        print("❌ Dataset not found! Please run generate_data.py first.")
        return
    
    print("📊 Loading dataset...")
    df = pd.read_csv(data_path)
    print(f"Dataset shape: {df.shape}")
    
    # Initialize classifier
    classifier = DogBehaviorClassifier(random_state=42)
    
    # Prepare features
    print("\n🔧 Preparing features...")
    X = classifier.prepare_features(df)
    y = df['barks']
    
    print(f"Features shape: {X.shape}")
    print(f"Target distribution: {y.value_counts().to_dict()}")
    
    # Train model
    print("\n🚀 Training model...")
    results = classifier.train(X, y, test_size=0.2, optimize_hyperparams=True)
    
    # Analyze bias patterns
    analyze_bias_patterns(df, results)
    
    # Create visualizations
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    create_visualizations(df, results, reports_dir)
    
    # Save model
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)
    classifier.save_model(models_dir / "dog_behavior_classifier.joblib")
    
    # Save training results
    training_results = {
        'auc_score': results['auc_score'],
        'accuracy': results['accuracy'],
        'feature_importance': results['feature_importance'].to_dict('records'),
        'confusion_matrix': results['confusion_matrix'].tolist(),
        'classification_report': results['classification_report']
    }
    
    with open(reports_dir / "training_results.json", 'w') as f:
        json.dump(training_results, f, indent=2)
    
    print(f"\n✅ Training completed!")
    print(f"Model saved to: models/dog_behavior_classifier.joblib")
    print(f"Results saved to: reports/training_results.json")
    print(f"Visualizations saved to: reports/")


if __name__ == "__main__":
    main()
