#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
import cgi
import csv
import datetime
import hmac
import pymongo
import random
import re
import sys
import user

connection_string = "mongodb://localhost"

# прописываем обработку статического css-файла
@bottle.get('/css/<filename>')
def server_static(filename):
    return bottle.static_file('style.css', root='css')

# выбираем какой шаблон показывать на главной и отправляем на /login если пользователь не зашел
@bottle.get('/')
def blog_index():
    connection = pymongo.MongoClient(connection_string)
    db = connection.diploma
    test = db.testinput

    username = login_check()  # проверяем залогинен ли пользователь и возвращаем имя пользователя в username

    if username == None:
        bottle.redirect("/login")
    elif username == "luzlol":
        return bottle.template('admin')
    else:
        return bottle.template('home', dict(username=username))

# показываем форму логинки
@bottle.get('/login')
def present_login():
    
    if (login_check() == None):
        return bottle.template("login",dict(username="", password="",login_error=""))
    else:
        bottle.redirect("/")
    
# обрабатываем риквест из логин-формы
@bottle.post('/login')
def process_login():

    connection = pymongo.MongoClient(connection_string)

    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")

    print "user submitted ", username, "pass ", password

    userRecord = {}
    if (user.validate_login(connection, username, password, userRecord)):
        session_id = user.start_session(connection, username)
        if (session_id == -1):
            bottle.redirect("/internal_error")

        cookie = user.make_secure_val(session_id)

        # не работает с bottle .12, откатитесь на версию .11
        bottle.response.set_cookie("session", cookie)
        
        bottle.redirect("/")

    else:
        return bottle.template("login", 
                           dict(username=cgi.escape(username), password="", 
                                login_error="Invalid Login"))

@bottle.get('/internal_error')
@bottle.view('error_template')
def present_internal_error():
    return ({error:"System has encountered a DB error"})

# обработка разлогинивания
@bottle.get('/logout')
def process_logout():

    connection = pymongo.MongoClient(connection_string)
    cookie = bottle.request.get_cookie("session")

    if (cookie == None):
        print "no cookie..."
        bottle.redirect("/")
        
    else:
        session_id = user.check_secure_val(cookie)

        if (session_id == None):
            print "no secure session_id"
            bottle.redirect("/")
            
        else:
            # удаляем сессию
            user.end_session(connection, session_id)
            print "clearing the cookie"
            bottle.response.set_cookie("session","")
            bottle.redirect("/")

# форма добавления пользователя
@bottle.get("/adduser")
def present_signup():
    
    if (login_check() == "luzlol"):
        return bottle.template("signup", dict(username="", password="", password_error="", email="", username_error="", email_error="", verify_error =""))
    else:
        print "not admin!"
        bottle.redirect("/")
        
# обработка добавления пользователя
@bottle.post("/adduser")
def process_signup():

    connection = pymongo.MongoClient(connection_string)
    
    email = bottle.request.forms.get("email")
    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")
    verify = bottle.request.forms.get("verify")

    # подготовоим объект, если вдруг у нас будут ошибки
    errors = {'username':cgi.escape(username), 'email':cgi.escape(email)}
    if (user.validate_signup(username, password, verify, email, errors)):
        if (not user.newuser(connection, username, password, email)):
            # дубликат
            errors['username_error'] = "Имя пользователя уже используется, пожалуйста выберите другое"
            return bottle.template("signup", errors)
            
        session_id = user.start_session(connection, username)
        print session_id
        cookie= user.make_secure_val(session_id)
        bottle.response.set_cookie("session",cookie)
        bottle.redirect("/")
    else:
        print "user did not validate"
        return bottle.template("signup", errors)

# форма импорта файла
@bottle.get('/import')
def present_import():
    
    if (login_check() == "luzlol"):
        return bottle.template("import")
    
# обработка импорта файла
@bottle.post('/import')
def do_upload():
    upload = bottle.request.files.get('upload')
    connection = pymongo.MongoClient(connection_string)
    db = connection.diploma
    importcol = db.importcol
    reader = csv.DictReader(upload.file, delimiter=';')
    # наименование;инвентарный-номер;дата-поступления;начальное-количество;цена;дата-выдачи;количество-выдано
    for key in reader:
        item = unicode(key['0'],'cp1251')
        number = unicode(key['1'],'cp1251')
        datein = unicode(key['2'],'cp1251')
        amountstart = unicode(key['3'],'cp1251')
        price = unicode(key['4'],'cp1251')
        dateout = unicode(key['5'],'cp1251')
        amountend = unicode(key['6'],'cp1251')
        keys = {
        'Наименование':item,
        'Инвентарный номер':number,
        'Дата поступления':datein,
        'Начальное количество':amountstart,
        'Цена':price,
        'Дата выдачи':dateout,
        'Выдано количество':amountend
        }
        importcol.update(keys, keys, upsert=True, safe=True)
    return "OK <a href=\"/\">На главную</a>"

# проверяем залогинен ли пользователь и возвращаем username, если пользователь не залогинен – возвращает None
def login_check():
    connection = pymongo.MongoClient(connection_string)
    cookie = bottle.request.get_cookie("session")

    if (cookie == None):
        print "no cookie..."
        return None

    else:
        session_id = user.check_secure_val(cookie)

        if (session_id == None):
            print "no secure session_id"
            return None
            
        else:
            # look up username record
            session = user.get_session(connection, session_id)
            if (session == None):
                return None

    return session['username']

bottle.run(host='localhost', port=8082, debug=True)