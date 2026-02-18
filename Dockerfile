# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /workspace

# Copy requirements first (better caching)
COPY requirements.txt .

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install RunPod serverless SDK (IMPORTANT)
RUN pip install --no-cache-dir runpod fastapi uvicorn gunicorn

# Copy application files
COPY . .

# Start handler
CMD ["python", "-u", "handler.py"]
