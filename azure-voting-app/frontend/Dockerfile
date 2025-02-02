# Dockerfile dla frontend
FROM python:3.9-slim

WORKDIR /app

# Skopiuj plik z wymaganiami do kontenera
COPY requirements.txt requirements.txt

# Zainstaluj wymagane biblioteki
RUN pip install -r requirements.txt

# Skopiuj pozostałe pliki aplikacji
COPY . .

# Ustaw domyślną komendę startową
CMD ["python", "app.py"]
