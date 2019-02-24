# skurcz.to
Recruitment task

Przygotować aplikację skracającą URLe. Aplikacja ma za zadanie:
• pobierać od (anonimowego) użytkownika URL
• generować skrócony URL w formie `<twoja domena>/<skrót>`
• podawać go użytkownikowi
• w interfejsie admina ma być widoczna lista wszystkich URLi wraz z ich
wartością
• po przejściu do `<twoja domena>/<skrót>` użytkownik ma być
przekierowany na pierwotny adres podany do skrócenia.

# Installation and launching locally

- create virtual environment with python (>=3.6) and install dependencies from requirements.txt
- provide environment variables:
	- `SECRET_KEY`
- make migrations with `python manage.py makemigrations`
- migrate models to db with `python manage.py migrate`
- runserver with `python manage.py runserver`
- to launch tests run `python manage.py test`
- to launch functional tests run `python functional_tests.py`


# Live demo

[http://skurcz.pythonanywhere.com](http://skurcz.pythonanywhere.com/)
