# QuickDraw Image Classification using CNN and Classical ML

A comprehensive machine learning project that classifies hand-drawn sketches from Google's QuickDraw dataset using both deep learning (CNN) and classical machine learning approaches (SVM, Logistic Regression).

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Models Implemented](#models-implemented)
- [Results](#results)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 🎯 Overview

This project implements and compares multiple machine learning approaches for classifying hand-drawn sketches from the QuickDraw dataset. The dataset contains 28×28 grayscale images across 10 different categories. We explore both traditional machine learning algorithms and modern deep learning architectures to achieve high classification accuracy.

## ✨ Features

- **Multiple Model Implementations**:
  - Convolutional Neural Networks (CNN) with 4 different architectures
  - Support Vector Machines (SVM) with multiple kernels
  - Logistic Regression
  
- **Comprehensive Testing Suite**:
  - Random test sample predictions
  - Per-class accuracy analysis
  - Confidence distribution analysis
  - Common misclassification patterns
  - Model robustness testing (noise resistance)
  
- **Interactive Drawing Canvas**:
  - Real-time sketch recognition
  - Draw your own sketches and get predictions
  - Visual confidence scores

- **Detailed Visualizations**:
  - Training history plots
  - Confusion matrices
  - Per-class performance charts
  - Confidence distribution graphs

## 📊 Dataset

The project uses Google's **QuickDraw Dataset**, which contains millions of hand-drawn sketches across 345 categories. For this project, we focus on 10 classes:

- 🐱 Cat
- 🐕 Dog
- 🚗 Car
- 🌳 Tree
- ☀️ Sun
- 🚲 Bicycle
- 🏠 House
- ⭐ Star
- ☁️ Cloud
- 🍎 Apple

**Dataset Statistics**:
- **Samples per class**: 20,000
- **Total samples**: 200,000
- **Image size**: 28×28 pixels (grayscale)
- **Train/Val/Test split**: 80/10/10

## 🤖 Models Implemented

### 1. Convolutional Neural Networks (CNN)

We implemented and compared 4 CNN architectures:

#### **CNN V1** - Full Architecture
```
Conv2D(32) → MaxPool → Conv2D(64) → MaxPool → Dense(128) → Softmax
```

#### **CNN V2** - Simplified (Best Performance) ⭐
```
Conv2D(32) → MaxPool → Dense(128) → Softmax
```

#### **CNN V3** - Single MaxPool
```
Conv2D(32) → MaxPool → Conv2D(64) → Dense(128) → Softmax
```

#### **CNN V4** - Reduced Dense Units
```
Conv2D(32) → MaxPool → Conv2D(64) → MaxPool → Dense(64) → Softmax
```

### 2. Support Vector Machine (SVM)

Tested with multiple kernels:
- Linear Kernel
- RBF Kernel
- Polynomial Kernel
- Sigmoid Kernel

### 3. Logistic Regression

- Solver: L-BFGS
- Multi-class: Multinomial
- Max iterations: 100

## 📈 Results

### Model Performance Comparison

| Model | Test Accuracy | Training Time |
|-------|--------------|---------------|
| **CNN V2** | **~93%** | ~1600s (20 epochs) |
| SVM (Poly Kernel) | 84.10% | 32.74s |
| SVM (RBF Kernel) | 83.75% | 26.49s |
| Logistic Regression | 77.88% | 97.93s |
| SVM (Linear) | 69.08% | 26.42s |
| SVM (Sigmoid) | 69.19% | 23.25s |

### Per-Class Performance (CNN V2)

The CNN V2 model achieves excellent accuracy across all classes, with most categories achieving >90% accuracy.

**Best performing classes**: Star, House, Sun
**Challenging classes**: Cat vs Dog confusion

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/quickdraw-classification.git
cd quickdraw-classification
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Running the Complete Pipeline

Open the Jupyter notebook:
```bash
jupyter notebook ML_Project.ipynb
```

Or use Google Colab for free GPU access:
1. Upload `ML_Project.ipynb` to Google Colab
2. Run all cells sequentially

### Training Individual Models

**Train CNN:**
```python
# The notebook automatically trains CNN V2
# Results are displayed with training history plots
```

**Train Classical ML Models:**
```python
# Logistic Regression and SVM models are trained
# on a subset for faster computation
```

### Using the Interactive Drawing Canvas

The notebook includes an interactive canvas where you can:
1. Draw a sketch using your mouse
2. Click "Predict Drawing" to see the model's prediction
3. View confidence scores for all classes

### Testing and Evaluation

The project includes 6 comprehensive tests:
1. **Random Test Samples** - Verify predictions on random samples
2. **Per-Class Accuracy** - Analyze performance for each category
3. **Confidence Distribution** - Understand model certainty
4. **Misclassification Patterns** - Identify common errors
5. **Detailed Class Examples** - Deep dive into each category
6. **Robustness Test** - Test with noisy images

## 📁 Project Structure

```
quickdraw-classification/
│
├── ML_Project.ipynb          # Main Jupyter notebook
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
├── .gitignore               # Git ignore rules
│
├── quickdraw_data/          # Dataset directory (auto-created)
│   ├── cat.npy
│   ├── dog.npy
│   └── ...
│
├── models/                  # Saved models (optional)
│   └── cnn_v2_best.h5
│
└── results/                 # Results and visualizations (optional)
    ├── confusion_matrix.png
    └── training_history.png
```

## 🛠️ Technologies Used

**Deep Learning & Machine Learning:**
- TensorFlow 2.x
- Keras
- scikit-learn

**Data Processing & Visualization:**
- NumPy
- Pandas
- Matplotlib
- Seaborn
- OpenCV

**Interactive Components:**
- ipycanvas
- ipywidgets

**Dataset:**
- QuickDraw library

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contribution:
- Add more drawing categories
- Implement data augmentation
- Try transfer learning approaches
- Optimize model architectures
- Add model deployment (Flask/FastAPI)
- Create a web interface

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google QuickDraw Dataset**: [https://quickdraw.withgoogle.com/data](https://quickdraw.withgoogle.com/data)
- **TensorFlow/Keras** for deep learning framework
- **scikit-learn** for classical ML algorithms
- Inspired by research on sketch recognition and classification

## 📧 Team 

 Md.Jawwaad Sheriff (PES1UG23CS366)
 
 Lakshya Mehta (PES1UG23CS324)



---

⭐ If you found this project helpful, please consider giving it a star!

## 📚 References

1. Ha, D., & Eck, D. (2017). A Neural Representation of Sketch Drawings. arXiv preprint arXiv:1704.03477.
2. Google QuickDraw Dataset Documentation
3. TensorFlow Documentation
4. scikit-learn Documentation




