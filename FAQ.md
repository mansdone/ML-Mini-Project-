# Frequently Asked Questions (FAQ)

## General Questions

### Q: What is this project about?
**A:** This project implements and compares multiple machine learning approaches (CNN, SVM, Logistic Regression) for classifying hand-drawn sketches from Google's QuickDraw dataset.

### Q: What drawing categories are supported?
**A:** Currently 10 categories: Cat, Dog, Car, Tree, Sun, Bicycle, House, Star, Cloud, and Apple.

### Q: Can I add more categories?
**A:** Yes! You can easily add more categories by modifying the `class_names` list in the notebook and downloading the corresponding `.npy` files.

## Installation & Setup

### Q: What Python version do I need?
**A:** Python 3.8 or higher is required. Python 3.9-3.11 are recommended for best compatibility.

### Q: Do I need a GPU to run this project?
**A:** No, but it's recommended. The CNN training will be faster with a GPU. You can use Google Colab for free GPU access.

### Q: How long does training take?
**A:** 
- CNN (20 epochs): ~25-30 minutes on GPU, ~1-2 hours on CPU
- SVM: ~30 seconds (on 10k samples)
- Logistic Regression: ~1-2 minutes

### Q: I'm getting TensorFlow installation errors. What should I do?
**A:** Make sure you're using a compatible Python version (3.8-3.11). Try installing TensorFlow separately:
```bash
pip install tensorflow==2.10.0
```

### Q: The dataset download is very slow. Any alternatives?
**A:** The notebook automatically downloads from Google Cloud Storage. If it's slow, you can manually download `.npy` files from [QuickDraw Dataset](https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/numpy_bitmap).

## Usage Questions

### Q: How do I use the interactive drawing canvas?
**A:** 
1. Run all cells in the notebook
2. Scroll to the interactive canvas section
3. Draw using your mouse
4. Click "Predict Drawing" to see results

### Q: The drawing canvas isn't working. Why?
**A:** The canvas requires `ipycanvas` and `ipywidgets`. Make sure they're installed:
```bash
pip install ipycanvas ipywidgets
```
Then restart the Jupyter kernel.

### Q: Can I use my own images instead of the QuickDraw dataset?
**A:** Yes! You'll need to:
1. Resize images to 28×28 pixels
2. Convert to grayscale
3. Normalize pixel values to [0, 1]
4. Reshape to the correct input format

### Q: How do I save the trained model?
**A:** Add this code after training:
```python
cnn_v2.save('my_model.h5')
```
To load it later:
```python
model = keras.models.load_model('my_model.h5')
```

## Performance Questions

### Q: Why is CNN V2 the best model?
**A:** CNN V2 has the optimal balance between complexity and performance. Removing the second convolutional layer reduces overfitting while maintaining high accuracy.

### Q: Can I improve the accuracy?
**A:** Yes! Try:
- Data augmentation (rotation, zoom, shift)
- Training for more epochs
- Increasing the dataset size
- Hyperparameter tuning
- Ensemble methods

### Q: Why are Cat and Dog often confused?
**A:** Hand-drawn cats and dogs can look very similar at 28×28 resolution. This is a common challenge in sketch recognition.

### Q: What's the theoretical maximum accuracy for this dataset?
**A:** The original QuickDraw paper reports ~75-90% accuracy on 345 classes. For 10 classes, >95% is achievable with advanced techniques.

## Troubleshooting

### Q: I'm getting "Out of Memory" errors during training
**A:** Try:
- Reduce batch size (e.g., from 128 to 64)
- Use fewer samples per class
- Close other applications
- Use Google Colab with GPU

### Q: The confusion matrix isn't displaying correctly
**A:** Make sure you have `seaborn` and `matplotlib` installed:
```bash
pip install seaborn matplotlib
```

### Q: I'm getting convergence warnings for Logistic Regression
**A:** This is normal. The model still works. To fix:
- Increase `max_iter` parameter
- Scale the data (already done in the notebook)

### Q: The model predictions seem random
**A:** Check that:
- The model is properly trained
- Input data is normalized correctly
- The image is inverted (black on white vs white on black)

## Deployment Questions

### Q: Can I deploy this model to a website?
**A:** Yes! You can use Flask, FastAPI, or Streamlit to create a web interface. Convert the model to TensorFlow.js for client-side deployment.

### Q: How can I use this on mobile?
**A:** Convert the model to TensorFlow Lite (.tflite) for Android/iOS deployment.

### Q: Can I convert this to ONNX format?
**A:** Yes, use `tf2onnx`:
```bash
python -m tf2onnx.convert --saved-model saved_model_dir --output model.onnx
```

## Contributing

### Q: How can I contribute to this project?
**A:** See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines. All contributions are welcome!

### Q: I found a bug. Where do I report it?
**A:** Open an issue on GitHub with:
- Clear description of the bug
- Steps to reproduce
- Your environment details
- Screenshots if applicable

### Q: Can I use this project for my research/thesis?
**A:** Absolutely! This project is MIT licensed. Please cite it using the [CITATION.cff](CITATION.cff) file.

## Data & Privacy

### Q: Is the QuickDraw dataset free to use?
**A:** Yes! It's released by Google under a Creative Commons license.

### Q: Does this project collect any user data?
**A:** No. Everything runs locally. No data is sent to external servers.

### Q: Can I use this commercially?
**A:** Yes, under the MIT License. See [LICENSE](LICENSE) for details.

## Still have questions?

Feel free to:
- Open an issue on GitHub
- Check the [README.md](README.md) for more details
- Review the code comments in the notebook

---

**Last Updated:** October 14, 2025

