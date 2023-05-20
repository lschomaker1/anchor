# Use an official Python runtime as the base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
    

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the project code to the working directory
COPY . .

# Expose the port on which your Django application will run (default is 8000)
EXPOSE 8000

# Run the Django application using Gunicorn
CMD ["gunicorn", "anchor.wsgi:application", "--bind", "0.0.0.0:8000"]
