"""
Evaluate the trained dog behavior classification model.

This script provides comprehensive evaluation of the model including
bias analysis, fairness metrics, and performance across different groups.
"""

import pandas as pd
import numpy as np
import joblib
import json
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report,
    precision_recall_curve, roc_curve
)
from typing import Dict, List, Tuple, Any
import warnings
warnings.filterwarnings('ignore')


class ModelEvaluator:
    """Comprehensive model evaluation with bias analysis."""
    
    def __init__(self, model_path: str):
        """Initialize evaluator with trained model."""
        self.model_path = model_path
        self.model_data = None
        self.model = None
        self.scaler = None
        self.label_encoders = None
        self.feature_columns = None
        
    def load_model(self):
        """Load the trained model and preprocessors."""
        try:
            self.model_data = joblib.load(self.model_path)
            self.model = self.model_data['model']
            self.scaler = self.model_data['scaler']
            self.label_encoders = self.model_data['label_encoders']
            self.feature_columns = self.model_data['feature_columns']
            print(f"✅ Model loaded from {self.model_path}")
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            raise
    
    def prepare_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Prepare features using the same preprocessing as training."""
        df = df.copy()
        
        # Encode categorical variables
        for col in self.feature_columns:
            if col in self.label_encoders:
                df[col] = self.label_encoders[col].transform(df[col].astype(str))
        
        # Handle missing values
        df[self.feature_columns] = df[self.feature_columns].fillna(df[self.feature_columns].median())
        
        return df[self.feature_columns]
    
    def predict(self, df: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        """Make predictions on the dataset."""
        X = self.prepare_features(df)
        X_scaled = self.scaler.transform(X)
        
        predictions = self.model.predict(X_scaled)
        probabilities = self.model.predict_proba(X_scaled)[:, 1]
        
        return predictions, probabilities
    
    def evaluate_overall_performance(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Evaluate overall model performance."""
        print("📊 Evaluating Overall Performance...")
        print("=" * 50)
        
        y_true = df['barks'].values
        y_pred, y_proba = self.predict(df)
        
        # Calculate metrics
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        auc = roc_auc_score(y_true, y_proba)
        
        # Confusion matrix
        cm = confusion_matrix(y_true, y_pred)
        
        print(f"Accuracy:  {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall:    {recall:.4f}")
        print(f"F1 Score:  {f1:.4f}")
        print(f"AUC Score: {auc:.4f}")
        
        print(f"\nConfusion Matrix:")
        print(f"                Predicted")
        print(f"                No Bark  Bark")
        print(f"Actual No Bark    {cm[0,0]:4d}    {cm[0,1]:4d}")
        print(f"       Bark        {cm[1,0]:4d}    {cm[1,1]:4d}")
        
        return {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'auc_score': auc,
            'confusion_matrix': cm.tolist()
        }
    
    def evaluate_bias_by_race(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Evaluate model performance and bias by race."""
        print("\n🔍 Bias Analysis by Race...")
        print("=" * 50)
        
        race_results = {}
        
        for race in df['human_race'].unique():
            race_df = df[df['human_race'] == race]
            if len(race_df) < 10:  # Skip if too few samples
                continue
                
            y_true = race_df['barks'].values
            y_pred, y_proba = self.predict(race_df)
            
            # Calculate metrics
            accuracy = accuracy_score(y_true, y_pred)
            precision = precision_score(y_true, y_pred, zero_division=0)
            recall = recall_score(y_true, y_pred, zero_division=0)
            f1 = f1_score(y_true, y_pred, zero_division=0)
            auc = roc_auc_score(y_true, y_proba) if len(np.unique(y_true)) > 1 else 0
            
            # Actual vs predicted rates
            actual_rate = y_true.mean()
            predicted_rate = y_pred.mean()
            
            race_results[race] = {
                'n_samples': len(race_df),
                'actual_bark_rate': actual_rate,
                'predicted_bark_rate': predicted_rate,
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1_score': f1,
                'auc_score': auc,
                'bias_score': predicted_rate - actual_rate  # Positive = over-prediction
            }
            
            print(f"{race:<15}: {len(race_df):4d} samples, "
                  f"Actual: {actual_rate:.2%}, Predicted: {predicted_rate:.2%}, "
                  f"Bias: {predicted_rate - actual_rate:+.2%}")
        
        return race_results
    
    def evaluate_bias_by_gender(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Evaluate model performance and bias by gender."""
        print("\n🔍 Bias Analysis by Gender...")
        print("=" * 50)
        
        gender_results = {}
        
        for gender in df['human_gender'].unique():
            gender_df = df[df['human_gender'] == gender]
            if len(gender_df) < 10:
                continue
                
            y_true = gender_df['barks'].values
            y_pred, y_proba = self.predict(gender_df)
            
            # Calculate metrics
            accuracy = accuracy_score(y_true, y_pred)
            precision = precision_score(y_true, y_pred, zero_division=0)
            recall = recall_score(y_true, y_pred, zero_division=0)
            f1 = f1_score(y_true, y_pred, zero_division=0)
            auc = roc_auc_score(y_true, y_proba) if len(np.unique(y_true)) > 1 else 0
            
            # Actual vs predicted rates
            actual_rate = y_true.mean()
            predicted_rate = y_pred.mean()
            
            gender_results[gender] = {
                'n_samples': len(gender_df),
                'actual_bark_rate': actual_rate,
                'predicted_bark_rate': predicted_rate,
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1_score': f1,
                'auc_score': auc,
                'bias_score': predicted_rate - actual_rate
            }
            
            print(f"{gender:<15}: {len(gender_df):4d} samples, "
                  f"Actual: {actual_rate:.2%}, Predicted: {predicted_rate:.2%}, "
                  f"Bias: {predicted_rate - actual_rate:+.2%}")
        
        return gender_results
    
    def evaluate_bias_by_age(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Evaluate model performance and bias by age group."""
        print("\n🔍 Bias Analysis by Age Group...")
        print("=" * 50)
        
        age_results = {}
        
        for age in df['human_age_group'].unique():
            age_df = df[df['human_age_group'] == age]
            if len(age_df) < 10:
                continue
                
            y_true = age_df['barks'].values
            y_pred, y_proba = self.predict(age_df)
            
            # Calculate metrics
            accuracy = accuracy_score(y_true, y_pred)
            precision = precision_score(y_true, y_pred, zero_division=0)
            recall = recall_score(y_true, y_pred, zero_division=0)
            f1 = f1_score(y_true, y_pred, zero_division=0)
            auc = roc_auc_score(y_true, y_proba) if len(np.unique(y_true)) > 1 else 0
            
            # Actual vs predicted rates
            actual_rate = y_true.mean()
            predicted_rate = y_pred.mean()
            
            age_results[age] = {
                'n_samples': len(age_df),
                'actual_bark_rate': actual_rate,
                'predicted_bark_rate': predicted_rate,
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1_score': f1,
                'auc_score': auc,
                'bias_score': predicted_rate - actual_rate
            }
            
            print(f"{age:<15}: {len(age_df):4d} samples, "
                  f"Actual: {actual_rate:.2%}, Predicted: {predicted_rate:.2%}, "
                  f"Bias: {predicted_rate - actual_rate:+.2%}")
        
        return age_results
    
    def calculate_fairness_metrics(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Calculate fairness metrics across different groups."""
        print("\n⚖️  Fairness Metrics...")
        print("=" * 50)
        
        # Get predictions for all groups
        y_pred, y_proba = self.predict(df)
        
        # Calculate demographic parity
        race_rates = {}
        for race in df['human_race'].unique():
            race_mask = df['human_race'] == race
            if race_mask.sum() > 0:
                race_rates[race] = y_pred[race_mask].mean()
        
        gender_rates = {}
        for gender in df['human_gender'].unique():
            gender_mask = df['human_gender'] == gender
            if gender_mask.sum() > 0:
                gender_rates[gender] = y_pred[gender_mask].mean()
        
        # Calculate statistical parity difference
        race_rates_list = list(race_rates.values())
        gender_rates_list = list(gender_rates.values())
        
        race_spd = max(race_rates_list) - min(race_rates_list) if race_rates_list else 0
        gender_spd = max(gender_rates_list) - min(gender_rates_list) if gender_rates_list else 0
        
        print(f"Race Statistical Parity Difference: {race_spd:.4f}")
        print(f"Gender Statistical Parity Difference: {gender_spd:.4f}")
        
        # Calculate equalized odds (simplified)
        race_equalized_odds = {}
        for race in df['human_race'].unique():
            race_mask = df['human_race'] == race
            if race_mask.sum() > 0:
                race_df = df[race_mask]
                race_y_true = race_df['barks'].values
                race_y_pred = y_pred[race_mask]
                
                # True positive rate
                tpr = recall_score(race_y_true, race_y_pred, zero_division=0)
                # False positive rate
                fpr = 1 - recall_score(1 - race_y_true, 1 - race_y_pred, zero_division=0)
                
                race_equalized_odds[race] = {'tpr': tpr, 'fpr': fpr}
        
        return {
            'race_statistical_parity_difference': race_spd,
            'gender_statistical_parity_difference': gender_spd,
            'race_rates': race_rates,
            'gender_rates': gender_rates,
            'race_equalized_odds': race_equalized_odds
        }
    
    def create_bias_visualizations(self, df: pd.DataFrame, output_dir: Path):
        """Create visualizations for bias analysis."""
        print("\n📊 Creating bias visualizations...")
        
        # Set style
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        # Get predictions
        y_pred, y_proba = self.predict(df)
        
        # 1. Bias by race
        plt.figure(figsize=(12, 8))
        race_bias = df.groupby('human_race').apply(
            lambda x: y_pred[df['human_race'] == x.name].mean() - x['barks'].mean()
        ).sort_values(ascending=False)
        
        sns.barplot(x=race_bias.index, y=race_bias.values)
        plt.title('Model Bias by Race (Predicted Rate - Actual Rate)')
        plt.xlabel('Race')
        plt.ylabel('Bias Score')
        plt.xticks(rotation=45)
        plt.axhline(y=0, color='red', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig(output_dir / 'bias_by_race.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # 2. Bias by gender
        plt.figure(figsize=(10, 6))
        gender_bias = df.groupby('human_gender').apply(
            lambda x: y_pred[df['human_gender'] == x.name].mean() - x['barks'].mean()
        ).sort_values(ascending=False)
        
        sns.barplot(x=gender_bias.index, y=gender_bias.values)
        plt.title('Model Bias by Gender (Predicted Rate - Actual Rate)')
        plt.xlabel('Gender')
        plt.ylabel('Bias Score')
        plt.axhline(y=0, color='red', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig(output_dir / 'bias_by_gender.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # 3. ROC curves by race
        plt.figure(figsize=(12, 8))
        for race in df['human_race'].unique():
            race_mask = df['human_race'] == race
            if race_mask.sum() > 10:  # Only plot if enough samples
                race_y_true = df[race_mask]['barks'].values
                race_y_proba = y_proba[race_mask]
                
                fpr, tpr, _ = roc_curve(race_y_true, race_y_proba)
                auc = roc_auc_score(race_y_true, race_y_proba)
                
                plt.plot(fpr, tpr, label=f'{race} (AUC={auc:.3f})', linewidth=2)
        
        plt.plot([0, 1], [0, 1], 'k--', alpha=0.5)
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC Curves by Race')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(output_dir / 'roc_curves_by_race.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # 4. Prediction distribution by race
        plt.figure(figsize=(14, 8))
        race_data = []
        for race in df['human_race'].unique():
            race_mask = df['human_race'] == race
            race_proba = y_proba[race_mask]
            race_data.extend([(race, prob) for prob in race_proba])
        
        race_df_plot = pd.DataFrame(race_data, columns=['Race', 'Prediction_Probability'])
        sns.boxplot(data=race_df_plot, x='Race', y='Prediction_Probability')
        plt.title('Distribution of Prediction Probabilities by Race')
        plt.xlabel('Race')
        plt.ylabel('Prediction Probability')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(output_dir / 'prediction_distribution_by_race.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Bias visualizations saved to {output_dir}/")
    
    def generate_evaluation_report(self, df: pd.DataFrame, output_dir: Path):
        """Generate comprehensive evaluation report."""
        print("\n📋 Generating Evaluation Report...")
        
        # Overall performance
        overall_perf = self.evaluate_overall_performance(df)
        
        # Bias analysis
        race_bias = self.evaluate_bias_by_race(df)
        gender_bias = self.evaluate_bias_by_gender(df)
        age_bias = self.evaluate_bias_by_age(df)
        
        # Fairness metrics
        fairness_metrics = self.calculate_fairness_metrics(df)
        
        # Create visualizations
        self.create_bias_visualizations(df, output_dir)
        
        # Compile report
        report = {
            'evaluation_date': pd.Timestamp.now().isoformat(),
            'dataset_info': {
                'total_samples': len(df),
                'positive_samples': df['barks'].sum(),
                'positive_rate': df['barks'].mean()
            },
            'overall_performance': overall_perf,
            'bias_analysis': {
                'by_race': race_bias,
                'by_gender': gender_bias,
                'by_age': age_bias
            },
            'fairness_metrics': fairness_metrics,
            'recommendations': self._generate_recommendations(race_bias, gender_bias, fairness_metrics)
        }
        
        # Save report
        with open(output_dir / 'evaluation_report.json', 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        # Save summary
        self._save_summary_report(report, output_dir)
        
        print(f"✅ Evaluation report saved to {output_dir}/evaluation_report.json")
        return report
    
    def _generate_recommendations(self, race_bias: Dict, gender_bias: Dict, 
                                fairness_metrics: Dict) -> List[str]:
        """Generate recommendations based on bias analysis."""
        recommendations = []
        
        # Race bias recommendations
        race_spd = fairness_metrics['race_statistical_parity_difference']
        if race_spd > 0.1:
            recommendations.append(
                f"High racial bias detected (SPD={race_spd:.3f}). "
                "Consider retraining with balanced data or using fairness constraints."
            )
        
        # Gender bias recommendations
        gender_spd = fairness_metrics['gender_statistical_parity_difference']
        if gender_spd > 0.1:
            recommendations.append(
                f"High gender bias detected (SPD={gender_spd:.3f}). "
                "Review feature engineering and consider gender-aware preprocessing."
            )
        
        # Specific group recommendations
        for race, metrics in race_bias.items():
            if abs(metrics['bias_score']) > 0.1:
                recommendations.append(
                    f"Significant bias detected for {race} group "
                    f"(bias={metrics['bias_score']:+.3f}). "
                    "Investigate feature importance and data representation."
                )
        
        if not recommendations:
            recommendations.append("No significant bias detected. Model appears fair across groups.")
        
        return recommendations
    
    def _save_summary_report(self, report: Dict, output_dir: Path):
        """Save a human-readable summary report."""
        summary = f"""
# Dog Behavior Model Evaluation Report

## Dataset Overview
- Total samples: {report['dataset_info']['total_samples']:,}
- Positive samples: {report['dataset_info']['positive_samples']:,}
- Positive rate: {report['dataset_info']['positive_rate']:.2%}

## Overall Performance
- Accuracy: {report['overall_performance']['accuracy']:.4f}
- Precision: {report['overall_performance']['precision']:.4f}
- Recall: {report['overall_performance']['recall']:.4f}
- F1 Score: {report['overall_performance']['f1_score']:.4f}
- AUC Score: {report['overall_performance']['auc_score']:.4f}

## Bias Analysis Summary
### By Race
"""
        
        for race, metrics in report['bias_analysis']['by_race'].items():
            summary += f"- {race}: {metrics['bias_score']:+.3f} bias score\n"
        
        summary += "\n### By Gender\n"
        for gender, metrics in report['bias_analysis']['by_gender'].items():
            summary += f"- {gender}: {metrics['bias_score']:+.3f} bias score\n"
        
        summary += f"""
## Fairness Metrics
- Race Statistical Parity Difference: {report['fairness_metrics']['race_statistical_parity_difference']:.4f}
- Gender Statistical Parity Difference: {report['fairness_metrics']['gender_statistical_parity_difference']:.4f}

## Recommendations
"""
        for i, rec in enumerate(report['recommendations'], 1):
            summary += f"{i}. {rec}\n"
        
        with open(output_dir / 'evaluation_summary.md', 'w') as f:
            f.write(summary)


def main():
    """Main evaluation function."""
    # Check if model exists
    model_path = Path("models/dog_behavior_classifier.joblib")
    if not model_path.exists():
        print("❌ Model not found! Please run train_model.py first.")
        return
    
    # Check if dataset exists
    data_path = Path("data/dog_behavior_dataset.csv")
    if not data_path.exists():
        print("❌ Dataset not found! Please run generate_data.py first.")
        return
    
    # Load data
    print("📊 Loading dataset...")
    df = pd.read_csv(data_path)
    print(f"Dataset shape: {df.shape}")
    
    # Initialize evaluator
    evaluator = ModelEvaluator(str(model_path))
    evaluator.load_model()
    
    # Create output directory
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    
    # Generate evaluation report
    report = evaluator.generate_evaluation_report(df, reports_dir)
    
    print(f"\n✅ Evaluation completed!")
    print(f"Report saved to: reports/evaluation_report.json")
    print(f"Summary saved to: reports/evaluation_summary.md")
    print(f"Visualizations saved to: reports/")


if __name__ == "__main__":
    main()
