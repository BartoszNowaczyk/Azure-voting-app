Opis projektu

Azure Voting App to prosta aplikacja do głosowania, która wykorzystuje Redis jako bazę danych oraz działa w kontenerach Docker Compose. Aplikacja składa się z dwóch głównych komponentów:

Frontend – aplikacja webowa do głosowania,

Backend (Redis) – przechowuje wyniki głosowania.

1️. Wymagania wstępne

Aby uruchomić aplikację, upewnij się, że masz zainstalowane:

Docker + Docker Compose → Pobierz tutaj

2️. Klonowanie repozytorium

 git clone https://github.com/BartoszNowaczyk/Azure-voting-app.git
 cd Azure-voting-app

3️. Instalacja zależności (opcjonalnie, jeśli uruchamiasz lokalnie)

pip install -r requirements.txt

4️. Uruchomienie aplikacji w Dockerze

Aby uruchomić aplikację wraz z Redisem w kontenerach Docker, użyj komendy:

docker-compose up

Jeśli chcesz ponownie zbudować obrazy Dockera, wykonaj:

docker-compose build

5️. Otwórz aplikację w przeglądarce

Po uruchomieniu aplikacja będzie dostępna pod adresem:
http://localhost:5000
