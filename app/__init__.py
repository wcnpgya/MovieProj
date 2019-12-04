#coding:utf-8
from flask import Flask
app = Flask(__name__)
app.debug = True
from app.home import home as home_bluePrint
from app.admin import admin as admin_bluePrint
from app.admin import Truman as Truman_bluePrint


app.register_blueprint(home_bluePrint)
app.register_blueprint(admin_bluePrint, url_prefix="/admin")
app.register_blueprint(Truman_bluePrint)