FROM python:3.11-slim

WORKDIR /app

# Copier requirements.txt depuis API/backend
COPY API/backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le backend Django
COPY API/backend/ .

CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
