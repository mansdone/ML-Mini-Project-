"""
Setup script for QuickDraw Image Classification
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="quickdraw-classification",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="QuickDraw Image Classification using CNN and Classical ML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/quickdraw-classification",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
            "isort>=5.0",
        ],
    },
    keywords="machine-learning deep-learning cnn svm classification quickdraw image-recognition",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/quickdraw-classification/issues",
        "Source": "https://github.com/yourusername/quickdraw-classification",
        "Documentation": "https://github.com/yourusername/quickdraw-classification#readme",
    },
)

