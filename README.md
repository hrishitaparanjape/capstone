# capstone
Dream Log website

## Introduction

The Dream Journal is a personal journaling application where users can record and manage their dreams privately. Each user has their own secure, private journal to log dreams with a title, description, emotional state, and date. The application includes features to view all recorded dreams, track a streak of journaling, and filter dreams by emotional state. It has a login and logout functionality, which ensures privacy and security.

## Distinctiveness and Complexity

The Dream Journal project stands out as a unique and distinctive application since it offers a private platform that can be used as an online journal. Users have their own personal journal that they can use to record their dreams every morning, or even throughout the day. One user cannot see another user's dream log, and everyone's journal reflects only their dreams.This project also includes features such as a filter, which filters dreams by emotional state, and a streak recorder. The website is designed in a user friendly way, and is easy to navigate.

Additionally, the user can see all of their dreams, but also has the option to go to the dashboard page on which they can filter their dreams by emotional state. This allows users to reflect on their entries, and look through dreams that gave them a similar feeling. This feature involved creating a dropdown menu from which the user can select an emotion, handling the form submissions, and displaying the correct results.

The user is also able to log a streak by just the press of a button, which encourages them to keep on using this journal. The streak button uses JavaScript to increase the steak number everytime the user remembers to log in their dream. This feature makes it hard for users to forget to add a new dream. In the case that a user does forget to log in their dream, the new dream form has a feature that allows the user to enter their own date, so they can enter their dream several days after as well.

## File Descriptions

### `models.py`
This file defines models that are used for this application. It includes a Dream model which stores information about each dream such as title, description, date, and emotional state a, as well as a foreign key to the User model to ensure each dream is associated with a specific user.

### `views.py`
This file contains the view functions that handle the logic for displaying pages and processing the user input. This includes views for the index page which displays all dreams, the dashboard page which filters dreams by emotional state, and the login, logout and register page which allows users to create an account and manages authentication.

### `urls.py`
This file defines the URL patterns for the application, routing URLs to their correct view functions.

### `templates/dream/layout.html`
The base HTML template that includes the navigation bar and styles. The other html templates extend this base template to ensure that the navigation bar is on every page, and the application looks consistent.

### `templates/dream/index.html`
This file is the template for displaying all dreams. It includes a list of all the dreams recorded by the user.

### `templates/dream/dashboard.html`
This file is the template for the dashboard page, where users can filter their dreams by emotional state and track their journaling streak.

### `templates/dream/new_dream.html`
This file is the template for the form used to create a new dream entry.

### `templates/dream/login.html`
This file is the template for the login page, where users can enter their username and password to access their dream journal.

### `templates/dream/register.html`
This file is the template for the registration page, where new users can create an account.

## Python Packages Used
These are the Python Packages used in the project, which are also located in the requirments.txt file:

asgiref==3.8.1
Django==5.1.2
Markdown==3.7
sqlparse==0.5.1
tzdata==2024.2

## How to run the application
To run the application, you have to follow these steps:
1. Clone the repository:
    git clone https://github.com/hrishitaparanjape/capstone.git
    cd capstone

2. Install the required python packages:
    pip install -r requirements.txt

4. Apply the database migrations:
    python manage.py makemigrations dream
    python manage.py migrate

6. Run the server:
    python manage.py runserver

7. Now you can navigate to `http://127.0.0.1:8000` on your web browser to access the application.










