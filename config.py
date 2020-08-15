from flask import Flask

HOST = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = '123123'
DATABASE = 'bw_student'
db_url = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = db_url
SQLALCHEMY_TRACK_MODIFICATIONS = False
