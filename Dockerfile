#Python basic image
FROM python:3.12-slim

# Work directory
WORKDIR /app

# Files copy
COPY . /app

# Set requirements
RUN pip install --no-cache-dir -r requirements.txt

# Set port
EXPOSE 8000

# Start with Gunicorn
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:8000", "wsgi:app"]

