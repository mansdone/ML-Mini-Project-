# 🚀 Quick Start Guide

Get up and running with QuickDraw Classification in under 5 minutes!

## Prerequisites Checklist

- [ ] Python 3.8+ installed
- [ ] pip package manager
- [ ] 2GB free disk space
- [ ] Internet connection (for dataset download)

## Installation (3 Steps)

### Step 1: Clone or Download

**Option A - Git Clone:**
```bash
git clone https://github.com/yourusername/quickdraw-classification.git
cd quickdraw-classification
```

**Option B - Download ZIP:**
1. Download the repository as ZIP
2. Extract to your preferred location
3. Open terminal/command prompt in that folder

### Step 2: Install Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### Step 3: Launch Jupyter Notebook

```bash
jupyter notebook ML_Project.ipynb
```

## Running on Google Colab (No Installation Required!)

1. Go to [Google Colab](https://colab.research.google.com/)
2. Click `File` → `Upload notebook`
3. Upload `ML_Project.ipynb`
4. Click `Runtime` → `Run all`
5. Wait ~30 minutes for complete execution

**Advantages of Colab:**
- ✅ Free GPU access
- ✅ No local setup needed
- ✅ Pre-installed libraries
- ✅ Easy sharing

## First Run Guide

### What to Expect

**Total Runtime:** ~30-40 minutes (with GPU) or ~2-3 hours (CPU only)

**Steps that will automatically happen:**
1. ⬇️ Download QuickDraw dataset (~200MB)
2. 📊 Load and preprocess 200,000 images
3. 🤖 Train Logistic Regression (~2 min)
4. 🤖 Train SVM with 4 kernels (~2 min)
5. 🧠 Train CNN model (~25-30 min)
6. 📈 Generate visualizations
7. 🎨 Launch interactive drawing canvas

### Cell-by-Cell Breakdown

| Cell # | What It Does | Time |
|--------|-------------|------|
| 0 | Install libraries & imports | 1 min |
| 1-2 | Download dataset (200MB) | 3-5 min |
| 3-5 | Prepare data | 1 min |
| 6 | Train Logistic Regression | 2 min |
| 7 | Train SVMs | 2 min |
| 8-9 | Define & train CNN | 25-30 min |
| 10-19 | Interactive tests & canvas | Instant |
| 20-21 | Confusion matrix | 1 min |

## Quick Commands Reference

### Create New Virtual Environment
```bash
python -m venv venv
```

### Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Launch Jupyter
```bash
jupyter notebook
```

### Save Model
```python
# Add this after training (Cell 9)
cnn_v2.save('models/quickdraw_model.h5')
```

### Load Saved Model
```python
from tensorflow import keras
model = keras.models.load_model('models/quickdraw_model.h5')
```

## Common First-Time Issues & Fixes

### Issue 1: TensorFlow Installation Error
```bash
# Try installing specific version
pip install tensorflow==2.10.0
```

### Issue 2: Jupyter Not Found
```bash
# Install Jupyter
pip install jupyter notebook
```

### Issue 3: Canvas Not Working
```bash
# Reinstall canvas widgets
pip install --upgrade ipycanvas ipywidgets

# Then restart Jupyter kernel
# Kernel → Restart
```

### Issue 4: Out of Memory
```python
# In Cell 2, reduce samples:
samples_per_class = 10000  # Instead of 20000
```

### Issue 5: Slow Training
**Solution:** Use Google Colab with GPU (free!)

## Testing Your Installation

Run this quick test to verify everything works:

```python
# In a new Jupyter cell or Python script
import tensorflow as tf
import sklearn
import numpy as np
import matplotlib.pyplot as plt

print("✅ TensorFlow:", tf.__version__)
print("✅ NumPy:", np.__version__)
print("✅ scikit-learn:", sklearn.__version__)
print("\n🎉 All dependencies installed successfully!")
```

## Next Steps

After successful installation:

1. **Run All Cells** - Let it train completely
2. **Try the Drawing Canvas** - Draw your own sketches
3. **Explore Results** - Check accuracy, confusion matrix
4. **Experiment** - Modify hyperparameters, add classes
5. **Deploy** - Create a web app or mobile app

## Useful Tips

💡 **Tip 1:** Save your model after training to avoid retraining
```python
cnn_v2.save('my_model.h5')
```

💡 **Tip 2:** Use fewer samples for quick testing
```python
samples_per_class = 5000  # Instead of 20000
```

💡 **Tip 3:** Enable GPU in Colab
- Runtime → Change runtime type → GPU

💡 **Tip 4:** Monitor training progress
- Watch the loss/accuracy values in real-time
- Training graphs are generated automatically

💡 **Tip 5:** Clear output to save space
- Cell → All Output → Clear

## Getting Help

- 📖 Read the full [README.md](README.md)
- ❓ Check [FAQ.md](FAQ.md)
- 🐛 Report issues on GitHub
- 💬 Join discussions on GitHub

## Verification Checklist

After running the notebook, verify:

- [ ] Dataset downloaded (200,000 samples)
- [ ] Logistic Regression accuracy ~78%
- [ ] SVM Poly accuracy ~84%
- [ ] CNN accuracy ~93%
- [ ] Confusion matrix displayed
- [ ] Drawing canvas works
- [ ] Can predict your own drawings

## Estimated Resource Requirements

| Resource | Minimum | Recommended |
|----------|---------|-------------|
| RAM | 4 GB | 8 GB+ |
| Disk Space | 2 GB | 5 GB |
| CPU | 2 cores | 4+ cores |
| GPU | None | Any CUDA GPU |
| Internet | 10 Mbps | 50+ Mbps |

---

## Ready to Start? 🚀

```bash
# One-command setup (after cloning)
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && jupyter notebook
```

**Happy Classifying! 🎨🤖**

