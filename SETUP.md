# Project Setup Guide

This guide will help you set up the Car Price Prediction project on your local machine.

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

**For Linux/Mac:**
```bash
./activate_env.sh
```

**For Windows:**
```cmd
activate_env.bat
```

The script will:
- Create virtual environment if it doesn't exist
- Install all required dependencies
- Activate the environment
- Display available commands

### Option 2: Manual Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ArnavGRao/PredictCarPriceWithRegression.git
   cd PredictCarPriceWithRegression
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv .venv
   ```

3. **Activate virtual environment**
   
   **Linux/Mac:**
   ```bash
   source .venv/bin/activate
   ```
   
   **Windows:**
   ```cmd
   .venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements-simple.txt
   ```

## 📋 Requirements

### System Requirements
- Python 3.8 or higher
- 2GB+ RAM (for loading dataset)
- ~500MB disk space (including virtual environment)

### Python Dependencies
The project uses these main libraries:
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms
- **matplotlib**: Data visualization
- **seaborn**: Statistical data visualization
- **jupyter**: Interactive development environment

## 🔧 Verification

After setup, verify everything works:

```bash
# Test core imports
python -c "import pandas, numpy, sklearn, matplotlib; print('✅ All libraries imported successfully!')"

# Run quick test
python examples/quick_start.py

# Run full pipeline
python main.py
```

## 📂 Project Structure

```
PredictCarPrice/
├── .venv/                    # Virtual environment (created during setup)
├── dataset/                  # Dataset files
├── examples/                 # Example scripts and tutorials
├── results/                  # Model outputs and results
├── main.py                   # Main ML pipeline
├── dataCleanup.py           # Data preprocessing functions
├── loadData.py              # Data loading utilities
├── custom_transformers.py   # Custom sklearn transformers
├── requirements.txt         # Detailed dependencies
├── requirements-simple.txt  # Simplified dependencies
├── activate_env.sh          # Linux/Mac setup script
├── activate_env.bat         # Windows setup script
└── README.md               # Project documentation
```

## 🐍 Virtual Environment Management

### Activating Environment
**Linux/Mac:**
```bash
source .venv/bin/activate
```

**Windows:**
```cmd
.venv\Scripts\activate
```

### Deactivating Environment
```bash
deactivate
```

### Reinstalling Dependencies
```bash
pip install -r requirements-simple.txt --force-reinstall
```

## 🚨 Troubleshooting

### Common Issues

**1. Python not found**
- Ensure Python 3.8+ is installed
- Try `python3` instead of `python`
- On Windows, ensure Python is in PATH

**2. Permission denied (Linux/Mac)**
```bash
chmod +x activate_env.sh
./activate_env.sh
```

**3. Virtual environment creation fails**
```bash
# Install venv if missing (Ubuntu/Debian)
sudo apt-get install python3-venv

# Or use pip
pip install virtualenv
virtualenv .venv
```

**4. Import errors after installation**
```bash
# Ensure you're in the virtual environment
which python  # Should show .venv/bin/python

# Reinstall dependencies
pip install -r requirements-simple.txt --force-reinstall
```

**5. Jupyter notebook not starting**
```bash
# Install jupyter in virtual environment
pip install jupyter

# Or use the detailed requirements
pip install -r requirements.txt
```

### Environment Variables

No special environment variables are required for this project.

### Dataset Issues

If you encounter dataset loading issues:
1. Ensure `dataset/CarPrice_Assignment.csv` exists
2. Check file permissions
3. Verify the file isn't corrupted

## 💻 Development Setup

For development work:

1. **Install additional tools**
   ```bash
   pip install black flake8 pytest
   ```

2. **Code formatting**
   ```bash
   black *.py
   ```

3. **Code linting**
   ```bash
   flake8 *.py
   ```

## 🎯 Running the Project

### Full ML Pipeline
```bash
python main.py
```
Expected output:
- Model training progress
- Cross-validation scores
- Feature importance rankings
- Final test set evaluation

### Quick Example
```bash
python examples/quick_start.py
```
Expected output:
- Simplified pipeline demonstration
- Sample predictions
- Performance summary

### Jupyter Exploration
```bash
jupyter notebook
```
Opens browser for interactive data exploration.

## 📊 Expected Performance

After successful setup, you should see:
- **Training time**: ~30 seconds on modern hardware
- **Final RMSE**: ~$2,000 average prediction error
- **Memory usage**: ~200-500MB during execution

## 🤝 Support

If you encounter issues:
1. Check this troubleshooting guide
2. Ensure all requirements are met
3. Verify virtual environment is activated
4. Check the GitHub issues page

## ✅ Setup Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed successfully
- [ ] Core imports work without errors
- [ ] Dataset files are present
- [ ] Example script runs successfully
- [ ] Main pipeline executes without errors

---

**Ready to explore machine learning with car price prediction! 🚗🤖**
