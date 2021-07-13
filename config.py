import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    secret_key = os.environ.get('secret_key')
    sqlalchemy_database_uri = os.environ.get('database_url')
    sqlalchemy_track_modifications=False