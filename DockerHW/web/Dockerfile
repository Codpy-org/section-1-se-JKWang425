# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /web

# Copy files into the container
COPY ./web

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "main.py"]