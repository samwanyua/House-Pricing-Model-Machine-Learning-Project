# Use Python 3.9 (or the version you prefer)
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app/public

# Install dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the default port for the app 
ENV PORT 5000

# Expose port 5000
EXPOSE 5000

# Run the app with Gunicorn (adjust for your app)
CMD gunicorn --workers=2 --bind 0.0.0.0:$PORT app:app
