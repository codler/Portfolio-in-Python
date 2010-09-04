#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Filename:   techniques.py
Authors:    Han Lin Yap and Alexander Östman
Course:     TDP003 - Projekt: Egna datormiljön
Date:       HT09   - 2009-10-07
Program:    LiU/IP1
Desciption: This is the techniques page handler. 
"""

import kid
import os
import data
from config import *
kid.enable_import(path=os.path.dirname(__file__) + "/" + "templates")

def index():
    #default template
    template = kid.Template(name=os.path.basename(__file__)[:-3], 
                            title=get_text('sitename') + '-' + get_text(os.path.basename(__file__)[:-3]), 
                            projects=[],
                            techs= [],
                            headline=get_text(os.path.basename(__file__)[:-3]),
                            project_not_found=get_text('database_not_available'),
                            **common_language[DEFAULT_LANGUAGE])

    data.init()
    techniques = data.retrieve_technique_stats()
    
    
    if techniques[0] == 0:
        template = kid.Template(name=os.path.basename(__file__)[:-3],
                                title=get_text('sitename') + ' - ' + get_text('techniques'),
                                headline=get_text('techniques'), 
                                techs=techniques[1],
                                project_not_found='',
                                **common_language[DEFAULT_LANGUAGE])
    template.cache = False

    return template.serialize(output='xhtml-strict')
