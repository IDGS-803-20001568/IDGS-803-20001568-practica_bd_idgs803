import os 
from sqlalchemy import create_engine
import urllib

# Se necesitainstalar estas cosas
# pip install SQLAlchemy
# pip install Flask-SQLAlchemys
# pip install PyMySQL

class Config(object):
    SECRET_KEY='Clave_Nueva'
    SESSION_COOKIE_SECURE= False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:@127.0.0.1/pruebas_bd_idgs803'
    SQLALCHEMY_TRACK_MODIFICATIONS=False