py - m venv test
source test/Scripts/activate # Remind using it in GitBash
pip install django
django-admin startproject project
django-admin startapp apps

# Configuration Settings File

# Step 01 :
# if not import in any case, use it before starting configurations
import os.path
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps', # Put your apps name here. This is your apps name while creating apps in intial stage. 
]

# Step 02 :
# Add these 2 lines code after BASE_DIR
BASE_DIR       = Path(__file__).resolve().parent.parent
TEMPLATES_DIR  = os.path.join(BASE_DIR, 'templates')
STATIC_DIR     = os.path.join(BASE_DIR, 'static')


# Step 03 :
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR], # Here is your update line of the codes. Put your defined template directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Step 04 :
STATIC_URL      = '/static/'
STATICFILES_DIRS = [STATIC_DIR] # Add this line

# Step 05:
# In Root folder urls.py, update codes

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls') ),
]

# Step 06 :
# In App folder urls.py, use this code

from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home)
]

# Step 07 :
# Make ensure project structure as below
- project
- apps
- static
   - img
   - css
   - js
   - audio
   - video
 - templates
   - index.html

# static 08 :
# index.html
# For HTML : {% load static %}
# For CSS  : <link rel="stylesheet" href="{% static 'css/style.css' %}">
# For Image: <img src="{% static 'img/photo.jpg' %}" alt="">
# For JS   : <script type="text/javascript" src="{% static 'js/jquery.min.js' %}"></script>
# For Video: <video width="320" height="240" controls><source src="{% static 'video/sample.mp4' %}" type="video/mp4"></video><
# For Audio: <audio controls><source src="{% static 'audio/music.mp3' %}" type="audio/mp3"></audio> 	
