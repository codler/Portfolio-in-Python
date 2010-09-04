#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Filename:   projects.py
Authors:    Han Lin Yap and Alexander Östman
Course:     TDP003 - Projekt: Egna datormiljön
Date:       HT09   - 2009-10-07
Program:    LiU/IP1
Desciption: This is our . FIXME  
"""

import kid
import os
import data
from config import *
kid.enable_import(path=os.path.dirname(__file__) + "/" + "templates")




def index(id=None):
    data.init()

    #default template
    template = kid.Template(name=os.path.basename(__file__)[:-3], 
                                title=get_text('sitename') + '-' + get_text(os.path.basename(__file__)[:-3]), 
                                projects=[],
                                headline=get_text(os.path.basename(__file__)[:-3]),
                                project_not_found=u'Databasen är inte tillgänglig',
                                **common_language[DEFAULT_LANGUAGE])

    if id == None:
        projects = data.retrieve_projects(sort_order='desc');
    
        if projects[0] == 0:
            template = kid.Template(name=os.path.basename(__file__)[:-3], 
                                title=get_text('sitename') + '-' + get_text(os.path.basename(__file__)[:-3]), 
                                projects=projects[1],
                                headline=get_text(os.path.basename(__file__)[:-3]),
                                project_not_found='',
                                **common_language[DEFAULT_LANGUAGE])

    # Find project by id
    else:
        project = data.lookup_project(id)
        # Project not found
        if project[0] == 2:
            projects = data.retrieve_projects(sort_order='desc');
            
            if projects[0] == 0:
                template = kid.Template(name=os.path.basename(__file__)[:-3],
                                        title=get_text('sitename') + '-' + get_text('project_not_found'),
                                        projects=projects[1],
                                        headline=get_text(os.path.basename(__file__)[:-3]),
                                        project_not_found=get_text('project_not_found'),
                                        **common_language[DEFAULT_LANGUAGE])
        # Show project by id
        else:
            project = data.retrieve_projects(search=id,search_fields=['project_no']);
            project[1][0]['techniques_used'] = ", ".join(project[1][0]['techniques_used'])
            template = kid.Template(name='projectsbyid', 
                                    title=get_text('sitename') + 
                                    '-' + 
                                    get_text('projects') + 
                                    ": " +
                                    project[1][0]['project_name'],
                                    headline=project[1][0]['project_name'],
                                    **dict(project[1][0],**common_language[DEFAULT_LANGUAGE]))
    
    template.cache = False

    return template.serialize(output='xhtml-strict')
