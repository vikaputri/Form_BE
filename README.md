# Backend
How To Install in Local
1. Clone Project :
```
git clone https://github.com/vikaputri/Form_BE.git
```
2. Change Project Directory :
```
cd Form_BE
```
4. Create Env
```
python -m venv <virtual-environment-name>
```
5. Activate Env
```
env/Scripts/activate
```
6. Install Requirement :
```
pip install -r requirements.txt
```
7. Migrate Database
```
python manage.py makemigrations
python manage.py migrate
```
9. Createsuperuser:
```
python manage.py createsuperuser
```
8. Run
```
python manage.py runserver
```