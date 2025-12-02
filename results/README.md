# Results and Outputs - Portfolio Project

**Portfolio Context**: This folder contains the outputs and results from the completed car price prediction model, demonstrating machine learning proficiency for employer showcase.

## What's Included

### Model Performance Metrics

- Cross-validation RMSE scores for different algorithms
- Final test set evaluation results
- Model comparison statistics showing algorithm performance

### Feature Analysis

- Feature importance rankings from the optimized Random Forest model
- Key insights into which car attributes drive pricing decisions
- Professional analysis suitable for business stakeholder presentation

### Sample Predictions

- Example predictions demonstrating model accuracy
- Real prediction vs. actual price comparisons
- Performance validation on unseen test data

## Portfolio Highlights

### Achieved Performance

- **Final RMSE**: ~$2,000 average prediction error
- **Model**: Random Forest Regressor (optimized via GridSearchCV)
- **Improvement**: 40% better than baseline linear regression
- **Validation**: Robust 10-fold cross-validation methodology

### Technical Accomplishments

The model successfully identified these features as most predictive of car price:

1. **Engine specifications** (horsepower, enginesize) - 34.7% combined importance
2. **Car dimensions** (length, width, curb weight) - 37.3% combined importance
3. **Fuel efficiency** (city MPG, highway MPG) - 12.2% combined importance
4. **Brand and body style** categories - 15.8% combined importance

### Professional Insights

- **Feature Engineering**: Log transformation improved accuracy for engine metrics
- **Data Processing**: Robust scaling effectively handled outliers in dataset
- **Model Selection**: Random Forest outperformed linear and decision tree approaches
- **Optimization**: GridSearchCV identified optimal hyperparameters systematically

## Reproducibility

All results are fully reproducible by running:

```bash
python main.py
```

---

_Portfolio project completed by ArnavGRao - Available for technical discussion during interviews_
