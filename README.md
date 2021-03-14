# Requirements
- Make sure to have Docker installed and up to date
- Check that the settings.py file in tscompose has the correct DB parameters 
-   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'techstaffDB',
        'USER' : 'user',
        'PASSWORD' : 'password',
        'HOST': 'db',
        'PORT': '3306',
    }
# TechStaffApp
Run the following commands:
- "docker-compose build"   

- "docker-compse up -d"

# Notes
if you get a "cannot connect to DB" type of error, try migrating the DB AKA the command:
- run "docker-compose run web python manage.py migrate"
