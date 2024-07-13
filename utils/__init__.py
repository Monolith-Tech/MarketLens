# utils.py
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

def validate_url(url):
    # Validate URL format
    pass
