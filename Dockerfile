# Dockerfile for QuickDraw Classification Project

FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY ML_Project.ipynb .
COPY README.md .

# Create directories
RUN mkdir -p quickdraw_data models results

# Expose Jupyter port
EXPOSE 8888

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV JUPYTER_ENABLE_LAB=yes

# Run Jupyter notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]

# Usage:
# Build: docker build -t quickdraw-classification .
# Run: docker run -p 8888:8888 -v $(pwd)/quickdraw_data:/app/quickdraw_data quickdraw-classification
# Access: http://localhost:8888

