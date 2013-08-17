# cdd_config.py
# configuration settings for code_doc_data

# fill this out for database logging
database = 'localhost'
username = 'username'
password = 'hunter2'

# fill this out for logging to CSV files
csv_folder = ''   


# Data Structures (note - tables are filenames for file logging)
tableList = [
    'cddProject',
    'cddProcess',
    'cddEvents'
    ]

from collections import namedtuple

# make a basic Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])

# list of Links to work with
links = [
    Link(0, 60398, 1334014208.0, 109,
         "C overtakes Java as the No. 1 programming language in the TIOBE index.",
         "http://pixelstech.net/article/index.php?id=1333969280"),
    Link(1, 60254, 1333962645.0, 891,
         "This explains why technical books are all ridiculously thick and overpriced",
         "http://prog21.dadgum.com/65.html")
]

def TestNamedTuple():
    # self test function - temp
    for link in links:
        #print ( link )
        if link.id == 1:
            print ('link 1 has the following votes = ', link.votes)

    
    