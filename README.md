# Django Tenant MySQL

**Introduction to multi-tenant applications using MySQL database**

## Requirements

- Python3.8 +
- Django 4

## Building


```shell
$ # Clone the repo
$ git clone https://github.com/mahtat555/django-tenant-postgresql.git

$ # Go to the root folder
$ cd django-tenant-postgresql

$ # # Create isolated Python environment
$ python -m venv venv
$ source venv/bin/activate

$ # Install the required libraries
$ pip install -r requirements.txt

$ # Set up the project configuration
$ cd src
$ cp .env.example .env
$ # Please Don't forget to provide the configuration variables
$ # Also the creation of the database

$ # Run the migrations
$ python manage.py migrate

$ # Start the Server
$ python manage.py runserver
```
