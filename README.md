
# Groceries List

Python Full stack demo app

## Features

 - Families
   - Create families in the system
   - Allow users to 'join' families  
 - Users
   - Sign up
   - Sign in
   - Sign out
 - Lists and Tasks
   - View list items for selected family
   - add, delete, change state ( started, finished, none )



## Live demo

http://35.183.2.50:5000/users


## Technologies

[alembic](https://alembic.zzzcomputing.com/en/latest/) migrations
[Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) database ORM
[Flask-restplus](https://flask-restplus.readthedocs.io/en/stable/) Rest API

## API routes and models ( swagger UI )

http://35.183.2.50:5000/

## First time setup
```bash
# >  /groceriesApp/app/pip3 install -r requirements.txt

# > /groceriesApp/python3 manage.py db init
# > /groceriesApp/python3 manage.py db migrate
# > /groceriesApp/python3 manage.py db upgrade
```

## Running the app
```bash
# > /groceriesApp/python3 manage.py run
```

##Todos

Management UI for Users, Families, and Memberships
Better UI in general
Real-time notifications when a list is modified by another family member


