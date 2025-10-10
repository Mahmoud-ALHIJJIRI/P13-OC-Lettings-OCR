# --------------------------------------------------------------------------
# Stage 1: Build Stage (Handles large downloads and static files)
# --------------------------------------------------------------------------
FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Ensure the settings module is set in the build environment
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Set working directory inside the container
WORKDIR /app

# Copy and install dependencies first (leverages Docker caching)
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# NOTE: Removed --target=/install here as it interferes with later commands

# --- CRITICAL CHANGE START ---
# Copy the entire Django project code before running manage.py
COPY . /app/

# In Django, static files must be collected before deployment
# If this fails, check for Python syntax errors in any settings/urls file
# or a missing app/module referenced in INSTALLED_APPS.
RUN python manage.py collectstatic --noinput

# --------------------------------------------------------------------------
# Stage 2: Final Production Image (Minimal Runtime)
# --------------------------------------------------------------------------
# Use the same base image for consistency and environment compatibility
FROM python:3.11-slim

# Set environment variables for the application at runtime
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Set working directory and copy requirements for re-install
WORKDIR /app
COPY requirements.txt /app/

# CRITICAL FIX: Re-install dependencies in the final stage's environment.
# This ensures all executables (like gunicorn) are correctly placed in the $PATH.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code and collected static files from the builder stage
# /app now contains the source code AND the static files collected in Stage 1.
COPY --from=builder /app /app

# Expose the application port
EXPOSE 8000

# Set the command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi"]
