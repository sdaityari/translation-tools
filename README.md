
###Install dependencies:
>Django 1.4 without Apache (https://docs.djangoproject.com/en/1.4/topics/install/)   
>translate-toolkit (http://docs.translatehouse.org/projects/translate-toolkit/en/latest/installation.html)   

###In "src/translationtools/settings.py"
>Set database username, password in DATABASES   
>Set MEDIA_ROOT to src/media (provide full path)   
>Set STATICFILES_DIRS   
>Set TEMPLATE_DIRS   

###To get the server running
>Create MySQL database (with the name that you set in settings.py)   
>From src directory, run python manage.py syncdb   
>To run server, python manage.py runserver   
