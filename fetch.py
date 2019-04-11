# coding=utf-8
# python 3.7.3

import worker

import sqlite_data

sqlite_data.init_data()
worker.fetch_villages('2018')