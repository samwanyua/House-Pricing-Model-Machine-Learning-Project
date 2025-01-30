# Use Python 3.9 (or preferred version)
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the app with Gunicorn (Optimized for production)
CMD ["gunicorn", "--workers=2", "--bind", "0.0.0.0:5000", "app:app"]
