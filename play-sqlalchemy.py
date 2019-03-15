#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, BigInteger
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_object('app-config')
db = SQLAlchemy()


class User(db.Model):
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    age = Column(Integer)
    name = Column(String(length=30))
    zyx_name = Column(String(length=30))


db.init_app(app)
db.create_all(app=app)

db.se

if __name__ == '__main__':
    app.run()
