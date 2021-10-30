from io import StringIO
import os

from dotenv import load_dotenv

FLASK_ENV = os.environ.get('FLASK_ENV')

with open('.env' if FLASK_ENV != 'test' else '.env.test') as dotenv:
    load_dotenv(stream=StringIO(dotenv.read()), override=True)


class Settings:
    SECRET_KEY = os.environ.get('SECRET_KEY') \
        or 'aec8084845b41a6952d46cbaa1c9b798659487ffd133796d95d05ba45d9096c2'
