#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Filename:   config.py
Authors:    Han Lin Yap and Alexander Östman
Course:     TDP003 - Projekt: Egna datormiljön
Date:       HT09   - 2009-10-07
Program:    LiU/IP1
Desciption: This is the configuaration file for languages. 
"""

import data

data.init()
projects = data.retrieve_projects()

# Available values: sv
DEFAULT_LANGUAGE = 'sv'

# Language translation in kid-templates
common_language = {'sv':
                {'sitename':'Portfolio',
                 'startpage':'Startsida',
                 'project':'Projekt',
                 'techniques':'Tekniker',
                 'search':u'Sök',
                 'latest_projects':'Senaste projekt',
                 'search_word':u'Sökord',
                 'sort_by':'Sortera efter',
                 'standard':'Standard',
                 'search_by_field':u'Sök i fält',
                 'ascending':'Stigande',
                 'descending':'Fallande',
                 'all':'Alla',
                 'projects_not_found':u'Inga projekt matchade din sökning.',
                 'latest_projects_data':projects[1][:10]
                 } 


}

# In python code translation
base_language = {'sv':
                {'sitename':'Portfolio',
                'projects':'Projekt',
                 'techniques':'Tekniker',
                 'project_not_found':'Projektet hittades inte',
                 'search':u'Sök',
                 'startpage':'Startsida',
                 'database_not_available':u'Databasen är inte tillgänglig'}
}
# CSV fieldnames translation
field_language = {'sv':
                 {'project_no':'Projektnummer',
                  'project_name':'Projektnamn',
                  'start_date':'Startdatum',
                  'end_date':'Slutdatum',
                  'course_id':'Kursnummer',
                  'course_name':'Kursnamn',
                  'academic_credits':u'Högskolepoäng',
                  'techniques_used':'Tekniker',
                  'short_description':'Kort beskrivning',
                  'long_description':u'Lång beskrivning',
                  'small_image':'Liten bild',
                  'big_image':'Stor bild',
                  'group_size':'Gruppstorlek',
                  'external_link':u'Externa länkar'}
    
}

#-- get_text --
#Function description: Get text in default language
#Parameters: word, key to "base language"-dictionary
#Return values: translated word
def get_text(word):
    return base_language[DEFAULT_LANGUAGE][word]
    
