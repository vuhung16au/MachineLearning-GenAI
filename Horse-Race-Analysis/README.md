# Horse Race Analysis

This project provides tools and analysis for horse racing data.

Refer to the [Notebooks](Horse-Race-Analysis.ipynb) for detailed analysis and insights, including data preprocessing, model training, evaluation, as well as visualizations and key findings.

## Development Environment Setup

Follow these steps to set up your development environment:

### Prerequisites

- Python 3.10 or 3.11

### Setup Instructions

1. **Create a virtual environment**

   ```bash
   python3.11 -m venv .venv
   ```

2. **Activate the virtual environment**

   ```bash
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Deactivating the Environment

When you're done working, you can deactivate the virtual environment:

```bash
deactivate
```

## Project Structure

```text
Horse-Race-Analysis/
├── data/
│   ├── field.csv
│   ├── gear_changes.csv
│   ├── horses.csv
│   ├── horses1.csv
│   ├── horses2.csv
│   └── README.md
├── docs/
│   ├── gear_changes.md
│   ├── horse-race-fields.md
│   ├── horses.md
│   └── key-concepts.md
├── model/
│   ├── nn_model.h5
│   └── nn_model.keras
├── Horse-Race-Analysis.ipynb
├── Horse-Race-Analysis-DeepDive.ipynb
├── Prompt.md
├── README.md
└── requirements.txt
```

## Data

The `data/` directory contains various CSV files with horse racing information. See `data/README.md` for more details about the data structure and contents.

## Running on Google Colab

If you want to run this project on Google Colab, follow these steps:

### Option 1: Clone the Repository

1. **Open Google Colab** in your browser: [https://colab.research.google.com](https://colab.research.google.com)

2. **Create a new notebook** or open an existing one

3. **Clone the repository** by running this command in a code cell:

   ```python
   !git clone https://github.com/vuhung16au/MachineLearning-GenAI.git
   ```

4. **Navigate to the project directory**:

   ```python
   import os
   os.chdir('/content/MachineLearning-GenAI/Horse-Race-Analysis')
   ```

5. **Install the required dependencies**:

   ```python
   !pip install -r requirements.txt
   ```

6. **List the files** to verify everything is downloaded:

   ```python
   !ls -la
   ```

### Option 2: Direct Notebook Access

You can also directly open the Jupyter notebooks in Google Colab:

- **Main Analysis Notebook**:
  [Open Horse-Race-Analysis.ipynb in Colab](https://colab.research.google.com/github/vuhung16au/MachineLearning-GenAI/blob/main/Horse-Race-Analysis/Horse-Race-Analysis.ipynb)

- **Deep Dive Analysis Notebook**:
  [Open Horse-Race-Analysis-DeepDive.ipynb in Colab](https://colab.research.google.com/github/vuhung16au/MachineLearning-GenAI/blob/main/Horse-Race-Analysis/Horse-Race-Analysis-DeepDive.ipynb)

### Working with Data in Colab

When working in Google Colab, the data files will be automatically available after cloning the repository. You can access them using relative paths:

```python
import pandas as pd

# Load the data files
horses_df = pd.read_csv('data/horses.csv')
field_df = pd.read_csv('data/field.csv')
gear_changes_df = pd.read_csv('data/gear_changes.csv')
```

### Loading Pre-trained Models

If you need to load the pre-trained neural network models:

```python
from tensorflow.keras.models import load_model

# Load the saved model
model = load_model('model/nn_model.keras')
# or (oldered for compatibility with older versions)
# model = load_model('model/nn_model.h5')
```

### Tips for Google Colab

- **Runtime**: Use GPU runtime for faster training if working with neural networks
- **File persistence**: Files will be deleted when the runtime disconnects. Consider mounting Google Drive for persistent storage
- **Dependencies**: All required packages will be installed via the requirements.txt file