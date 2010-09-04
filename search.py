#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Filename:   search.py
Authors:    Han Lin Yap and Alexander Östman
Course:     TDP003 - Projekt: Egna datormiljön
Date:       HT09   - 2009-10-07
Program:    LiU/IP1
Desciption: This is the search page handler. 
"""

import kid
import os
import data
from config import *
kid.enable_import(path=os.path.dirname(__file__) + "/" + "templates")

def index(sort_by='start_date', sort_order='asc', techniques=None, search=None, search_fields=None):

    #default template
    template = kid.Template(name=os.path.basename(__file__)[:-3], 
                            title=get_text('sitename') + '-' + get_text(os.path.basename(__file__)[:-3]), 
                            results=[],
                            techs=[],
                            search_fields=[],
                            translate_field=[],
                            headline=get_text(os.path.basename(__file__)[:-3]),
                            project_not_found=get_text('database_not_available'),
                            **common_language[DEFAULT_LANGUAGE])

    if techniques == '':
        techniques = None
    if search_fields == '':
        search_fields = None
    if type(search_fields) != type([]) and search_fields != None:
        search_fields = [search_fields]

    data.init()
    # search projects
    results = data.retrieve_projects(sort_by, sort_order, techniques, search, search_fields)
    
    # Projects found
    if results[0] == 0:
        techniques = data.retrieve_techniques()

        template = kid.Template(name=os.path.basename(__file__)[:-3], 
                                title=get_text('sitename') + ' - ' + get_text('search'),
                                headline=get_text(os.path.basename(__file__)[:-3]),
                                results=results[1],
                                techs=techniques[1],
                                search_fields=data.data[0].keys(),
                                translate_field=field_language[DEFAULT_LANGUAGE],
                                project_not_found='', 
                                **common_language[DEFAULT_LANGUAGE])
    template.cache = False

    return template.serialize(output='xhtml-strict')
 
