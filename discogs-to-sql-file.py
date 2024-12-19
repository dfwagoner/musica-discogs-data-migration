# This script queries my discogs collection and writes the data as sql insert statements to a text file.

import os
import requests
import json
import time

url = 'https://api.discogs.com/users/dwagoner/collection/folders/0/releases?sort=artist&page=1&per_page=50'
token = os.getenv("DISCOGS_TOKEN")
headers = {"Authorization": "Discogs token=" + token}
response = requests.get(url, headers=headers)
raw_json = response.json()

totalpages = (raw_json['pagination']['pages'])

print ("Starting...")

for p in range(1, totalpages + 1):
    url = str('https://api.discogs.com/users/dwagoner/collection/folders/0/releases?sort=artist&page=' + str(p) + '&per_page=50')
    response = requests.get(url, headers=headers)
    raw_json = response.json()   
    items_on_current_page = (len(raw_json['releases']))
    
    for i in range(items_on_current_page):
        with open('discogs_data_sql.sql', mode='a', newline='\n') as f:
            if len(raw_json['releases'][i]['notes'])==3:
                with open('discogs_data_sql.sql', mode='a', newline='\n') as f:
                    f.write('INSERT INTO discogs_data VALUES (' + 
                    str(raw_json['releases'][i]['id']) + ", " + 
                    str(raw_json['releases'][i]['instance_id']) + ", " + 
                    str(raw_json['releases'][i]['basic_information']['artists'][0]['id']) + ", " +  "'" +  
                    raw_json['releases'][i]['basic_information']['title'].replace("\"", "'").replace("'", "\\'") + "'" + ", " +  "'" + 
                    raw_json['releases'][i]['basic_information']['artists'][0]['name'].replace("\"", "'").replace("'", "\\'") + "'" + ", " +  
                    str(raw_json['releases'][i]['basic_information']['year']) + ", " + str(raw_json['releases'][i]['rating']) + ", " + "'" + 
                    raw_json['releases'][i]['notes'][2]['value'].replace("\"", "'").replace("'", "\\'") + "'" + ", " + "NULL, " + "NULL" + ");\n")
                    time.sleep(.005)              
            else:
                    f.write('INSERT INTO discogs_data VALUES (' +
                    str(raw_json['releases'][i]['id']) + ", " + 
                    str(raw_json['releases'][i]['instance_id']) + ", " + 
                    str(raw_json['releases'][i]['basic_information']['artists'][0]['id']) + ", " +  "'" +  
                    raw_json['releases'][i]['basic_information']['title'].replace("\"", "'").replace("'", "\\'") + "'" + ", " +  "'" + 
                    raw_json['releases'][i]['basic_information']['artists'][0]['name'].replace("\"", "'").replace("'", "\\'") + "'" + ", " +  
                    str(raw_json['releases'][i]['basic_information']['year']) + ", " + str(raw_json['releases'][i]['rating']) + ", " + 
                    "'', " + "NULL, " + "NULL" + ");\n")     
                    time.sleep(.005)

print("Finished.")