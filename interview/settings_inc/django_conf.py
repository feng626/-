import os

from common.util.path import dirname

BASE_DIR = dirname(os.path.abspath(__file__), repeat=3)

ALLOWED_HOSTS = ['*']

SECRET_KEY = '2$f2)kf)l#&kfd+a8&pb-eytb019oa+q0(#qcp$4awe$)))h3v'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

DATABASES = {
    'default': {
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': '123',
        'PORT': 3306,
        'HOST': '127.0.0.1',
        'ENGINE': 'django.db.backends.mysql'
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ROOT_URLCONF = 'interview.urls'

AUTH_USER_MODEL = 'user.User'

WSGI_APPLICATION = 'interview.wsgi.application'
# AUTHENTICATION_BACKENDS = [
#     'user.extenion.backends.MyModelBackend',
#     'user.extenion.backends.UserNoBackend',
#     'user.extenion.backends.RBACBackend',
# ]
