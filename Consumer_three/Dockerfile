# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8003 available to the world outside this container
EXPOSE 8003

# Define environment variable
ENV NAME World

# Run stock_management.py when the container launches
CMD ["python", "stock_management.py"]
