# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy wheelhouse folder and install pre-built wheels
COPY wheelhouse /app/wheelhouse

# Install pre-built wheels first, then install the remaining dependencies from requirements.txt
RUN pip install --no-index --find-links=/app/wheelhouse torch==2.5.1 sentence_transformers==3.2.1 && \
    pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "routes.py"]
