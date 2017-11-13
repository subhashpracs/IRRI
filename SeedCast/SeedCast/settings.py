"""
Django settings for SeedCast project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4s%pxae4%a3&z5-t2*_-@x03ex)n!0%oqk#k2r6#fa5)bkn4h1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ '*' ]


# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'import_export',
    'Masters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'multiselectfield',
    'rest_framework',
    'report_builder',
    'highcharts',
    'corsheaders',
    #'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True#For Allow-Access-Control headers

CORS_ORIGIN_WHITELIST = ('35.154.189.226:6565',)

ROOT_URLCONF = 'SeedCast.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'SeedCast.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'OPTIONS': {
        #     # ...
        #     'timeout': 100,
        #     # ...
        # }
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_root')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static/'),
  # '/var/www/static/',
  #   "/home/sai/Desktop/Jetpractice/static",
)

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]



# MEDIA_ROOT = '/home/ubuntu/irri-pracs/SeedCastfromGit/IRRI-Test/SeedCast'

MEDIA_ROOT = '/home/sai/Desktop/SeedCast'

JET_DEFAULT_THEME = 'green' #For Default Theme Colour


#XLS Importer...
DATA_IMPORTER_EXCEL_DECODER = "cp1252"

DATA_IMPORTER_DECODER = "UTF-8"

SOUTH_MIGRATION_MODULES = {
        'data_importer': 'data_importer.south_migrations',
    },

MIGRATION_MODULES = {
        'data_importer': 'data_importer.django_migrations'
    }


#Another import

IMPORT_EXPORT_USE_TRANSACTIONS = True


FILE_UPLOAD_HANDLERS = ("django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler")





#Django REST Framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAdminUser',
        # 'rest_framework.permissions.IsAuthenticated',
    ]

    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework.authentication.BasicAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    #     # 'rest_framework.authentication.TokenAuthentication',
    #     ],
}




#Admin Action is disabled by default...to enabling. Follow below step
REPORT_BUILDER_GLOBAL_EXPORT = True






