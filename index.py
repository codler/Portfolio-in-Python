#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Filename:   index.py
Authors:    Han Lin Yap and Alexander Östman
Course:     TDP003 - Projekt: Egna datormiljön
Date:       HT09   - 2009-10-07
Program:    LiU/IP1
Desciption: This is the startpage. 
"""


import kid
import os
from config import *
kid.enable_import(path=os.path.dirname(__file__) + "/" + "templates")

def index():
    template = kid.Template(name='home', 
                            headline=get_text('startpage'),
                            title=get_text('sitename'),
                            **common_language[DEFAULT_LANGUAGE])
    template.cache = False

    return template.serialize(output='xhtml-strict')
