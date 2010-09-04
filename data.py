#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Filename:   data.py
Authors:    Han Lin Yap and Alexander Östman
Course:     TDP003 - Projekt: Egna datormiljön
Date:       HT09   - 2009-10-11
Program:    LiU/IP1
Desciption: This is our datalayer. 
"""

#imported modules
import csv,operator,time,os

#global variables
data = []
errorCode = 1

#-- init --
#Function description: Reads data from a file, converting it to Unicode
#Parameters: None
#Return values: None 
def init():
    global errorCode
    global data
    data = []

    try:
        csvReader = csv.reader(open(os.path.dirname(__file__)+'/data.csv','r'))
        fieldNames = csvReader.next()

        for row in csvReader:
            field = {}
            for fieldName in fieldNames:

                index = fieldNames.index(fieldName)
                if not row[index].isdigit():
                    if len(row[index]) == 0:
                        field[fieldName] = None
                    else:
                        field[fieldName] = unicode(row[index],'utf-8')
                else:
                    field[fieldName] = int(row[index])

            data.append(field)
        # Convert project_name to always be a string
        for row in data:
            row['project_name'] = unicode(str(row['project_name']),'utf-8')
            if row['techniques_used'] != None:
                row['techniques_used'] = row['techniques_used'].split(',')
                if len(row['techniques_used']) > 1:
                    row['techniques_used'].sort()
            else:
                row['techniques_used'] = []

        errorCode = 0
            
    except IOError:
        errorCode = 1 
    access_log("Calling function init()")

#-- project count --
#Function description: Counting the number of projects in "data"
#Parameters: None
#Return values: Error code as integer, number of projects as integer inside a tuple
def project_count():
    global errorCode

    if errorCode != 1:
        errorCode = 0
 
    access_log("Calling function project_count(), return: " + str(len(data)))
    return (errorCode,len(data))

#-- lookup_project --
#Function description: looking up a projects based on project id.
#Parameters: id - the unique project number as integer
#Return values: Error code as integer, project as a list inside a tuple
def lookup_project(id):
    global errorCode
    project = {}
    id = int(id)
    # Get project info by id
    for row in data:
        if row['project_no'] == id:
            project = row
            break

    if len(project) == 0:
        errorCode = 2
        project = None
    access_log("Calling function lookup_project(), args: id=" + str(id))
    return (errorCode,project)

#-- retrieve_project --
#Function description: "searching" after a project after certain criterias and sort it
#Parameters:
#   sort_by (predefined) - determines the column feature to sort by
#   sort_order (predefined) - determines if the the column shall be sorted ascending or decending
#   techniques (predefined) - selecting projects based on a certain technique
#   search (predefined) - phrase to search by
#   search_field (predefined) - selecting which "field" to search in
#Return values: Error code as integer, project as a list inside a tuple
def retrieve_projects(sort_by='start_date', sort_order = "asc", techniques=None, search = None, search_fields = None):
    global errorCode

    access_log("Calling function retrieve_projects(), args: sort_by=%s,sort_order=%s,techniques=%s,search=%s,search_fields=%s" % (sort_by,sort_order,techniques,search,search_fields))

    if search == None:
        search = ''
    if type(search) != type(2):
        search = unicode(search,'utf-8')
        search = search.lower()

    if techniques == []:
        techniques = None
    searchData = []

    for row in data:
        if search_fields != None:
            searchFields = search_fields
        else:
            searchFields = row
        #search_field
        foundMatch = False
        for field in searchFields:
            # search word
            if type(row[field]) == type(u''):
                if row[field].lower().find(search) != -1:
                    foundMatch = True
            elif search.isdigit() and row[field] == int(search):
                foundMatch = True
        if foundMatch:
            # technique
            if techniques != None:
                techniquesCount = len(techniques)
                for technique in techniques:
                    if row['techniques_used'].count(unicode(technique,'utf-8')) > 0:
                        techniquesCount -= 1
                if techniquesCount == 0:
                    searchData.append(row)
            else:
                searchData.append(row)
            
            errorCode = 0

    # Sort
    if sort_order == "desc":
        searchData = sorted(searchData,key=operator.itemgetter(sort_by),reverse=True)
    else:
        searchData = sorted(searchData,key=operator.itemgetter(sort_by),reverse=False)

    return (errorCode, searchData)

#-- retrive_techniques --
#Function description: retrieve all the techniques used in any projects
#Parameters: None
#Return values: Error code as integer, list of techniques inside a tuple
def retrieve_techniques():
    global errorCode

    techniquesList = []
    for row in data:
        if row['techniques_used'] != []:
            techniquesList += row['techniques_used']
    
    # Filter techniquesList so it have only unique techniques in the list
    for word in techniquesList:
        while techniquesList.count(word) > 1:
            techniquesList.remove(word)
        
    try:
        techniquesList.remove('')
    except:
        pass

    techniquesList.sort()

    if errorCode != 1:
        errorCode = 0
    access_log("Calling function retrieve_techniques()")
    return (errorCode, techniquesList)
    

#-- retrive_technique_stats --
#Function description: retrieve stats of techniques used in any projects
#Parameters: None
#Return values: Error code as integer, techniqueStats - (statistics of techniques) as dictionary, inside a tuple
def retrieve_technique_stats():
    # Get all unique techniques
    techniquesList = retrieve_techniques()[1]
    techniqueStats = []

    for technique in techniquesList:
        numberOfProjects = 0
        projects = []

        for row in data:
            if row['techniques_used'].count(technique) > 0:
                numberOfProjects += 1
                projects.append({'id':row['project_no'],'name':row['project_name']})

        projects = sorted(projects,key=operator.itemgetter('name'),reverse=False)
        tech = {'name':technique,'count':numberOfProjects,'projects':projects}
        techniqueStats.append(tech)

    access_log("Calling function retrieve_techniques_stats()")
    return (errorCode, techniqueStats)

#-- access_log --
#Function description: Logging all functions call and certain outdata
#Parameters: Text which shall be written to the logfile
#Return values: None
def access_log(text):
    global errorCode
    text = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + " Code: " + str(errorCode) + " " + text + "\n"
    f = open(os.path.dirname(__file__)+"/logfile.log", "a")
    f.writelines(text)
    f.close()
    
