"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os 
import environ



# instance is initialized with some default values
env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, ''),
    DB_NAME=(str, ''),
    DB_USER=(str, ''),
    DB_PASSWORD=(str, ''),
    DB_HOST=(str, 'localhost'),
    DB_PORT=(str, '5432'),
    EMAIL_HOST_USER=(str, ''),
    EMAIL_HOST_PASSWORD=(str, ''),
    RAZORPAY_KEY_ID=(str, ''),
    RAZORPAY_KEY_SECRET=(str, ''),
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=(str, ''),
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=(str, ''),
)



BASE_DIR = Path(__file__).resolve().parent.parent


environ.Env.read_env(os.path.join(BASE_DIR, '.env'))





SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

# ALLOWED_HOSTS = ['*']

ALLOWED_HOSTS = ['vegefoods.shop', 'www.vegefoods.shop']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'user',
    'admin_panel',
    'django.contrib.sites',  # Required by Django-Allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',  # Google provider
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'admin_panel.middleware.BlockedUserMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates'),
            os.path.join(BASE_DIR, 'admin_panel', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}




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




STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'assets'),
    
]

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')


FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]



MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user.CustomUser'  # needed while using abstractuser model


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True 
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# loging out error solving
LOGOUT_REDIRECT_URL = 'login'  # Use the name of your login URL pattern

# settings.py
# DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760

DEBUG = True




AUTHENTICATION_BACKENDS =  [
  
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
    
]

SITE_ID = 1


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': env('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'),
            'secret': env('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'),
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# Allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_UNIQUE_EMAIL = True
SOCIALACCOUNT_AUTO_SIGNUP = True


# Login/logout settings
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/welcome/'
LOGOUT_REDIRECT_URL = '/'



ACCOUNT_FORMS = {
    'login': 'user.forms.CustomLoginForm',
    'signup': 'user.forms.CustomSignupForm',
}





# Razorpay Credentials
RAZORPAY_KEY_ID = env('RAZORPAY_KEY_ID')
RAZORPAY_KEY_SECRET = env('RAZORPAY_KEY_SECRET')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'ERROR',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': '/home/ubuntu/vegefoods/VEGEFOODS/debug.log',
            'formatter': 'verbose',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
        '': {  # Root logger
            'handlers': ['console', 'file'],
            'level': 'DEBUG',  # This will capture all DEBUG level logs
        },
    },
}







