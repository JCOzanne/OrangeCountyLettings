# Pulls the official base image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Accept build-time variables
ARG SECRET_KEY
ARG DEBUG
ARG SENTRY_DSN

ENV SECRET_KEY=$SECRET_KEY
ENV DEBUG=$DEBUG
ENV SENTRY_DSN=$SENTRY_DSN

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy and install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project in the work directory
COPY . /app/

# Create static directory if it doesn't exist
RUN mkdir -p static staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port on which the application will run
EXPOSE 8000

# Running the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
