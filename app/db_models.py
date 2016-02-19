'''Defines the database functions'''
import sqlite3
from contextlib import closing
from flask import g
from app import App

def connect_db():
    return sqlite3.connect(App.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with App.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@App.before_request
def before_request():
    g.db = connect_db()


@App.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
