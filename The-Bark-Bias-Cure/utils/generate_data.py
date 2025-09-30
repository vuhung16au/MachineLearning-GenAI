"""
Generate synthetic dog behavior dataset for bias analysis.

This script creates a fun, synthetic dataset that demonstrates patterns
in dog behavior based on various human attributes.
"""

import numpy as np
import pandas as pd
import random
from typing import List, Dict, Any
import json
from pathlib import Path


class DogBehaviorGenerator:
    """Generate synthetic dog behavior data with bias patterns."""
    
    def __init__(self, seed: int = 42):
        """Initialize the generator with a random seed."""
        np.random.seed(seed)
        random.seed(seed)
        
        # Define human attributes
        self.races = ['White', 'Black', 'Asian', 'Hispanic', 'Middle Eastern', 'Native American']
        self.genders = ['Male', 'Female', 'Non-binary']
        self.skin_colors = ['Light', 'Medium', 'Dark']
        self.age_groups = ['Child', 'Teen', 'Young Adult', 'Middle-aged', 'Senior']
        self.clothing_styles = ['Casual', 'Formal', 'Athletic', 'Traditional', 'Alternative']
        self.heights = ['Short', 'Average', 'Tall']
        self.voice_pitches = ['High', 'Medium', 'Low']
        
        # Dog attributes
        self.dog_breeds = ['Labrador', 'German Shepherd', 'Golden Retriever', 'Bulldog', 
                          'Poodle', 'Beagle', 'Rottweiler', 'Siberian Husky']
        self.dog_ages = list(range(1, 16))  # 1-15 years
        self.dog_training_levels = ['Untrained', 'Basic', 'Intermediate', 'Advanced']
        self.dog_temperaments = ['Calm', 'Energetic', 'Aggressive', 'Friendly', 'Shy']
        
    def generate_human_attributes(self, n_samples: int) -> pd.DataFrame:
        """Generate human attributes for the dataset."""
        data = []
        
        for _ in range(n_samples):
            # Create some correlation between attributes for realism
            race = np.random.choice(self.races)
            
            # Some races more likely to have certain skin colors
            if race in ['White']:
                skin_color = np.random.choice(self.skin_colors, p=[0.7, 0.25, 0.05])
            elif race in ['Black']:
                skin_color = np.random.choice(self.skin_colors, p=[0.05, 0.25, 0.7])
            elif race in ['Asian']:
                skin_color = np.random.choice(self.skin_colors, p=[0.1, 0.7, 0.2])
            else:
                skin_color = np.random.choice(self.skin_colors)
            
            person = {
                'person_id': f"P_{len(data):06d}",
                'race': race,
                'gender': np.random.choice(self.genders),
                'skin_color': skin_color,
                'age_group': np.random.choice(self.age_groups),
                'clothing_style': np.random.choice(self.clothing_styles),
                'height': np.random.choice(self.heights),
                'voice_pitch': np.random.choice(self.voice_pitches),
                'age_years': np.random.randint(5, 80),
                'has_glasses': np.random.choice([True, False], p=[0.3, 0.7]),
                'has_hat': np.random.choice([True, False], p=[0.2, 0.8]),
                'is_smiling': np.random.choice([True, False], p=[0.6, 0.4]),
                'movement_speed': np.random.choice(['Slow', 'Normal', 'Fast']),
                'body_language': np.random.choice(['Relaxed', 'Tense', 'Confident', 'Nervous'])
            }
            data.append(person)
        
        return pd.DataFrame(data)
    
    def generate_dog_attributes(self, n_dogs: int) -> pd.DataFrame:
        """Generate dog attributes for the dataset."""
        data = []
        
        for _ in range(n_dogs):
            dog = {
                'dog_id': f"D_{len(data):06d}",
                'breed': np.random.choice(self.dog_breeds),
                'age_months': np.random.randint(3, 180),  # 3 months to 15 years
                'training_level': np.random.choice(self.dog_training_levels),
                'temperament': np.random.choice(self.dog_temperaments),
                'size': np.random.choice(['Small', 'Medium', 'Large']),
                'energy_level': np.random.choice(['Low', 'Medium', 'High']),
                'socialization_score': np.random.uniform(0, 10),  # 0-10 scale
                'previous_negative_experiences': np.random.randint(0, 5),
                'owner_race': np.random.choice(self.races),  # Dog's owner's race
                'living_environment': np.random.choice(['Urban', 'Suburban', 'Rural']),
                'daily_exercise_hours': np.random.uniform(0.5, 4.0)
            }
            data.append(dog)
        
        return pd.DataFrame(data)
    
    def calculate_bias_score(self, human: Dict, dog: Dict) -> float:
        """
        Calculate a bias score based on human and dog attributes.
        This is where we introduce the 'racist' behavior patterns.
        """
        bias_score = 0.0
        
        # Base barking probability
        base_prob = 0.1
        
        # Dog-specific factors
        if dog['temperament'] == 'Aggressive':
            bias_score += 0.3
        elif dog['temperament'] == 'Shy':
            bias_score -= 0.1
        
        if dog['training_level'] == 'Untrained':
            bias_score += 0.2
        elif dog['training_level'] == 'Advanced':
            bias_score -= 0.15
        
        if dog['previous_negative_experiences'] > 2:
            bias_score += 0.1
        
        # Human-specific bias factors (the "racist" part)
        # This is intentionally biased to demonstrate the problem
        
        # Race-based bias
        if human['race'] == 'Black':
            bias_score += 0.25  # Higher chance of barking
        elif human['race'] == 'Asian':
            bias_score += 0.15
        elif human['race'] == 'Hispanic':
            bias_score += 0.1
        elif human['race'] == 'White':
            bias_score -= 0.05  # Lower chance of barking
        
        # Gender bias
        if human['gender'] == 'Male':
            bias_score += 0.05
        elif human['gender'] == 'Non-binary':
            bias_score += 0.1
        
        # Age bias
        if human['age_group'] == 'Child':
            bias_score += 0.1  # Dogs might be more reactive to children
        elif human['age_group'] == 'Senior':
            bias_score -= 0.05
        
        # Skin color bias (additional to race)
        if human['skin_color'] == 'Dark':
            bias_score += 0.1
        elif human['skin_color'] == 'Light':
            bias_score -= 0.05
        
        # Clothing and appearance bias
        if human['clothing_style'] == 'Traditional':
            bias_score -= 0.05  # More familiar
        elif human['clothing_style'] == 'Alternative':
            bias_score += 0.1
        
        if human['has_hat']:
            bias_score += 0.05  # Hats can make dogs nervous
        
        # Dog-owner race matching effect
        if dog['owner_race'] == human['race']:
            bias_score -= 0.1  # Less likely to bark at same race as owner
        
        # Environmental factors
        if dog['living_environment'] == 'Urban':
            bias_score += 0.05  # More exposure, but also more stress
        
        # Interaction effects
        if human['body_language'] == 'Tense':
            bias_score += 0.1
        elif human['body_language'] == 'Confident':
            bias_score -= 0.05
        
        if human['movement_speed'] == 'Fast':
            bias_score += 0.1
        
        # Add some randomness
        noise = np.random.normal(0, 0.05)
        bias_score += noise
        
        # Ensure score is between 0 and 1
        bias_score = max(0, min(1, base_prob + bias_score))
        
        return bias_score
    
    def generate_interactions(self, humans_df: pd.DataFrame, dogs_df: pd.DataFrame, 
                            n_interactions: int) -> pd.DataFrame:
        """Generate dog-human interactions with bias patterns."""
        interactions = []
        
        for _ in range(n_interactions):
            human = humans_df.sample(1).iloc[0].to_dict()
            dog = dogs_df.sample(1).iloc[0].to_dict()
            
            # Calculate bias score
            bias_score = self.calculate_bias_score(human, dog)
            
            # Determine if dog barks
            barks = np.random.random() < bias_score
            
            # Additional behavior details
            if barks:
                intensity = np.random.choice(['Low', 'Medium', 'High'], 
                                          p=[0.4, 0.4, 0.2])
                duration = np.random.uniform(1, 30)  # seconds
                triggers = []
                
                # Determine what triggered the barking
                if bias_score > 0.5:
                    triggers.append('Appearance')
                if human['movement_speed'] == 'Fast':
                    triggers.append('Movement')
                if human['body_language'] == 'Tense':
                    triggers.append('Body Language')
                if human['voice_pitch'] == 'High':
                    triggers.append('Voice')
                
                if not triggers:
                    triggers = ['Unknown']
            else:
                intensity = 'None'
                duration = 0
                triggers = []
            
            interaction = {
                'interaction_id': f"I_{len(interactions):08d}",
                'person_id': human['person_id'],
                'dog_id': dog['dog_id'],
                'timestamp': pd.Timestamp.now() - pd.Timedelta(days=np.random.randint(0, 365)),
                'location': np.random.choice(['Park', 'Street', 'Home', 'Park', 'Vet']),
                'barks': barks,
                'bias_score': bias_score,
                'bark_intensity': intensity,
                'bark_duration': duration,
                'triggers': '; '.join(triggers) if triggers else 'None',
                'distance_meters': np.random.uniform(1, 20),
                'human_approach_speed': human['movement_speed'],
                'dog_was_sleeping': np.random.choice([True, False], p=[0.2, 0.8]),
                'other_dogs_present': np.random.choice([True, False], p=[0.3, 0.7]),
                'weather': np.random.choice(['Sunny', 'Cloudy', 'Rainy', 'Windy']),
                'time_of_day': np.random.choice(['Morning', 'Afternoon', 'Evening', 'Night'])
            }
            
            # Add all human and dog attributes to the interaction
            for key, value in human.items():
                if key != 'person_id':
                    interaction[f'human_{key}'] = value
            
            for key, value in dog.items():
                if key != 'dog_id':
                    interaction[f'dog_{key}'] = value
            
            interactions.append(interaction)
        
        return pd.DataFrame(interactions)
    
    def generate_dataset(self, n_humans: int = 1000, n_dogs: int = 200, 
                        n_interactions: int = 5000) -> Dict[str, pd.DataFrame]:
        """Generate the complete dataset."""
        print("Generating human attributes...")
        humans_df = self.generate_human_attributes(n_humans)
        
        print("Generating dog attributes...")
        dogs_df = self.generate_dog_attributes(n_dogs)
        
        print("Generating interactions...")
        interactions_df = self.generate_interactions(humans_df, dogs_df, n_interactions)
        
        return {
            'humans': humans_df,
            'dogs': dogs_df,
            'interactions': interactions_df
        }


def main():
    """Generate and save the dataset."""
    generator = DogBehaviorGenerator(seed=42)
    
    print("🐕 Generating The Bark Bias Cure Dataset...")
    print("=" * 50)
    
    # Generate dataset
    dataset = generator.generate_dataset(
        n_humans=1000,
        n_dogs=200, 
        n_interactions=5000
    )
    
    # Create data directory
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Save datasets
    print("\n💾 Saving datasets...")
    dataset['humans'].to_csv(data_dir / "humans.csv", index=False)
    dataset['dogs'].to_csv(data_dir / "dogs.csv", index=False)
    dataset['interactions'].to_csv(data_dir / "interactions.csv", index=False)
    
    # Save combined dataset for modeling
    combined_df = dataset['interactions'].copy()
    combined_df.to_csv(data_dir / "dog_behavior_dataset.csv", index=False)
    
    # Generate summary statistics
    print("\n📊 Dataset Summary:")
    print(f"Total humans: {len(dataset['humans'])}")
    print(f"Total dogs: {len(dataset['dogs'])}")
    print(f"Total interactions: {len(dataset['interactions'])}")
    print(f"Barking incidents: {dataset['interactions']['barks'].sum()}")
    print(f"Barking rate: {dataset['interactions']['barks'].mean():.2%}")
    
    # Bias analysis
    print("\n🔍 Bias Analysis:")
    bias_by_race = dataset['interactions'].groupby('human_race')['barks'].agg(['count', 'sum', 'mean'])
    print("\nBarking rate by race:")
    for race in bias_by_race.index:
        rate = bias_by_race.loc[race, 'mean']
        count = bias_by_race.loc[race, 'count']
        print(f"  {race}: {rate:.2%} ({bias_by_race.loc[race, 'sum']}/{count})")
    
    bias_by_gender = dataset['interactions'].groupby('human_gender')['barks'].agg(['count', 'sum', 'mean'])
    print("\nBarking rate by gender:")
    for gender in bias_by_gender.index:
        rate = bias_by_gender.loc[gender, 'mean']
        count = bias_by_gender.loc[gender, 'count']
        print(f"  {gender}: {rate:.2%} ({bias_by_gender.loc[gender, 'sum']}/{count})")
    
    # Save metadata
    metadata = {
        'generation_date': pd.Timestamp.now().isoformat(),
        'n_humans': len(dataset['humans']),
        'n_dogs': len(dataset['dogs']),
        'n_interactions': len(dataset['interactions']),
        'barking_rate': float(dataset['interactions']['barks'].mean()),
        'races': generator.races,
        'genders': generator.genders,
        'dog_breeds': generator.dog_breeds,
        'description': 'Synthetic dataset demonstrating bias patterns in dog behavior'
    }
    
    with open(data_dir / "metadata.json", 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"\n✅ Dataset saved to {data_dir}/")
    print("Files created:")
    print("  - humans.csv")
    print("  - dogs.csv") 
    print("  - interactions.csv")
    print("  - dog_behavior_dataset.csv")
    print("  - metadata.json")


if __name__ == "__main__":
    main()
