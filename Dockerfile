# Stage 1: Build Stage
# Use a Python base image to handle dependency installation and static file collection.
FROM python:3.11-slim AS builder

# Set environment variables for the container
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies first (leverages Docker caching)
# NOTE: Ensure Gunicorn is listed in requirements.txt
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire Django project code
COPY . /app/

# In Django, static files must be collected before deployment
RUN python manage.py collectstatic --noinput

# -----------------------------------------------------------------------------

# Stage 2: Final Production Image
# Use a highly minimal base image for the final running application
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy only the necessary files from the builder stage
# This includes the collected static files and the installed dependencies
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app /app

# Expose the application port (Render defaults to 8000 for Django)
EXPOSE 8000

# Set the command to run the application using Gunicorn (a production WSGI server)
# CORRECTION: Using your actual WSGI path (oc_lettings_site.wsgi)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi"]
