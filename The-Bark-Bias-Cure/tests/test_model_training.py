"""
Tests for model training functionality.
"""

import pytest
import pandas as pd
import numpy as np
import sys
from pathlib import Path

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent / "utils"))
from train_model import DogBehaviorClassifier
from generate_data import DogBehaviorGenerator


class TestDogBehaviorClassifier:
    """Test cases for DogBehaviorClassifier class."""
    
    @pytest.fixture
    def sample_data(self):
        """Create sample data for testing."""
        generator = DogBehaviorGenerator(seed=42)
        dataset = generator.generate_dataset(n_humans=100, n_dogs=20, n_interactions=500)
        return dataset['interactions']
    
    def test_initialization(self):
        """Test classifier initialization."""
        classifier = DogBehaviorClassifier(random_state=42)
        assert classifier.random_state == 42
        assert classifier.model is None
        assert classifier.label_encoders == {}
        assert classifier.feature_columns == []
    
    def test_prepare_features(self, sample_data):
        """Test feature preparation."""
        classifier = DogBehaviorClassifier(random_state=42)
        X = classifier.prepare_features(sample_data)
        
        assert isinstance(X, pd.DataFrame)
        assert len(X) == len(sample_data)
        assert len(classifier.feature_columns) > 0
        
        # Check that all features are numeric
        for col in X.columns:
            assert pd.api.types.is_numeric_dtype(X[col]), f"Column {col} should be numeric"
    
    def test_train_basic(self, sample_data):
        """Test basic model training."""
        classifier = DogBehaviorClassifier(random_state=42)
        X = classifier.prepare_features(sample_data)
        y = sample_data['barks']
        
        results = classifier.train(X, y, test_size=0.2, optimize_hyperparams=False)
        
        assert classifier.model is not None
        assert classifier.scaler is not None
        assert len(classifier.label_encoders) > 0
        assert 'auc_score' in results
        assert 'accuracy' in results
        assert 'feature_importance' in results
        
        # Check that metrics are reasonable
        assert 0 <= results['auc_score'] <= 1
        assert 0 <= results['accuracy'] <= 1
    
    def test_predict(self, sample_data):
        """Test model prediction."""
        classifier = DogBehaviorClassifier(random_state=42)
        X = classifier.prepare_features(sample_data)
        y = sample_data['barks']
        
        # Train model
        classifier.train(X, y, test_size=0.2, optimize_hyperparams=False)
        
        # Make predictions
        predictions, probabilities = classifier.predict(sample_data)
        
        assert len(predictions) == len(sample_data)
        assert len(probabilities) == len(sample_data)
        assert all(pred in [0, 1] for pred in predictions)
        assert all(0 <= prob <= 1 for prob in probabilities)
    
    def test_save_load_model(self, sample_data, tmp_path):
        """Test model saving and loading."""
        classifier = DogBehaviorClassifier(random_state=42)
        X = classifier.prepare_features(sample_data)
        y = sample_data['barks']
        
        # Train model
        classifier.train(X, y, test_size=0.2, optimize_hyperparams=False)
        
        # Save model
        model_path = tmp_path / "test_model.joblib"
        classifier.save_model(str(model_path))
        assert model_path.exists()
        
        # Load model
        new_classifier = DogBehaviorClassifier(random_state=42)
        new_classifier.load_model(str(model_path))
        
        assert new_classifier.model is not None
        assert new_classifier.scaler is not None
        assert len(new_classifier.label_encoders) > 0
        assert new_classifier.feature_columns == classifier.feature_columns
    
    def test_feature_importance(self, sample_data):
        """Test feature importance calculation."""
        classifier = DogBehaviorClassifier(random_state=42)
        X = classifier.prepare_features(sample_data)
        y = sample_data['barks']
        
        results = classifier.train(X, y, test_size=0.2, optimize_hyperparams=False)
        
        feature_importance = results['feature_importance']
        assert isinstance(feature_importance, pd.DataFrame)
        assert 'feature' in feature_importance.columns
        assert 'importance' in feature_importance.columns
        assert len(feature_importance) > 0
        
        # Check that importance values are non-negative
        assert all(feature_importance['importance'] >= 0)
        
        # Check that importance sums to 1 (approximately)
        assert abs(feature_importance['importance'].sum() - 1.0) < 0.01
    
    def test_bias_analysis(self, sample_data):
        """Test bias analysis functionality."""
        classifier = DogBehaviorClassifier(random_state=42)
        X = classifier.prepare_features(sample_data)
        y = sample_data['barks']
        
        results = classifier.train(X, y, test_size=0.2, optimize_hyperparams=False)
        
        # Check that bias analysis is included in results
        assert 'confusion_matrix' in results
        assert 'classification_report' in results
        
        # Check confusion matrix
        cm = results['confusion_matrix']
        assert cm.shape == (2, 2)
        assert all(cm.flat >= 0)  # All values should be non-negative
    
    def test_hyperparameter_optimization(self, sample_data):
        """Test hyperparameter optimization."""
        classifier = DogBehaviorClassifier(random_state=42)
        X = classifier.prepare_features(sample_data)
        y = sample_data['barks']
        
        # Test with hyperparameter optimization (smaller grid for speed)
        results = classifier.train(X, y, test_size=0.2, optimize_hyperparams=True)
        
        assert classifier.model is not None
        assert 'auc_score' in results
        assert 0 <= results['auc_score'] <= 1
    
    def test_data_validation(self):
        """Test data validation."""
        classifier = DogBehaviorClassifier(random_state=42)
        
        # Test with empty dataframe
        empty_df = pd.DataFrame()
        with pytest.raises((ValueError, KeyError)):
            classifier.prepare_features(empty_df)
        
        # Test with missing target column
        df_no_target = pd.DataFrame({'feature1': [1, 2, 3]})
        with pytest.raises(KeyError):
            classifier.train(df_no_target, pd.Series([1, 0, 1]))


if __name__ == "__main__":
    pytest.main([__file__])
