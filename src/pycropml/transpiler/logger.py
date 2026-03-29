from __future__ import absolute_import

import logging

_LOGGER_NAME = 'pycropml'


def _normalize_level(level):
    if isinstance(level, int):
        return level
    if not level:
        return logging.WARNING
    value = str(level).upper()
    return getattr(logging, value, logging.WARNING)


def configure_logging(level='WARNING'):
    """Configure the shared pycropml logger once and return it."""
    logger = logging.getLogger(_LOGGER_NAME)
    logger.setLevel(_normalize_level(level))

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s [%(name)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
        logger.addHandler(handler)

    logger.propagate = False
    return logger


def get_logger(name=None):
    """Return the root pycropml logger or a child logger."""
    if not name:
        return logging.getLogger(_LOGGER_NAME)
    return logging.getLogger('%s.%s' % (_LOGGER_NAME, name))
