# Start from an official, slim Python image
FROM python:3.11-slim-bookworm

# Install Docker CLI in container
RUN apt-get update && apt-get install -y --no-install-recommends docker.io

# Set working directory inside container
WORKDIR /app

# Copy reqs from host to container
COPY requirements.txt .

# Install Python dependencies in container
RUN pip install --no-cache-dir -r requirements.txt

# Copy main script from host to container
COPY cleaner.py .

# Specify command to run when container starts
ENTRYPOINT ["python", "./cleaner.py"]
