from io import StringIO
import os

from dotenv import load_dotenv

FLASK_ENV = os.environ.get('FLASK_ENV')

with open('.env' if FLASK_ENV != 'test' else '.env.test') as dotenv:
    load_dotenv(stream=StringIO(dotenv.read()), override=True)

basedir = os.path.abspath(os.path.dirname(__file__))

class Settings:
    SECRET_KEY = os.environ.get('SECRET_KEY') \
        or 'aec8084845b41a6952d46cbaa1c9b798659487ffd133796d95d05ba45d9096c2'

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') \
        or os.path.join(basedir, 'app.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    ADMINS = ['your-email@example.com']
