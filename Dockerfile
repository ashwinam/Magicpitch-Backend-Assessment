# Base image with minimal dependencies
FROM python:3.11-slim-buster

# Working directory for the application
WORKDIR /app

# Copy poetry configuration
COPY pyproject.toml /app/pyproject.toml

# Install dependencies using poetry
RUN pip install poetry
RUN poetry install

# Copy project code (excluding unnecessary files)
COPY . .

# Expose the port used by Django (default: 8000)
EXPOSE 8000

# Set the default command with poetry run
CMD [ "poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]
