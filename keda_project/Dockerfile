# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY rabbitmq_producer.py .

# Install the pika library (if any additional dependencies are needed, add them here)
RUN pip install pika

# Command to run the Python script when the container starts
CMD ["python", "rabbitmq_producer.py"]
