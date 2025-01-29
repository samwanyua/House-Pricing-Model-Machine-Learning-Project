# Use Python 3.9 (or the version you prefer)
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application code into the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 (Azure will map $PORT to the container port)
EXPOSE 5000

CMD gunicorn --workers=2 --bind 0.0.0.0:$PORT app:app
