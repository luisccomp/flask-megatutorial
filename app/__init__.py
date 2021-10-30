from flask import Flask

from app.settings import Settings

app = Flask(__name__)
app.config.from_object(Settings)

from app import routes
