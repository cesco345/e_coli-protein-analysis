# E. coli Protein Analysis Project

## Project Structure

## Setup and Execution

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation

1. Clone the repository:
   git clone https://github.com/cesco345/e_coli-protein-analysis.git
   cd ecoli-protein-analysis

2. Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate # On Windows, use venv\Scripts\activate

3. Install the required packages:
   pip install -r requirements.txt

### Executing the Workflow

1. Fetch and prepare the dataset:
   python src/data/load_data.py
   This will download the E. coli dataset and save it in `data/raw/`.

2. Preprocess the data:
   python src/data/preprocess.py
   This will preprocess the raw data and save the result in `data/processed/`.

3. Explore the data:
   jupyter notebook notebooks/01_data_exploration.ipynb
   This notebook provides visualizations and insights about the dataset.

4. Train the model:
   jupyter notebook notebooks/02_model_training.ipynb
   This notebook trains the PyTorch model on the preprocessed data and evaluates its performance.

5. Analyze results:
   jupyter notebook notebooks/03_results_analysis.ipynb
   This notebook provides in-depth analysis of the model's predictions and performance metrics.

### Running Tests

Execute the test suite to ensure everything is working correctly:
python -m unittest discover tests

## Project Overview

# E. coli Protein Analysis Project

## Project Structure

### `data/`

Contains raw and processed data files.

- `raw/`: Stores the original dataset.
- `processed/`: Stores any preprocessed data.

### `src/`

Contains the main source code.

- `data/`: Modules for data loading and preprocessing.
- `models/`: Defines the PyTorch model architecture.
- `utils/`: Utility functions, including visualization tools.

### `notebooks/`

Jupyter notebooks for exploration, training, and analysis.

### `tests/`

Contains unit tests for data loading and model functionality.

### `configs/`

Stores configuration files for model parameters.

### `requirements.txt`

Lists all Python dependencies.

### `setup.py`

Setup script for the project.

### `README.md`

Project description and instructions.

## Key Python Files

- `src/data/load_data.py`: Functions to load the E. coli dataset.
- `src/data/preprocess.py`: Data preprocessing functions.
- `src/models/ecoli_model.py`: PyTorch model definition.
- `src/utils/visualization.py`: Functions for data and results visualization.

## Scalability and Future Expansions

This structure is scalable and can accommodate future expansions, such as:

- Adding more complex protein analysis models.
- Incorporating sequence data processing for AlphaFold-like models.
- Including additional datasets or protein families.
- Implementing more sophisticated data preprocessing pipelines.

## Project Overview

This project separates data loading, preprocessing, model definition, and visualization into distinct modules, making the code more organized and easier to maintain. The Jupyter notebooks allow for interactive exploration and analysis of the data and model results.
