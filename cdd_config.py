# cdd_config.py
# configuration settings for code_doc_data
import os

# fill this out for database logging
database = 'localhost'
username = 'username'
password = 'hunter2'

# fill this out for logging to CSV files
csv_folder = os.getcwd()   


# Data Structures (note - tables are filenames for file logging)
tableList = [
    'cddProject',
    'cddProcess',
    'cddEvents'
    ]

    
    