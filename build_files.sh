#!/bin/bash

# Clean up any existing build artifacts
rm -rf __pycache__/
rm -rf *.pyc

# Install dependencies locally to test
pip install -r requirements.txt

# Test the application
python -c "import app; print('App imported successfully')"

echo "Build preparation completed successfully!"
