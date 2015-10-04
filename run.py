#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" App MAIN """

from app import create_app

from config import development as devconfig
app = create_app(devconfig)

if __name__ == '__main__':
    app.run()
