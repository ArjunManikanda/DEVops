# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .


RUN pip install fastapi
RUN pip install uvicorn
RUN pip install starlette

# Expose the port that the app will run on
EXPOSE 8000

# Run the command to start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

