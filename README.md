# Car Price Prediction with Machine Learning

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.1+-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Portfolio](https://img.shields.io/badge/Portfolio-Project-blue.svg)](https://github.com/ArnavGRao/PredictCarPriceWithRegression)

**Portfolio Project**: A comprehensive machine learning project that predicts car prices using various regression algorithms. This project demonstrates data preprocessing, feature engineering, model comparison, and hyperparameter tuning techniques for showcase to potential employers.

## Project Overview

This project uses machine learning algorithms to predict car prices based on various features such as engine specifications, fuel type, body style, and more. The model is trained on a dataset containing detailed information about different car models and their corresponding prices.

## Dataset

**Source**: [Kaggle - Car Price Prediction Dataset](https://www.kaggle.com/datasets/hellbuoy/car-price-prediction/code?datasetId=383055&sortBy=voteCount)

The dataset contains information about cars with the following key features:

- **Engine specifications**: Engine size, horsepower, fuel system
- **Physical attributes**: Length, width, height, curb weight
- **Performance metrics**: City MPG, highway MPG, compression ratio
- **Categories**: Car company, fuel type, aspiration, body style, drive wheels
- **Target variable**: Price (what we're predicting)

### Dataset Files

- `CarPrice_Assignment.csv` - Main dataset with car features and prices
- `Data Dictionary - carprices.xlsx` - Detailed description of all features

## Technologies Used

- **Python 3.x**
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **scikit-learn** - Machine learning algorithms and tools
- **matplotlib** - Data visualization
- **Custom transformers** - Log transformation for specific features

## Project Structure

```
PredictCarPrice/
│
├── dataset/
│   ├── CarPrice_Assignment.csv       # Main dataset
│   └── Data Dictionary - carprices.xlsx  # Feature descriptions
│
├── main.py                          # Main script with model training
├── loadData.py                      # Data loading and splitting utilities
├── dataCleanup.py                   # Data preprocessing and feature engineering
├── custom_transformers.py           # Custom sklearn transformers
├── .gitignore                       # Git ignore file
└── README.md                        # This file
```

## Features & Data Processing

### Feature Engineering

- **Log transformation** applied to `horsepower` and `enginesize` for better distribution
- **Robust scaling** for numerical features to handle outliers
- **One-hot encoding** for categorical variables
- **Custom pipeline** for seamless data preprocessing

### Data Preprocessing Pipeline

1. **LogTransformer**: Applies log transformation to specified numerical features
2. **RobustScaler**: Scales numerical features while being robust to outliers
3. **OneHotEncoder**: Converts categorical variables to numerical format

## Machine Learning Models

The project evaluates multiple regression algorithms:

1. **Linear Regression** - Baseline model
2. **Decision Tree Regressor** - Non-linear relationships
3. **Random Forest Regressor** - Ensemble method (final choice)

### Model Selection Process

- **Cross-validation** with 10 folds for robust evaluation
- **Grid Search** for hyperparameter tuning
- **RMSE (Root Mean Square Error)** as the primary evaluation metric

### Hyperparameter Tuning

The Random Forest model is optimized using GridSearchCV with the following parameters:

- `n_estimators`: [3, 10, 30]
- `max_features`: [2, 4, 6, 8]
- `bootstrap`: [True, False]

## Results

The final Random Forest model provides:

- **Cross-validation RMSE** scores with mean and standard deviation
- **Test set RMSE** for final model evaluation
- **Feature importance** analysis showing which car attributes most influence price

## How to Run

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ArnavGRao/PredictCarPriceWithRegression.git
   cd PredictCarPriceWithRegression
   ```

2. **Install required packages**:

   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:

   ```bash
   pip install pandas numpy scikit-learn matplotlib scipy seaborn
   ```

3. **Run the main script**:
   ```bash
   python main.py
   ```

## Key Functions

### `main.py`

- Main execution script
- Model training, evaluation, and comparison
- Hyperparameter tuning with GridSearchCV
- Final model evaluation and feature importance analysis

### `loadData.py`

- Data loading utilities
- Train-test split functionality

### `dataCleanup.py`

- Data preprocessing functions
- Feature engineering pipeline

### `custom_transformers.py`

- `LogTransformer`: Custom sklearn transformer for log transformation

## Model Performance

The project includes comprehensive model evaluation:

- **Cross-validation scores** for model reliability
- **Grid search results** for optimal hyperparameters
- **Feature importance rankings** to understand which car attributes drive price predictions
- **Test set evaluation** for final model performance assessment

## Key Learnings

This portfolio project demonstrates:

- **End-to-end ML pipeline** from data loading to model evaluation
- **Proper data preprocessing** techniques for mixed data types
- **Model comparison** and selection methodology
- **Hyperparameter optimization** using grid search
- **Custom transformer creation** for specialized preprocessing needs

## Author

**ArnavGRao**

- GitHub: [@ArnavGRao](https://github.com/ArnavGRao)
- Email: arnavgrao@gmail.com

## License

This project is open source and available under the MIT License.
