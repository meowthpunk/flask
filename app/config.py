# import os

# Grabs the folder where the script runs.
# basedir = os.path.abspath(os.path.dirname(__file__))

API_KEY = "EuYBJ3ELuAxlsd4yECA4tRTX3TZh4rsf"

class Config():

    # Set up the App SECRET_KEY
    SECRET_KEY = 'EuYBJ3ELuAxlsd4yECA4tRTX3TZh4rsf'
    UPLOAD_FOLDER = 'images'

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
