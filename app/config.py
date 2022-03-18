import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME','admin')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD','Password123')
    BOOKING_FOLDER = os.environ.get('BOOKING_FOLDER')