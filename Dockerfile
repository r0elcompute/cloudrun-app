# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency list first (layer caching optimization)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app.py .

# Expose the port Cloud Run expects
EXPOSE 8080

# Run with gunicorn (production-grade server, NOT flask dev server)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "app:app"]
