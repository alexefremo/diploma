#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bson
import cgi
import hashlib
import hmac
import pymongo
import random
import re
import string
import sys

def make_salt():
    salt = ""
    for i in range(4):
        salt = salt + random.choice(string.ascii_letters)
    return salt

def make_pw_hash(pw,salt=None):
    if (salt == None):
        salt = make_salt();
    return hashlib.sha256(pw + salt).hexdigest()+","+ salt

def validate_signup(username, password, verify, email, errors):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    PASS_RE = re.compile(r"^.{3,20}$")
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

    errors['username_error']  = ""
    errors['password_error'] = ""
    errors['verify_error'] = ""
    errors['email_error'] = ""
    

    if not USER_RE.match(username):
        errors['username_error']  = "неподходящее имя пользователя, попробуйте только буквы и цифры"
        return False

    if not PASS_RE.match(password):
        errors['password_error'] = "неподходящий пароль"
        return False
    if password != verify:
        errors['verify_error'] = "пароли должны совпадать"
        return False
    if email != "":
        if not EMAIL_RE.match(email):
            errors['email_error'] = "неподходящий e-mail адрес"
            return False
    return True

def validate_login(connection, username, password, user_record):
    db = connection.blog
    users = db.users

    try:
        user = users.find_one({'_id':username})
    except:
        print "Невозможно сделать запрос к БД"

    if user == None:
        print "Пользователь не зарегистрирован"
        return False
    
    salt = user['password'].split(',')[1]

    if (user['password'] != make_pw_hash(password,salt)):
        print "неверный пароль"
        return False

    for key in user:
        user_record[key] = user[key] # perform a copy

    return True

def start_session(connection, username):
    db = connection.blog
    sessions = db.sessions

    session = {'username':username}

    try:
        sessions.insert(session, safe=True)
    except:
        print "Ошибка в функции start_session:", sys.exc_info()[0]
        return -1

    return str(session['_id'])

def end_session(connection, session_id):
    db = connection.blog
    sessions = db.sessions

    try:
        id = bson.objectid.ObjectId(session_id)
        sessions.remove({'_id':id})
    except:
        
        return

def get_session(connection, session_id):

    db = connection.blog
    sessions = db.sessions

    try:
        id = bson.objectid.ObjectId(session_id)
    except:
        print "передан неподходящий sessionid"
        return None

    session = sessions.find_one({'_id':id})

    return session

def newuser(connection, username, password, email):
    password_hash = make_pw_hash(password)

    user = {'_id':username, 'password':password_hash}
    if (email != ""):
        user['email'] = email

    db = connection.blog
    users = db.users

    try:
        db.users.insert(user, safe=True)
    except pymongo.errors.OperationFailure:
        print "ошибка базы данных"
        return False
    except pymongo.errors.DuplicateKeyError as e:
        print "такое имя пользователя уже занято"
        return False

    return True

def uid_to_username(connection, uid):
    db = connection.blog
    users = db.users
    
    user = users.find_one({'uid':int(uid)})

    return user['username']

# Описываю функцию hash_str для использования HMAC с нашим ключем SECRET
SECRET = 'verysecret'
def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

# хешируем значение cookie
def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

# проверяем, что cookie все еше защищена
def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val