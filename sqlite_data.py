# coding=utf-8
# python 3.7.3

import sqlite3

def init_data():
    print("initing sqlite data file")
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('create table IF NOT EXISTS provinces (code varchar(20) primary key,parent varchar(20), name varchar(100))')
    cursor.execute('create table IF NOT EXISTS cities (code varchar(20) primary key,parent varchar(20), name varchar(100))')
    cursor.execute('create table IF NOT EXISTS counties (code varchar(20) primary key,parent varchar(20), name varchar(100))')
    cursor.execute('create table IF NOT EXISTS towns (code varchar(20) primary key,parent varchar(20), name varchar(100))')
    cursor.execute('create table IF NOT EXISTS villages (code varchar(20) primary key,parent varchar(20), name varchar(100))')
    cursor.execute('DELETE FROM provinces')
    cursor.execute('DELETE FROM cities')
    cursor.execute('DELETE FROM counties')
    cursor.execute('DELETE FROM towns')
    cursor.execute('DELETE FROM villages')
    cursor.close()
    conn.commit()
    conn.close()
    return ''

def save_provinces(data):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.executemany('insert into provinces(code,name) values(?,?)',data)
    cursor.close()
    conn.commit()
    conn.close()
    return ''

def save_cities(data):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.executemany('insert into cities(code,name,parent) values(?,?,?)',data)
    cursor.close()
    conn.commit()
    conn.close()
    return ''

def save_counties(data):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.executemany('insert into counties(code,name,parent) values(?,?,?)',data)
    cursor.close()
    conn.commit()
    conn.close()
    return ''

def save_towns(data):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.executemany('insert into towns(code,name,parent) values(?,?,?)',data)
    cursor.close()
    conn.commit()
    conn.close()
    return ''

def save_villages(data):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.executemany('insert into villages(code,name,parent) values(?,?,?)',data)
    cursor.close()
    conn.commit()
    conn.close()
    return ''