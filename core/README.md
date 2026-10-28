## Obsidian Movie AutoNotes

### Description
Obsidian Movie AutoNotes is a Python-based application that automates the process of collecting, organizing, and analyzing movie data.

The program allows users to provide a list of movie titles, retrieves detailed metadata for each film, and generates structured Markdown notes designed for integration with Obsidian. 
In addition to note creation, the system stores all collected data in a structured CSV format, enabling further analysis and visualization.

(Personal Note)
I started working on this project because, I was spending a lot of my free time copying and pasting details from movies for my own personal Obsidian vault, and eventually realised that there was a much simpler way to get the information I needed, and also a much simpler way to generate notes.
Thanks, Python!

### Requirements
If you intend to use this program, then you need to have [Obsidian](https://obsidian.md/) installed, with the [Colored Text](https://github.com/erincayaz/obsidian-colored-text) plugin that can be found in the Community Plugins tab in Obsidian.

If you want to use this for cards, like I do, I recommend checking out this [video](https://youtu.be/yaqpVGekrro) on Youtube.

You also need to have python installed and you need to install all of the libraries that are listed in the requirements.txt file as well. Install from the requirements.txt file like so: python -m pip install -r requirements.txt  

Also, if you run into a 403 error when running main.py, try using this:  pip install --upgrade imdbinfo

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

*Text file with list of movies*

<img width="654" height="528" alt="UsageExample1" src="https://github.com/user-attachments/assets/51ffd39b-4a79-4210-851b-88e2871cb77e" />


*Terminal with results after running program*
<img width="984" height="489" alt="UsageExample3" src="https://github.com/user-attachments/assets/0c2d49c8-c735-40a7-9572-261505e6d582" />


*Histogram with top 10 most occuring directors*
<img width="1006" height="667" alt="UsageExample2" src="https://github.com/user-attachments/assets/f7e28a60-83b9-485c-919e-164b33a2e8a0" />


*Histogram with top 25 most occuring actors*
<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/417577ce-761c-4182-aed2-fc96b9f6106a" />


*Movie Base file with all movie cards that were created with the program*
<img width="1910" height="1034" alt="Screenshot 2026-02-20 214241" src="https://github.com/user-attachments/assets/d7d96a4d-89b7-41d7-a378-803fba5a68e6" />


*Note of Movie with all of the generated information*
<img width="1572" height="1039" alt="Screenshot 2026-02-20 214334" src="https://github.com/user-attachments/assets/a6df14ba-392b-45b7-a28d-8daba6bab733" />


## TODO
 - Add import option that allows the user to import txt file containing list of user movies
 - Add the other charts
 - Add small selection box on every added movie, so the user can have the option of mass deleting movies, or mass exporting.

## Team

Just me, Keenon!
