# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8004 available to the world outside this container
EXPOSE 8004

# Define environment variable
ENV NAME World

# Run order_processing.py when the container launches
CMD ["python", "order_processing.py"]
