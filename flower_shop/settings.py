import os
from pathlib import Path

from django.contrib import messages

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '(t2w63ugzv*xph#ghcqvu2-&7+22$ga7%s0x!ewzxusuo75zcl'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',
    'django_filters',
    'crispy_forms',
    'phonenumber_field',
    'django_tables2',
    'django_extensions',  # for shell_plus
    'rest_framework',

    'api.apps.ApiConfig',
    'account.apps.AccountConfig',
    'custom_admin.apps.CustomAdminConfig',
    'main.apps.MainConfig',
    'core.apps.CoreConfig',
    'reviews.apps.ReviewsConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'flower_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processor.categories',
                'cart.context_processor.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'flower_shop.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

# for local
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# for pythonanywhere
# STATIC_ROOT = BASE_DIR / 'static'

AUTH_USER_MODEL = 'account.User'
LOGIN_URL = 'user-login'
LOGOUT_REDIRECT_URL = 'product-list'
LOGIN_REDIRECT_URL = 'product-list'


IMAGE_UPLOAD_PATH = 'static/uploads/images/'
IMAGE_REVIEW_UPLOAD_PATH = 'static/uploads/reviews/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

DJANGO_TABLES2_TEMPLATE = 'django_tables2/bootstrap4.html'

PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'RU'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': int(os.getenv('PAGE_SIZE', 20)),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',

    ),
    'DEFAULT_RENDERER_CLASSES': (
        # 'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        # 'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
    'DEFAULT_PARSER_CLASSES': (
        # 'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        # 'djangorestframework_camel_case.parser.CamelCaseFormParser',
        # 'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    # 'DEFAULT_FILTER_BACKENDS': (
        # 'rest_framework_filters.backends.RestFrameworkFilterBackend',
    # ),
}
