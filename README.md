# Python-Django-Framework
Django is a Python-based free and open-source web framework that follows the model-template-view (MVT) Architectural Pattern. It is maintained by the Django Software Foundation. It is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development.

# Major Topics Contents:

  - MVT Design Pattern Overview
  - Django Architechture
  - URL & View Pattern
  - App
  - Templates
  - URL's Pattern
  - Include
  - Render Context
  - Passing data HTTP Response & Render
  - Static Files
  - Bootstrap Loading
  - Template Inherit
  - Template Mastering
  - For Loop
  - Migrate & Migrations
  - SuperUser
  - Django Admin
  - Models

# Most Command Line for Django Web Framework

- python --version
- python -m django --version
- pip list
- pip install django
- pip uninstall django

- django-admin
- django-admin startproject [your_project_name]

- python manage.py help
- python manage.py runserver [127.0.0.0:8000] [by Default]
- python manage.py runserver 8080 [127.0.0.0:8080] [Custom Port]
- python manage.py startapp [your_app_name]

- python manage.py migrate
- python manage.py createsuperuser
- python manage.py makemigrations
- python manage.py showmigrations

# Working with QuerySets, Django ORM
- Our Model is Post
  - post.objects.get(username='admin')
  
  - post = Post(title='BMW')
    post.save()
  
  - post.title = 'New Title'
    post.save()
  
  - all_posts = Post.objects.all()
  
  - Post.objects.filter(publish_year=2020)
  
  - Post.objects.order_by('title')
    Post.objects.order_by('-title')
  
  - post = Post.objects.get(id=1)
    post.delete()


