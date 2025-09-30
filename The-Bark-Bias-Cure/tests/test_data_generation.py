"""
Tests for data generation functionality.
"""

import pytest
import pandas as pd
import numpy as np
import sys
from pathlib import Path

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent / "utils"))
from generate_data import DogBehaviorGenerator


class TestDogBehaviorGenerator:
    """Test cases for DogBehaviorGenerator class."""
    
    def test_initialization(self):
        """Test generator initialization."""
        generator = DogBehaviorGenerator(seed=42)
        assert generator is not None
        assert len(generator.races) > 0
        assert len(generator.genders) > 0
        assert len(generator.dog_breeds) > 0
    
    def test_generate_human_attributes(self):
        """Test human attributes generation."""
        generator = DogBehaviorGenerator(seed=42)
        humans_df = generator.generate_human_attributes(100)
        
        assert len(humans_df) == 100
        assert 'person_id' in humans_df.columns
        assert 'race' in humans_df.columns
        assert 'gender' in humans_df.columns
        assert 'age_years' in humans_df.columns
        
        # Check that all races are represented
        assert set(humans_df['race'].unique()).issubset(set(generator.races))
        assert set(humans_df['gender'].unique()).issubset(set(generator.genders))
    
    def test_generate_dog_attributes(self):
        """Test dog attributes generation."""
        generator = DogBehaviorGenerator(seed=42)
        dogs_df = generator.generate_dog_attributes(50)
        
        assert len(dogs_df) == 50
        assert 'dog_id' in dogs_df.columns
        assert 'breed' in dogs_df.columns
        assert 'age_months' in dogs_df.columns
        assert 'temperament' in dogs_df.columns
        
        # Check that all breeds are represented
        assert set(dogs_df['breed'].unique()).issubset(set(generator.dog_breeds))
    
    def test_calculate_bias_score(self):
        """Test bias score calculation."""
        generator = DogBehaviorGenerator(seed=42)
        
        # Create sample human and dog
        human = {
            'race': 'Black',
            'gender': 'Male',
            'skin_color': 'Dark',
            'age_group': 'Young Adult',
            'clothing_style': 'Casual',
            'height': 'Average',
            'voice_pitch': 'Medium',
            'age_years': 25,
            'has_glasses': False,
            'has_hat': False,
            'is_smiling': True,
            'movement_speed': 'Normal',
            'body_language': 'Relaxed'
        }
        
        dog = {
            'breed': 'Labrador',
            'age_months': 24,
            'training_level': 'Basic',
            'temperament': 'Friendly',
            'size': 'Large',
            'energy_level': 'Medium',
            'socialization_score': 7.5,
            'previous_negative_experiences': 1,
            'owner_race': 'White',
            'living_environment': 'Suburban',
            'daily_exercise_hours': 2.0
        }
        
        bias_score = generator.calculate_bias_score(human, dog)
        
        assert 0 <= bias_score <= 1
        assert isinstance(bias_score, float)
    
    def test_generate_interactions(self):
        """Test interactions generation."""
        generator = DogBehaviorGenerator(seed=42)
        
        # Generate small dataset
        humans_df = generator.generate_human_attributes(10)
        dogs_df = generator.generate_dog_attributes(5)
        interactions_df = generator.generate_interactions(humans_df, dogs_df, 20)
        
        assert len(interactions_df) == 20
        assert 'interaction_id' in interactions_df.columns
        assert 'person_id' in interactions_df.columns
        assert 'dog_id' in interactions_df.columns
        assert 'barks' in interactions_df.columns
        assert 'bias_score' in interactions_df.columns
        
        # Check that barks is boolean
        assert interactions_df['barks'].dtype == bool or interactions_df['barks'].dtype == int
    
    def test_generate_dataset(self):
        """Test complete dataset generation."""
        generator = DogBehaviorGenerator(seed=42)
        dataset = generator.generate_dataset(n_humans=50, n_dogs=10, n_interactions=100)
        
        assert 'humans' in dataset
        assert 'dogs' in dataset
        assert 'interactions' in dataset
        
        assert len(dataset['humans']) == 50
        assert len(dataset['dogs']) == 10
        assert len(dataset['interactions']) == 100
        
        # Check that interactions reference valid humans and dogs
        valid_humans = set(dataset['humans']['person_id'])
        valid_dogs = set(dataset['dogs']['dog_id'])
        
        assert set(dataset['interactions']['person_id']).issubset(valid_humans)
        assert set(dataset['interactions']['dog_id']).issubset(valid_dogs)
    
    def test_bias_patterns(self):
        """Test that bias patterns are present in the dataset."""
        generator = DogBehaviorGenerator(seed=42)
        dataset = generator.generate_dataset(n_humans=200, n_dogs=50, n_interactions=1000)
        
        interactions_df = dataset['interactions']
        
        # Check that different races have different barking rates
        race_rates = interactions_df.groupby('human_race')['barks'].mean()
        assert len(race_rates.unique()) > 1, "All races should not have the same barking rate"
        
        # Check that different genders have different barking rates
        gender_rates = interactions_df.groupby('human_gender')['barks'].mean()
        assert len(gender_rates.unique()) > 1, "All genders should not have the same barking rate"
        
        # Check that bias scores vary
        assert interactions_df['bias_score'].std() > 0, "Bias scores should vary"
    
    def test_reproducibility(self):
        """Test that results are reproducible with same seed."""
        generator1 = DogBehaviorGenerator(seed=42)
        generator2 = DogBehaviorGenerator(seed=42)
        
        dataset1 = generator1.generate_dataset(n_humans=50, n_dogs=10, n_interactions=100)
        dataset2 = generator2.generate_dataset(n_humans=50, n_dogs=10, n_interactions=100)
        
        # Check that results are identical
        pd.testing.assert_frame_equal(dataset1['humans'], dataset2['humans'])
        pd.testing.assert_frame_equal(dataset1['dogs'], dataset2['dogs'])
        pd.testing.assert_frame_equal(dataset1['interactions'], dataset2['interactions'])


if __name__ == "__main__":
    pytest.main([__file__])
