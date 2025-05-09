# Pulls the official base image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy and install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project in the work directory
COPY . /app/

# COPY the start script
COPY start.sh /app/start.sh

# Create static and staticfiles directories if it doesn't exist
RUN mkdir -p /app/static /app/staticfiles

# Ensure start.sh is executable
RUN chmod +x /app/start.sh

# Expose the port on which the application will run
EXPOSE 8000

# Run the app using the custom start script
CMD ["./start.sh"]
