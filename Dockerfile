# Use official Python 3.12 image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Vercel expects the app to listen on port 8080
EXPOSE 8080

# Set environment variable for Flask
ENV PORT=8080
ENV HOST=0.0.0.0

# Command to run your app (replace index.py with your main file)
CMD ["python", "index.py"]
