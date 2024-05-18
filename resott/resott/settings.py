from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-ugzvpa!w=c9#(+()7*2rs+zn3e*b7fk(z)&qva392!@7k=tz_e'
DEBUG = True #if true it will show the debugs but when deploying it must be false

ALLOWED_HOSTS = []
# Application definition

INSTALLED_APPS = [ #we register api and apps here
    'django.contrib.admin',
    'home.apps.HomeConfig',     
    'account.apps.AccountConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'paypal.standard.ipn',
]

MIDDLEWARE = [   #useful for authentication,request/response,security,framework of hook into django request/response processing
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'resott.urls' 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"template")], #path of the template,in template folder we have all the pages
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

WSGI_APPLICATION = 'resott.wsgi.application' #for deployment
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Resott' ,
        'PASSWORD': '1234' ,
        'USER' : 'postgres' ,
        'HOST' : 'localhost'
    }
}
# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'  #static part like css
STATICFILES_DIRS=[os.path.join(BASE_DIR,"static")] #joing base path with the static path
STATIC_ROOT=os.path.join(BASE_DIR,'assets') #putting all the static files in assets folder

MEDIA_URL='/media/' #automatic media folder that contains all the media including default media
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

PAYPAL_RECEIVER_EMAIL='stutimishra58@gmail.com'
PAYPAL_TEST = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
