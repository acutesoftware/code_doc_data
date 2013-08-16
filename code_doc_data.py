# code_doc_data.py  written by Duncan Murray 14/8/2013 (C) Acute Software
# This is the python implementation of code_doc_data which allows you to
# automatically add documentation to a database (or CSV file) of your batch
# processes.
#   --- SETUP ---
#   # edit the cdd_config.py to chose how to keep logged information
#
#   --- USAGE DURING BATCH PROCESS ---
#   import code_doc_data as cdd
#   cdd.InitProject('TEST', 'Test project to see how it works', '')
#   cdd.CopyFile ('test.doc', 'test_backup.doc', 0)
#   # remaining batch process (ETL load, file transfers, web downloads)
#
#  --- REPORTING ---

import cdd_config
import os, sys, csv

def InitProject(proj_id, proj_name, srcFolder):
    # initialise the database / folder for a new project
    # this wipes existing data for 'proj_id' to allow the 
    # batch process in your code to reenter the details
    # with updated metadata
    # DELETE FROM dataStore WHERE database.proj_id = proj_id
    # INSERT INTO dataStore.listOfProjects (proj_id, proj_name, srcFolder)
    pass

def CopyFile(src, dst, verify=1):
    # copies a file, and logs the details
    # shutil.copyfile(src, dst)                             # do the file copy
    # todo                                                  # verify if needed
    # dataStore.fileCopies.Add(fname, srcPath, destPath)    # log the file copy
    pass
    
def LoadData(csvFile, dataStore):
    # load a csv file to a database
    pass

def SaveData(logMethod, proj, title, comment):
    if logMethod == 'FILE':
        pass
    elif logMethod == 'DATABASE':
        pass
    