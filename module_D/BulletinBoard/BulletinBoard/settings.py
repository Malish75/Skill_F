from pathlib import Path
import os

# Build paths inside the BulletinBoard like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=intx-*0njk_yb!*m2)l(@ug4b&_n5t#x$xsk^oyyhqa$*@6u&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',
                 'localhost',
                ]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'account',  # pip install django-user-accounts
    'bootstrap4',

    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',

    'boardapp',
    # 'blog.apps.BlogConfig',
    # 'accounts.apps.AccountsConfig',
    'django_filters'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware'
]

ROOT_URLCONF = 'BulletinBoard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'account.context_processors.account',
            ],
        },
    },
]


TEMPLATE_CONTEXT_PROCESSORS = ["account.context_processors.account",]


WSGI_APPLICATION = 'BulletinBoard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )


ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False  # todo вернуть тру для подтверждения регистрации
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

# ACCOUNT_LOGIN_URL = 'boardapp:account_login'

# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = ACCOUNT_LOGIN_URL
# ACCOUNT_PASSWORD_RESET_REDIRECT_URL = ACCOUNT_LOGIN_URL
# ACCOUNT_EMAIL_CONFIRMATION_URL = "boardapp:account_confirm_email"
# ACCOUNT_SETTINGS_REDIRECT_URL = 'boardapp:account_settings'
# ACCOUNT_PASSWORD_CHANGE_REDIRECT_URL = "boardapp:account_password"


# LOGIN_URL = '/account/login/'  #  через allauth
# LOGIN_REDIRECT_URL = '/'

SITE_ID = 3

'''
Пока разрабатывается проект (в режиме DEBUG = True) можно вместо отправки почты через почтовый сервис, использовать консоль (т.е. все отправки писем будут выводится в консоли в запущенном проекте ./manage.py runserver)'''
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# Settings for django-bootstrap4
BOOTSTRAP4 = {
    "error_css_class": "bootstrap4-error",
    "required_css_class": "bootstrap4-required",
    "javascript_in_head": True,
    "include_jquery": True,
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

" для работы account"
DEFAULT_FROM_EMAIL = 'asmal75@bk.ru'
EMAIL_HOST = "smtp.mail.ru"
EMAIL_PORT = 465
EMAIL_HOST_USER = "asmal75"
EMAIL_HOST_PASSWORD = "Angel@101"
EMAIL_USE_SSL = True
# EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же
# EMAIL_PORT = 465  # 2265 порт smtp сервера тоже одинаковый
# EMAIL_HOST_USER = 'andstamal'  # ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки
# EMAIL_HOST_PASSWORD = 'AnGeliNa101001'  # пароль от почты
# EMAIL_USE_SSL = True  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках, но включать его здесь обязательно
# EMAIL_USE_TSL = False
# DEFAULT_FROM_EMAIL = 'andstamal@yandex.ru'
# или
#DEFAULT_FROM_EMAIL = EMAIL_HOST_USER + '@yandex.ru'




AUTHENTICATION_BACKENDS = [
    'account.auth_backends.EmailAuthenticationBackend',
]