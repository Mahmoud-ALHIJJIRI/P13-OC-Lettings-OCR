# --------------------------------------------------------------------------
# Stage 1: Build Stage (Handles large downloads and static files)
# --------------------------------------------------------------------------
FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory inside the container
WORKDIR /app

# Copy and install dependencies in the builder stage
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --target=/install

# Copy the entire Django project code
COPY . /app/

# In Django, static files must be collected before deployment
RUN python manage.py collectstatic --noinput

# --------------------------------------------------------------------------
# Stage 2: Final Production Image (Minimal Runtime)
# --------------------------------------------------------------------------
# Use the same base image for consistency and environment compatibility
FROM python:3.11-slim

# Copy the requirements file needed for the Gunicorn installation path
COPY requirements.txt /app/
WORKDIR /app

# *** CRITICAL FIX: Re-install dependencies in the final stage's environment. ***
# This guarantees that the Gunicorn executable is placed in the final image's $PATH.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code and collected static files from the builder stage
COPY --from=builder /app /app

# Expose the application port
EXPOSE 8000

# Set the command to run the application using Gunicorn
# Ensure gunicorn is in requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi"]
