#coding:utf-8
from . import admin, Truman

@admin.route("/")
def index():
    return "<h1 style='color:red'>this is admin</h1>"

@Truman.route("/Truman")
def index():
    return "<h2 style='color:orange'>You're going to the top of this mountain,broken legs and all.</h2>"
