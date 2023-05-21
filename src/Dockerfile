# Use a base image with Python and dependencies installed
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the desired port for incoming connections
EXPOSE 5000

# Set the command to start the Flask application
CMD ["python", "app.py"]
