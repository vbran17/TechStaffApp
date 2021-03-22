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
 - Run "pip freeze" and make sure the output matches that of the "requirements.txt" file
# TechStaffApp Run project
Run the following commands in the same file directory as the manage.py file:
- "docker-compose build"   

- "docker-compse up -d"

- Go to "localhost:8000". Should see the Django default app view (Rocket thingy)

# Notes
if you get a "cannot connect to DB" type of error, try migrating the DB AKA the command:
- run "docker-compose run web python manage.py migrate"

