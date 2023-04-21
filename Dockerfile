# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

COPY . /app


RUN pip install --no-cache-dir -r data.txt

# Copy the current directory contents into the container at /app

# Expose the port that the app will run on
EXPOSE 80

# Run the command to start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

