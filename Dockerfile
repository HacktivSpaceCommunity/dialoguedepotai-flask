# FROM python:3.11
# LABEL maintainer="company@stacknyu.com"
# COPY . /app
# WORKDIR /app
# RUN pip install -r requirements.txt
# EXPOSE 5000
# ENTRYPOINT ["python"]
# CMD ["app.py"]


# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 8000 for Gunicorn to listen on
EXPOSE 8000

# Define environment variables
ENV FLASK_APP=app
ENV FLASK_ENV=production

# Start Gunicorn to serve the Flask app
CMD ["gunicorn", "--workers=1", "--bind=0.0.0.0:8000", "app:app"]
