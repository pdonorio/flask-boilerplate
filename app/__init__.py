#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Factory and blueprints patterns """

import os,logging
from flask import Flask, request as req
from app.controllers import pages

config = {
    "development": "config.DevelopmentConfig",
    #"testing": "bookshelf.config.TestingConfig",
    "default": "config.DevelopmentConfig"
}

def create_app(config_filename):

    app = Flask(__name__)

    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name]) # object-based default configuration
    #print(app.config)

    app.register_blueprint(pages.blueprint)
    app.logger.setLevel(logging.NOTSET)

    @app.after_request
    def log_response(resp):
        app.logger.info("{} {} {}\n{}".format(req.method,req.url,req.data,resp))
        return resp

    return app
