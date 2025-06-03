# SOURCEAdd commentMore actions
# Bankovní aplikace (Django)

Tato webová aplikace simuluje základní funkce banky – registrace uživatele, přihlášení, zůstatek, převody mezi účty apod. Aplikace je postavena na frameworku **Django** v jazyce **Python**.

## Použité technologie
- Python 3.10+
- SQLite (výchozí databáze)
- Bootstrap
- ...

## Lokální spuštění

### 1. Stažení projektu
Nejprve si stáhněte.

2. Vytvoření virtuálního prostředí
Doporučeno pro správu závislostí:

python -m venv venv
# Aktivace:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

3. Instalace závislostí
pip install -r requirements.txt
Pokud nemáš soubor requirements.txt, vytvoř ho pomocí:
pip freeze > requirements.txt

4. Migrace databáze
python manage.py migrate

5. Vytvoření superuživatele (volitelné – pro admin rozhraní)
python manage.py createsuperuser

6. Spuštění serveru
python manage.py runserver

Aplikace poběží na adrese:
👉 http://127.0.0.1:8000

Poznámky
Pokud používáš .env pro tajné klíče (např. SECRET_KEY), přilož také soubor .env.example.
V settings.py musí být DEBUG = True a ALLOWED_HOSTS = [], aby aplikace šla lokálně spustit.
