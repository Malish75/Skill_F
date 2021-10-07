import os
from pathlib import Path
import logging
# from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@c&fle+1jx-d6cg8n%xwj+h_udu@@o3j6px#b)(zuss5od_2m&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '127.0.0.2']

# Application definition
INSTALLED_APPS = [
    'djangosecure',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_apscheduler',
    'django_celery_beat',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'fpages',
    'bootstrap4',
    # 'newapp',
    'sign',
    'protect',
    #любые обработчики сигналов, добавленные в signals.py, будут автоматически подключаться к нашему приложению.
    'newapp.apps.NewConfig',
    'sslserver',
    'pytz',
]


MIDDLEWARE = [
    # 'djangosecure.middleware.SecurityMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'newapp.middlewares.TimezoneMiddleware',
]


ROOT_URLCONF = 'NewsPortal.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        # 'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # `allauth` needs this from django
                'django.template.context_processors.request',

            ],
        },
    },
]

WSGI_APPLICATION = 'NewsPortal.wsgi.application'


# Database https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
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

LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('ru', 'Русский'),
    ('en-us', 'English'),
)
# Internationalization https://docs.djangoproject.com/en/3.1/topics/i18n/

TIME_ZONE = 'Europe/Moscow'
USE_I18N = True                                             # интернационализация в приложении - перевод через gettext
USE_L10N = True                                             # локализованный формат даты
LOCALE_PATH = [os.path.join(BASE_DIR, 'locale'),]
USE_TZ = True                                               # используется ли часовой пояс


# TEMPLATE_CONTEXT_PROCESSORS = ("django.core.context_processors.i18n",)

# Static files (CSS, JavaScript, Images) https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = ((BASE_DIR / 'static'),)


# для загрузки медиа (урок из ютуб)
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'


SITE_ID = 2


# добавил из документации изза ошибках в консоли о примари кей
# HINT: Configure the DEFAULT_AUTO_FIELD setting or the NewConfig.default_auto_field attribute
# to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'
DEFAULT_AUTO_FIELD='django.db.models.AutoField'


#allauth
AUTHENTICATION_BACKENDS = [
# бекенд классической аутентификации, чтобы работала авторизация через обычный логин и пароль
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'  # mandatory, optional
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True # активирует аккаунт сразу при переходе по ссылке из письма
ACCOUNT_USERNAME_BLACKLIST = ['admin',
                              #'asmal75', 'Malish75',
                              ]


ACCOUNT_LOGOUT_REDIRECT_URL= '/news/'
LOGIN_URL = '/account/login/'  #  через allauth
# LOGIN_REDIRECT_URL = '/news/'
LOGOUT_REDIRECT_URL = '/'


EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465  # 2265 порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = 'andstamal'  # ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = '###########'  # пароль от почты
EMAIL_USE_SSL = True  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках, но включать его здесь обязательно
EMAIL_USE_TSL = False
DEFAULT_FROM_EMAIL = 'andstamal@yandex.ru'
# или
#DEFAULT_FROM_EMAIL = EMAIL_HOST_USER + '@yandex.ru'


#при рассылке админам
ADMINS = [
    ('admin', 'asmal75@bk.ru'),
    # список всех админов в формате ('имя', 'их почта')
]


MANAGERS = [
    ('manager', 'asmal75@bk.ru'),
    # список всех админов в формате ('имя', 'их почта')
]


SERVER_EMAIL = DEFAULT_FROM_EMAIL  # это будет у нас вместо аргумента FROM в ма


'''
Пока разрабатывается проект (в режиме DEBUG = True) можно вместо отправки почты через почтовый сервис, использовать консоль (т.е. все отправки писем будут выводится в консоли в запущенном проекте ./manage.py runserver)'''
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"


# если задача не выполняется за 25 секунд, то она автоматически снимается, увеличение сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds


CELERY_BROKER_URL = 'redis://127.0.0.1:6379'                                # URL брокера сообщений (Redis). По умолчанию он находится на порту 6379.
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'                            # хранилище результатов выполнения задач.
CELERY_ACCEPT_CONTENT = ['application/json']                                # допустимый формат данных.
CELERY_TASK_SERIALIZER = 'json'                                             # метод сериализации задач
CELERY_RESULT_SERIALIZER = 'json'                                           # метод сериализации результатов
CELERY_BEAT_SCHEDULER ='django_celery_beat.schedulers:DatabaseScheduler'
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
CELERY_TASK_ALWAYS_EAGER = True


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),                  # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
		'TIMEOUT': 60,
    }
}


logger = logging.getLogger(__name__)
#logger.info("тестовое сообщение логирования")
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {
        'console_debug': {'format': '%(asctime)-5s %(levelname)-5s %(message)s'},
        'console_warning_and_e-mail_error': {'format': '%(asctime)-5s %(levelname)-5s %(message)-5s %(pathname)s'},
        'console_error': {'format': '%(asctime)-5s %(levelname)-5s %(message)-5s %(pathname)-5s %(exc_info)s'},
        'file_general_and_file_security': {'format': '%(asctime)-5s %(levelname)-5s %(module)-5s %(message)s'},
        'file_errors': {'format': '%(asctime)-5s %(levelname)-5s %(message)-5s %(pathname)-5s %(exc_info)s'},
        },

    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
            },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
            },
    },

    'handlers': {
        'console_debug': {
            # 'level': 'DEBUG',                     # В консоль все DEBUG и выше, - время, уровень сообщения, сообщения
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_debug'},
        'console_warning': {
            'level': 'WARNING',                   # Для WARNING и выше + путь к источнику события (аргумент pathname)
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_warning_and_e-mail_error'},
        'console_error_critical': {
            'level': 'ERROR',                     # ERROR и CRITICAL еще должен выводить стэк ошибки (аргумент exc_info)
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_error',},
        'file_general': {
            'level': 'INFO',                      # INFO и выше с указанием времени, уровня логирования, модуля, сообщение.
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'logs/general.log',
            'formatter': 'file_general_and_file_security',
        },
        'file_errors': {
            'level': 'ERROR',                   # В этот из django.request, django.server, django.template, django.db_backends.
            'class': 'logging.FileHandler',
            'filename': 'logs/errors.log',
            'formatter': 'file_errors',
        },
        'file_security': {
            'level': 'DEBUG',                   # В этот только сообщения, связанные с безопасностью
            'class': 'logging.FileHandler',
            'filename': 'logs/security.log',
            'formatter': 'file_general_and_file_security',
        },
        'e-mail': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'email_backend': 'django.core.mail.backends.filebased.EmailBackend',
            'formatter': 'console_warning_and_e-mail_error',}
    },
    'loggers': {
        'django': {
            'handlers': ['console_debug', 'file_general'],
            'level': 'DEBUG',
            'propagate': True,                      # логгер будет передавать сообщения родительским логгерам.
        },
        'django.request': {
            'handlers': ['file_errors', 'e-mail',],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['file_errors', 'e-mail',],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['file_errors', ],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['file_errors', ],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['file_security'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

SECURE_SSL_REDIRECT = True