# ML-Mini-Project-
A Convolutional Neural Network (CNN) based classifier that recognizes hand-drawn sketches from multiple categories using the Quick, Draw! dataset. Includes pre-processing, training visualization, model evaluation, and serialization for easy inference on new doodles





QuickDraw Sketch Classification: A Comparison of Deep Learning and Traditional ML Models
This repository contains the code for classifying Google QuickDraw sketches using various machine learning and deep learning techniques. The project compares the performance, training time, and architectural complexity of models like Logistic Regression, Support Vector Machines (SVM), Custom Convolutional Neural Networks (CNNs), and several Transfer Learning architectures (MobileNet, VGG16, ResNet50, InceptionV3).

Project Goal
The primary objective is to replicate and extend classic findings in sketch recognition using a high-volume dataset of user-drawn images, specifically focusing on how deep learning (CNNs and Transfer Learning) stacks up against traditional methods.

Getting Started
Prerequisites
To run the notebook locally or in a Colab environment, you will need the following Python libraries:

pip install tensorflow numpy scikit-learn matplotlib seaborn pandas quickdraw

How to Run
The entire project is contained within the proj11.ipynb Jupyter Notebook.

Google Colab (Recommended): The easiest way to run the project is by opening the proj11.ipynb file directly in Google Colab. Colab already provides the necessary GPU/TPU resources and a pre-configured environment.

Jupyter/Local: You can download the notebook and run it locally in a Jupyter environment after installing the dependencies listed above.

The notebook handles all data downloading (QuickDraw bitmap files) and preprocessing automatically.

Project Structure
The project notebook walks through the following stages:

Data Loading and Preprocessing: Downloads 20,000 samples for each of the 10 chosen classes, converts them to 28x28 pixel arrays, normalizes the data, and splits it into training, validation, and test sets.

Classical ML Benchmarks: Trains and evaluates Logistic Regression and Support Vector Machines (SVM) on the flattened, non-binarized and binarized 784-dimensional feature vectors.

Custom CNN Analysis: Implements and compares four custom CNN architectures based on variations of convolutional and pooling layers to find an optimal low-complexity model.

Transfer Learning Preparation: Resizes the 28x28 grayscale images to 75x75 pixels and converts them to 3-channel RGB format to be compatible with pre-trained models from the ImageNet challenge.

Transfer Learning Evaluation: Evaluates four popular pre-trained models (MobileNet, VGG16, ResNet50, and InceptionV3) by freezing their base layers and training a new dense classification head.

Note: The notebook may take a significant amount of time to run, especially the classical ML models (Logistic Regression, SVM) and the larger Transfer Learning models (VGG16, ResNet50, InceptionV3).
