# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-14

### Added
- Initial release of QuickDraw Classification project
- Implemented 4 CNN architectures (V1, V2, V3, V4)
- Implemented SVM with multiple kernels (Linear, RBF, Polynomial, Sigmoid)
- Implemented Logistic Regression classifier
- 10 drawing categories from QuickDraw dataset
- Comprehensive testing suite (6 different tests)
- Interactive drawing canvas for real-time predictions
- Detailed visualizations:
  - Training history plots
  - Confusion matrices
  - Per-class accuracy charts
  - Confidence distribution graphs
  - Misclassification analysis
- Robustness testing with noisy images
- Complete documentation (README, CONTRIBUTING, LICENSE)

### Features
- Train/Validation/Test split (80/10/10)
- 200,000 total samples (20,000 per class)
- Best model (CNN V2) achieves ~93% test accuracy
- Automatic dataset downloading from Google Cloud Storage
- Support for both normalized and binarized data preprocessing

### Documentation
- Comprehensive README with installation and usage instructions
- Contributing guidelines
- MIT License
- Citation file for academic use
- Requirements file with all dependencies

## [Unreleased]

### Planned
- Data augmentation techniques
- Transfer learning with pre-trained models
- Web deployment (Flask/FastAPI)
- Model interpretability (Grad-CAM)
- Additional drawing categories
- Mobile app version
- Docker containerization
- CI/CD pipeline setup

