#!/bin/bash
set -e

echo "Starting Vercel build with Python 3.13..."

# Force Python 3.13
export PYTHON_VERSION=3.13
export PYTHON_RUNTIME=python3.13

# Check Python version
python3.13 --version

# Install dependencies with Python 3.13
python3.13 -m pip install --no-cache-dir --disable-pip-version-check --target . --upgrade -r requirements.txt

# Clean up to reduce size
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
find . -type f -name "*.pyo" -delete 2>/dev/null || true

echo "Build completed successfully!"
