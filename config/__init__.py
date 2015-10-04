#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Configurations """

import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = 'my precious'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'database.db')

    HOST = 'localhost'
    PORT = int(os.environ.get('PORT', 5000))

class DevelopmentConfig(BaseConfig):

    DEBUG = True
    HOST = '0.0.0.0'
