import os

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_IP = os.getenv('DB_IP')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

SQLALCHEMY_DATABASE_URI = "mysql://{0}:{1}@{2}:{3}/{4}".format(DB_USERNAME, DB_PASSWORD, DB_IP, DB_PORT, DB_NAME)
