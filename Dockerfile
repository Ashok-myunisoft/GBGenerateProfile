# Use official Python image
FROM python:3.11-slim

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory to /app (recommended for RunPod)
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install RunPod SDK
RUN pip install --no-cache-dir runpod openai

# Copy project files
COPY . .

# Start RunPod serverless handler
CMD ["python", "-u", "handler.py"]
