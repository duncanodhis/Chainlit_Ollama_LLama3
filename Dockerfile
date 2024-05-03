# Use a lightweight base image with Python
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point to run the Chainlit application
ENTRYPOINT ["chainlit", "run", "app.py"]
