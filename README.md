# AutoNotes_Movie_Library
A Simple website for creating a custom "seen films" database and exporting markdown files.

### Description
(TODO)

### Requirements
(TODO)

### Usage
Currently this is what is needed to use the site, but all of this most likely won't be needed when the website is up and proper(at least for users)

Setup virtual environment: python -m venv venv

Activate virtual environment: venv\Scripts\activate

Install required packages for the program to work: pip install -r requirements.txt

Create own database(`migrate` builds all the tables from the migration files in `core/migrations/`. You only need to run it again when new migrations arrive): python manage.py migrate

Create own admin account: python manage.py createsuperuser

Run the webserver: python manage.py runserver

Generate code for .env file: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"



Copy .env.example to .env and put in your own secret key (command above).


## TODO
 - Add import option that allows the user to import txt file containing list of user movies
 - Add the other charts
 - Add small selection box on every added movie, so the user can have the option of mass deleting movies, or mass exporting.
 - Add loading screen with added favourite quotes.

## Team
Keenon