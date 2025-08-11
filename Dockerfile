# Use official Python 3.12 slim image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements first and install them
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install gunicorn

# Copy the rest of the project
COPY . .

# Vercel expects app on port 8080
EXPOSE 8080
ENV PORT=8080
ENV HOST=0.0.0.0

# Start Gunicorn, pointing to the Flask app inside index.py
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "index:app"]

