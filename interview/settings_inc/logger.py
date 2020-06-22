import os

from common.util.path import dirname

LOG_DIR = os.path.join(dirname(os.path.abspath(__file__), repeat=3), 'mnt', 'var', 'log')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'base': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s',
        },
        'exception': {
            'format': '----------------------------------------- '
                      '\n%(asctime)s \n%(message)s',
        },
        'error': {
            'format': '%(asctime)s %(message)s',
        },
        'print': {
            'format': '%(asctime)s %(levelname)s -> %(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'info.txt'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 20,
            'formatter': 'base',
        },
        'access_log': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'access.txt'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 20,
            'formatter': 'print',
        },
        'exception': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'exception.txt'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 20,
            'formatter': 'exception',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'print': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'print',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'django': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'django.txt'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 20,
            'formatter': 'base',
        },
    },
    'loggers': {
        'root': {
            'handlers': ['file', 'print'],
            'level': 'INFO',
            'propagate': False,
        },
        'access_log': {
            'handlers': ['access_log'],
            'level': 'INFO',
            'propagate': False,
        },
        'print': {
            'handlers': ['print'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'exception': {
            'handlers': ['exception'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django': {
            'handlers': ['console', 'django'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}
