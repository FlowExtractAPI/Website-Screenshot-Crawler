# Use the official Apify Python base image
FROM python:3.10-slim

# Set environment variables
ENV PIP_NO_CACHE_DIR=1
ENV PLAYWRIGHT_BROWSERS_PATH=/usr/local/share/playwright/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    wget \
    xvfb \
    libnss3 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libgbm-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright (optional if using Pyppeteer)
RUN pip install playwright && playwright install --with-deps

# Create a directory for the actor's files
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy all files from the current directory into the container
COPY . .


# Command to run the application
CMD ["python", "-m", "src"]
