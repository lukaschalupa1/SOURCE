# Bankovní aplikace (Django)

Tato webová aplikace simuluje základní funkce banky – registrace uživatele, přihlášení, zobrazení zůstatku, převody mezi účty apod. Aplikace je postavena na frameworku **Django** v jazyce **Python**.

---

## 🛠 Použité technologie
- Python 3.10+
- Django 4.x
- SQLite (výchozí databáze)
- Bootstrap 5
- HTML, CSS

---

## 🖥️ Lokální spuštění

### 1. Stažení projektu
Stáhněte nebo naklonujte repozitář:

```bash
git clone https://github.com/uzivatel/bankovni-aplikace.git
cd bankovni-aplikace
2. Vytvoření a aktivace virtuálního prostředí
bash
Zkopírovat
Upravit
python -m venv venv
Aktivace:

Windows:

bash
Zkopírovat
Upravit
venv\Scripts\activate
macOS/Linux:

bash
Zkopírovat
Upravit
source venv/bin/activate
3. Instalace závislostí
bash
Zkopírovat
Upravit
pip install -r requirements.txt
Nemáš-li soubor requirements.txt, vytvoř ho pomocí:

bash
Zkopírovat
Upravit
pip freeze > requirements.txt
4. Migrace databáze
bash
Zkopírovat
Upravit
python manage.py migrate
5. (Volitelně) Vytvoření superuživatele
bash
Zkopírovat
Upravit
python manage.py createsuperuser
6. Spuštění vývojového serveru
bash
Zkopírovat
Upravit
python manage.py runserver
Aplikace poběží na adrese:
http://127.0.0.1:8000

📝 Poznámky
Pokud používáš .env pro tajné klíče (např. SECRET_KEY), přilož soubor .env.example.

V souboru settings.py nastav:

python
Zkopírovat
Upravit
DEBUG = True
ALLOWED_HOSTS = []
