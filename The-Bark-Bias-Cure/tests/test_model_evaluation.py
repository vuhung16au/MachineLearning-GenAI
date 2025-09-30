"""
Tests for model evaluation functionality.
"""

import pytest
import pandas as pd
import numpy as np
import sys
from pathlib import Path
import joblib
import tempfile
import os

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent / "utils"))
from evaluate_model import ModelEvaluator
from train_model import DogBehaviorClassifier
from generate_data import DogBehaviorGenerator


class TestModelEvaluator:
    """Test cases for ModelEvaluator class."""
    
    @pytest.fixture
    def sample_data(self):
        """Create sample data for testing."""
        generator = DogBehaviorGenerator(seed=42)
        dataset = generator.generate_dataset(n_humans=100, n_dogs=20, n_interactions=500)
        return dataset['interactions']
    
    @pytest.fixture
    def trained_model(self, sample_data, tmp_path):
        """Create a trained model for testing."""
        classifier = DogBehaviorClassifier(random_state=42)
        X = classifier.prepare_features(sample_data)
        y = sample_data['barks']
        
        # Train model
        classifier.train(X, y, test_size=0.2, optimize_hyperparams=False)
        
        # Save model
        model_path = tmp_path / "test_model.joblib"
        model_data = {
            'model': classifier.model,
            'scaler': classifier.scaler,
            'label_encoders': classifier.label_encoders,
            'feature_columns': classifier.feature_columns
        }
        joblib.dump(model_data, model_path)
        
        return str(model_path)
    
    def test_initialization(self, trained_model):
        """Test evaluator initialization."""
        evaluator = ModelEvaluator(trained_model)
        assert evaluator.model_path == trained_model
        assert evaluator.model is None
        assert evaluator.scaler is None
    
    def test_load_model(self, trained_model):
        """Test model loading."""
        evaluator = ModelEvaluator(trained_model)
        evaluator.load_model()
        
        assert evaluator.model is not None
        assert evaluator.scaler is not None
        assert evaluator.label_encoders is not None
        assert evaluator.feature_columns is not None
    
    def test_prepare_features(self, trained_model, sample_data):
        """Test feature preparation."""
        evaluator = ModelEvaluator(trained_model)
        evaluator.load_model()
        
        X = evaluator.prepare_features(sample_data)
        
        assert isinstance(X, pd.DataFrame)
        assert len(X) == len(sample_data)
        assert len(X.columns) == len(evaluator.feature_columns)
        
        # Check that all features are numeric
        for col in X.columns:
            assert pd.api.types.is_numeric_dtype(X[col]), f"Column {col} should be numeric"
    
    def test_predict(self, trained_model, sample_data):
        """Test model prediction."""
        evaluator = ModelEvaluator(trained_model)
        evaluator.load_model()
        
        predictions, probabilities = evaluator.predict(sample_data)
        
        assert len(predictions) == len(sample_data)
        assert len(probabilities) == len(sample_data)
        assert all(pred in [0, 1] for pred in predictions)
        assert all(0 <= prob <= 1 for prob in probabilities)
    
    def test_evaluate_overall_performance(self, trained_model, sample_data):
        """Test overall performance evaluation."""
        evaluator = ModelEvaluator(trained_model)
        evaluator.load_model()
        
        results = evaluator.evaluate_overall_performance(sample_data)
        
        assert 'accuracy' in results
        assert 'precision' in results
        assert 'recall' in results
        assert 'f1_score' in results
        assert 'auc_score' in results
        assert 'confusion_matrix' in results
        
        # Check that metrics are reasonable
        assert 0 <= results['accuracy'] <= 1
        assert 0 <= results['precision'] <= 1
        assert 0 <= results['recall'] <= 1
        assert 0 <= results['f1_score'] <= 1
        assert 0 <= results['auc_score'] <= 1
        
        # Check confusion matrix
        cm = results['confusion_matrix']
        assert cm.shape == (2, 2)
        assert all(cm.flat >= 0)
    
    def test_evaluate_bias_by_race(self, trained_model, sample_data):
        """Test bias evaluation by race."""
        evaluator = ModelEvaluator(trained_model)
        evaluator.load_model()
        
        race_results = evaluator.evaluate_bias_by_race(sample_data)
        
        assert isinstance(race_results, dict)
        assert len(race_results) > 0
        
        for race, metrics in race_results.items():
            assert 'n_samples' in metrics
            assert 'actual_bark_rate' in metrics
            assert 'predicted_bark_rate' in metrics
            assert 'bias_score' in metrics
            assert 'accuracy' in metrics
            
            # Check that rates are between 0 and 1
            assert 0 <= metrics['actual_bark_rate'] <= 1
            assert 0 <= metrics['predicted_bark_rate'] <= 1
            assert 0 <= metrics['accuracy'] <= 1
    
    def test_evaluate_bias_by_gender(self, trained_model, sample_data):
        """Test bias evaluation by gender."""
        evaluator = ModelEvaluator(trained_model)
        evaluator.load_model()
        
        gender_results = evaluator.evaluate_bias_by_gender(sample_data)
        
        assert isinstance(gender_results, dict)
        assert len(gender_results) > 0
        
        for gender, metrics in gender_results.items():
            assert 'n_samples' in metrics
            assert 'actual_bark_rate' in metrics
            assert 'predicted_bark_rate' in metrics
            assert 'bias_score' in metrics
            assert 'accuracy' in metrics
    
    def test_evaluate_bias_by_age(self, trained_model, sample_data):
        """Test bias evaluation by age group."""
        evaluator = ModelEvaluator(trained_model)
        evaluator.load_model()
        
        age_results = evaluator.evaluate_bias_by_age(sample_data)
        
        assert isinstance(age_results, dict)
        assert len(age_results) > 0
        
        for age, metrics in age_results.items():
            assert 'n_samples' in metrics
            assert 'actual_bark_rate' in metrics
            assert 'predicted_bark_rate' in metrics
            assert 'bias_score' in metrics
            assert 'accuracy' in metrics
    
    def test_calculate_fairness_metrics(self, trained_model, sample_data):
        """Test fairness metrics calculation."""
        evaluator = ModelEvaluator(trained_model)
        evaluator.load_model()
        
        fairness_metrics = evaluator.calculate_fairness_metrics(sample_data)
        
        assert 'race_statistical_parity_difference' in fairness_metrics
        assert 'gender_statistical_parity_difference' in fairness_metrics
        assert 'race_rates' in fairness_metrics
        assert 'gender_rates' in fairness_metrics
        
        # Check that statistical parity differences are non-negative
        assert fairness_metrics['race_statistical_parity_difference'] >= 0
        assert fairness_metrics['gender_statistical_parity_difference'] >= 0
    
    def test_generate_evaluation_report(self, trained_model, sample_data, tmp_path):
        """Test evaluation report generation."""
        evaluator = ModelEvaluator(trained_model)
        evaluator.load_model()
        
        report = evaluator.generate_evaluation_report(sample_data, tmp_path)
        
        assert isinstance(report, dict)
        assert 'evaluation_date' in report
        assert 'dataset_info' in report
        assert 'overall_performance' in report
        assert 'bias_analysis' in report
        assert 'fairness_metrics' in report
        assert 'recommendations' in report
        
        # Check that report files are created
        assert (tmp_path / 'evaluation_report.json').exists()
        assert (tmp_path / 'evaluation_summary.md').exists()
    
    def test_create_bias_visualizations(self, trained_model, sample_data, tmp_path):
        """Test bias visualization creation."""
        evaluator = ModelEvaluator(trained_model)
        evaluator.load_model()
        
        evaluator.create_bias_visualizations(sample_data, tmp_path)
        
        # Check that visualization files are created
        expected_files = [
            'bias_by_race.png',
            'bias_by_gender.png',
            'roc_curves_by_race.png',
            'prediction_distribution_by_race.png'
        ]
        
        for filename in expected_files:
            assert (tmp_path / filename).exists()
    
    def test_error_handling(self):
        """Test error handling for invalid inputs."""
        # Test with non-existent model file
        evaluator = ModelEvaluator("non_existent_model.joblib")
        with pytest.raises(Exception):
            evaluator.load_model()
        
        # Test with invalid data
        evaluator = ModelEvaluator("dummy_path")
        with pytest.raises(AttributeError):
            evaluator.predict(pd.DataFrame())


if __name__ == "__main__":
    pytest.main([__file__])
