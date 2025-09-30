# The Bark Bias Cure Dataset 📊

This document provides a comprehensive description of the synthetic dog behavior dataset used in The Bark Bias Cure project. The dataset is designed to demonstrate bias patterns in AI systems through a fun, educational example of dog behavior classification.

## 📁 Dataset Files

The dataset consists of four main CSV files:

1. **`humans.csv`** - Human attributes and demographics
2. **`dogs.csv`** - Dog attributes and characteristics  
3. **`interactions.csv`** - Individual dog-human interaction records
4. **`dog_behavior_dataset.csv`** - Combined dataset for machine learning (same as interactions.csv)

## 🧑‍🤝‍🧑 Human Attributes (`humans.csv`)

### Demographics
- **`person_id`** (string): Unique identifier for each person (format: P_XXXXXX)
- **`race`** (categorical): Racial/ethnic background
  - Values: `['White', 'Black', 'Asian', 'Hispanic', 'Middle Eastern', 'Native American']`
- **`gender`** (categorical): Gender identity
  - Values: `['Male', 'Female', 'Non-binary']`
- **`skin_color`** (categorical): Skin tone classification
  - Values: `['Light', 'Medium', 'Dark']`
- **`age_group`** (categorical): Age category
  - Values: `['Child', 'Teen', 'Young Adult', 'Middle-aged', 'Senior']`
- **`age_years`** (integer): Exact age in years (5-80)

### Physical Attributes
- **`height`** (categorical): Height category
  - Values: `['Short', 'Average', 'Tall']`
- **`voice_pitch`** (categorical): Voice pitch level
  - Values: `['High', 'Medium', 'Low']`
- **`clothing_style`** (categorical): Clothing preference
  - Values: `['Casual', 'Formal', 'Athletic', 'Traditional', 'Alternative']`

### Behavioral Attributes
- **`movement_speed`** (categorical): Walking/movement pace
  - Values: `['Slow', 'Normal', 'Fast']`
- **`body_language`** (categorical): Body posture and demeanor
  - Values: `['Relaxed', 'Tense', 'Confident', 'Nervous']`
- **`is_smiling`** (boolean): Whether the person is smiling
- **`has_glasses`** (boolean): Whether wearing glasses
- **`has_hat`** (boolean): Whether wearing a hat

## 🐕 Dog Attributes (`dogs.csv`)

### Basic Information
- **`dog_id`** (string): Unique identifier for each dog (format: D_XXXXXX)
- **`breed`** (categorical): Dog breed
  - Values: `['Labrador', 'German Shepherd', 'Golden Retriever', 'Bulldog', 'Poodle', 'Beagle', 'Rottweiler', 'Siberian Husky']`
- **`age_months`** (integer): Age in months (3-180, equivalent to 3 months to 15 years)
- **`size`** (categorical): Dog size category
  - Values: `['Small', 'Medium', 'Large']`

### Training & Behavior
- **`training_level`** (categorical): Level of training
  - Values: `['Untrained', 'Basic', 'Intermediate', 'Advanced']`
- **`temperament`** (categorical): Dog's personality type
  - Values: `['Calm', 'Energetic', 'Aggressive', 'Friendly', 'Shy']`
- **`energy_level`** (categorical): Activity level
  - Values: `['Low', 'Medium', 'High']`
- **`socialization_score`** (float): Socialization quality (0-10 scale)
- **`previous_negative_experiences`** (integer): Number of negative experiences (0-4)

### Environment & Ownership
- **`owner_race`** (categorical): Race of the dog's owner
  - Values: Same as human race categories
- **`living_environment`** (categorical): Living situation
  - Values: `['Urban', 'Suburban', 'Rural']`
- **`daily_exercise_hours`** (float): Hours of daily exercise (0.5-4.0)

## 🤝 Interaction Records (`interactions.csv`)

### Interaction Metadata
- **`interaction_id`** (string): Unique identifier for each interaction (format: I_XXXXXXXX)
- **`person_id`** (string): Reference to human in the interaction
- **`dog_id`** (string): Reference to dog in the interaction
- **`timestamp`** (datetime): When the interaction occurred
- **`location`** (categorical): Where the interaction took place
  - Values: `['Park', 'Street', 'Home', 'Vet']`

### Behavior Outcomes
- **`barks`** (boolean): Whether the dog barked at the person (target variable)
- **`bias_score`** (float): Calculated bias score (0-1) based on attributes
- **`bark_intensity`** (categorical): Intensity of barking
  - Values: `['None', 'Low', 'Medium', 'High']`
- **`bark_duration`** (float): Duration of barking in seconds (0-30)
- **`triggers`** (string): What triggered the barking
  - Values: `['Appearance', 'Movement', 'Body Language', 'Voice', 'Unknown', 'None']`

### Contextual Factors
- **`distance_meters`** (float): Distance between human and dog (1-20 meters)
- **`human_approach_speed`** (categorical): How fast the human was moving
  - Values: `['Slow', 'Normal', 'Fast']`
- **`dog_was_sleeping`** (boolean): Whether the dog was sleeping before interaction
- **`other_dogs_present`** (boolean): Whether other dogs were present
- **`weather`** (categorical): Weather conditions
  - Values: `['Sunny', 'Cloudy', 'Rainy', 'Windy']`
- **`time_of_day`** (categorical): Time when interaction occurred
  - Values: `['Morning', 'Afternoon', 'Evening', 'Night']`

### Human Attributes (Duplicated from humans.csv)
All human attributes are included with `human_` prefix:
- `human_race`, `human_gender`, `human_skin_color`, `human_age_group`
- `human_age_years`, `human_clothing_style`, `human_height`, `human_voice_pitch`
- `human_has_glasses`, `human_has_hat`, `human_is_smiling`
- `human_movement_speed`, `human_body_language`

### Dog Attributes (Duplicated from dogs.csv)
All dog attributes are included with `dog_` prefix:
- `dog_breed`, `dog_age_months`, `dog_training_level`, `dog_temperament`
- `dog_size`, `dog_energy_level`, `dog_socialization_score`
- `dog_previous_negative_experiences`, `dog_owner_race`, `dog_living_environment`
- `dog_daily_exercise_hours`

## 📊 Dataset Statistics

### Size
- **Total Humans**: 1,000 unique individuals
- **Total Dogs**: 200 unique dogs
- **Total Interactions**: 5,000 dog-human encounters
- **Overall Barking Rate**: ~30% (varies by demographic group)

### Bias Patterns (Intentionally Introduced)

#### Racial Bias
- **Black individuals**: Highest barking rate (~45-50%)
- **Asian individuals**: High barking rate (~35-40%)
- **Hispanic individuals**: Moderate-high barking rate (~30-35%)
- **White individuals**: Lowest barking rate (~20-25%)
- **Middle Eastern/Native American**: Moderate barking rate (~25-30%)

#### Gender Bias
- **Non-binary individuals**: Highest barking rate (~35-40%)
- **Male individuals**: Moderate-high barking rate (~30-35%)
- **Female individuals**: Lowest barking rate (~25-30%)

#### Age Bias
- **Children**: Higher reactivity due to unpredictable movement
- **Seniors**: Lower reactivity due to slower, more predictable movement
- **Young Adults**: Moderate reactivity
- **Middle-aged**: Moderate reactivity

#### Appearance Bias
- **Hats**: Increase barking probability (dogs may be nervous about head coverings)
- **Glasses**: Neutral effect
- **Clothing Style**: Traditional clothing reduces barking, alternative clothing increases it
- **Body Language**: Tense or nervous body language increases barking

## 🎯 Machine Learning Features

### Primary Features (25+ attributes)
The model uses the following features for prediction:

#### Human Features
- `human_race`, `human_gender`, `human_skin_color`, `human_age_group`
- `human_clothing_style`, `human_height`, `human_voice_pitch`
- `human_age_years`, `human_has_glasses`, `human_has_hat`, `human_is_smiling`
- `human_movement_speed`, `human_body_language`

#### Dog Features
- `dog_breed`, `dog_age_months`, `dog_training_level`, `dog_temperament`
- `dog_size`, `dog_energy_level`, `dog_socialization_score`
- `dog_previous_negative_experiences`, `dog_owner_race`, `dog_living_environment`
- `dog_daily_exercise_hours`

#### Context Features
- `distance_meters`, `human_approach_speed`, `dog_was_sleeping`
- `other_dogs_present`, `weather`, `time_of_day`

### Target Variable
- **`barks`** (boolean): Whether the dog barked at the person (0 = No Bark, 1 = Bark)

## 🔍 Bias Analysis

### Statistical Parity Differences
- **Race**: ~25-30% difference between highest and lowest groups
- **Gender**: ~10-15% difference between groups
- **Age**: ~15-20% difference between age groups

### Feature Importance Patterns
The model typically shows high importance for:
1. **Demographic features** (race, gender, age) - indicating bias
2. **Dog temperament and training** - legitimate behavioral factors
3. **Contextual factors** (distance, approach speed) - environmental factors
4. **Appearance factors** (clothing, accessories) - potential bias sources

## 📈 Usage Examples

### Loading the Dataset
```python
import pandas as pd

# Load individual components
humans = pd.read_csv('data/humans.csv')
dogs = pd.read_csv('data/dogs.csv')
interactions = pd.read_csv('data/interactions.csv')

# Load combined dataset for modeling
df = pd.read_csv('data/dog_behavior_dataset.csv')
```

### Basic Analysis
```python
# Analyze bias by race
bias_by_race = df.groupby('human_race')['barks'].mean()
print(bias_by_race)

# Analyze bias by gender
bias_by_gender = df.groupby('human_gender')['barks'].mean()
print(bias_by_gender)

# Feature importance analysis
feature_importance = df.corr()['barks'].abs().sort_values(ascending=False)
print(feature_importance.head(10))
```

### Bias Detection
```python
# Calculate statistical parity difference
race_rates = df.groupby('human_race')['barks'].mean()
spd = race_rates.max() - race_rates.min()
print(f"Statistical Parity Difference: {spd:.3f}")

# Analyze prediction bias
# (This would require a trained model)
```

## ⚠️ Important Notes

### Synthetic Nature
- This is a **synthetic dataset** created for educational purposes
- The bias patterns are **intentionally introduced** to demonstrate AI bias
- **Do not use this data for real-world decisions** about dog behavior
- The scenario is fictional but the bias principles are real

### Educational Purpose
- Designed to teach about bias in AI systems
- Demonstrates how bias can manifest in machine learning
- Shows techniques for bias detection and mitigation
- Provides tools for fairness analysis

### Ethical Considerations
- The "racist dog" concept is a metaphor for AI bias
- Real dogs are not inherently biased - this is a teaching tool
- Focus on the underlying principles of fairness in AI
- Use responsibly for educational purposes only

## 🔗 Related Files

- **`../notebooks/dog_behavior_analysis.ipynb`**: Interactive analysis notebook
- **`../utils/generate_data.py`**: Dataset generation script
- **`../utils/train_model.py`**: Model training script
- **`../utils/evaluate_model.py`**: Bias evaluation script


---

**Remember**: This dataset is designed to educate about bias in AI systems. The principles demonstrated here apply to real-world AI applications in healthcare, finance, criminal justice, and other domains where fairness is crucial. 🐕✨
