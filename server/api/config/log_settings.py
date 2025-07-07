import logging
import sys

log = logging.getLogger(__name__)

LOG_SETTINGS = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'info_stream_access': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'access',
            'stream': sys.stdout,
        },
        'info_access': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'access',
            'filename': './api/log/info.log',
            # 'filename': './api/log/info_access.log',
            'maxBytes': 1024 * 1024 * 200,
            'backupCount': 5,
            'encoding': 'utf-8'
        },
        'info_stream_root': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'root',
            'stream': sys.stdout,
        },
        'info_root': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'root',
            'filename': './api/log/info.log',
            # 'filename': './api/log/info_root.log',
            'maxBytes': 1024 * 1024 * 200,
            'backupCount': 5,
            'encoding': 'utf-8'
        },
        'error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'debug',
            'filename': './api/log/error.log',
            'maxBytes': 1024 * 1024 * 200,
            'backupCount': 5,
            'encoding': 'utf-8'
        },
    },
    'formatters': {
        'root': {
            'format': '%(asctime)s %(levelname)s %(name)s:%(lineno)d | %(message)s',
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter",
        },
        'debug': {
            'format': '%(asctime)s - %(levelname)s - %(name)s:%(lineno)d | %(message)s',
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter",
        },
        "access": {
            "format": "%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: %(request)s %(message)s %(status)d %(byte)d",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter",
        }
    },
    'loggers': {
        'sanic.access': {
            'level': 'INFO',
            'handlers': ['info_access','info_stream_access'],
            "propagate": True,
            "qualname": "sanic.access",
        },
        'sanic.root': {
            'level': 'INFO',
            'handlers': ['info_root', 'info_stream_root'],
            "propagate": True,
            "qualname": "sanic.root",
        },
        'sanic.error': {
            'level': 'ERROR',
            'handlers': ['error'],
            'propagate': True
        },

    }
}

# logger = logging.getLogger("sanic.root")
# """
# General Sanic logger
# """
#
# access_logger = logging.getLogger("sanic.access")
# """
# Logger used by Sanic for access logging
# """
#
# error_logger = logging.getLogger("sanic.error")
# """
# Logger used by Sanic for error logging
# """