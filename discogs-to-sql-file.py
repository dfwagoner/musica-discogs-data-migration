# This script queries my discogs collection and writes the data as sql insert statements to a text file.
# I backed this up to the older-scripts folder and then re-named it 

import os
import requests
import json

url = 'https://api.discogs.com/users/dwagoner/collection/folders/0/releases?sort=artist&page=0&per_page=50'
token = os.getenv("DISCOGS_TOKEN")
#url = 'https://api.discogs.com/users/dwagoner/collection/folders/0/releases?sort=artist'
headers = {"Authorization": "Discogs token=" + token}

 

response = requests.get(url, headers=headers)
raw_json = response.json()



#for help, watch the "Dictionaries in Python" (lesson 23) in the Udemy python class, at around 6:00
#print(json_string)
#print(raw_json['releases'][0]['instance_id'])
#print(raw_json)

#create pagination variables
totalpages = (raw_json['pagination']['pages'])
totalitems = (raw_json['pagination']['items'])
per_page = (raw_json['pagination']['per_page'])
print("total pages= " + str(totalpages))
print("total items= " + str(totalitems))

remainder = totalitems % per_page
print(remainder)
#you stopped here


#pagination_enum = raw_json
#for i in range(totalpages):
#    print(i + 1)

	
for p in range(totalpages-1):
    url = str('https://api.discogs.com/users/dwagoner/collection/folders/0/releases?sort=artist&page=' + str(p) + '&per_page=50')
    headers = {"Authorization": "Discogs token=" + token}
    response = requests.get(url, headers=headers)
    raw_json = response.json()   
    #print("p is " + str(p))

    for i in range(50):
        with open('discogs_data_sql.txt', mode='a', newline='\n') as f:
            if len(raw_json['releases'][i]['notes'])==3:
                with open('discogs_data_sql.txt', mode='a', newline='\n') as f:
                    f.write('INSERT INTO discogs_data VALUES (' + 
                    str(raw_json['releases'][i]['id']) + ", " + 
                    str(raw_json['releases'][i]['instance_id']) + ", " + 
                    str(raw_json['releases'][i]['basic_information']['artists'][0]['id']) + ", " +  "\"" +  
                    raw_json['releases'][i]['basic_information']['title'].replace('"', "'") + "\"" + ", " +  "\"" + 
                    raw_json['releases'][i]['basic_information']['artists'][0]['name'].replace('"', "'") + "\"" + ", " +  
                    str(raw_json['releases'][i]['basic_information']['year']) + ", " + str(raw_json['releases'][i]['rating']) + ", " + "\"" + 
                    raw_json['releases'][i]['notes'][2]['value'] + "\"" + ", " + "\"\"" + ", " + "\"\"" + ")\n")              
            else:
                    f.write('INSERT INTO discogs_data VALUES (' +
                    str(raw_json['releases'][i]['id']) + ", " + 
                    str(raw_json['releases'][i]['instance_id']) + ", " + 
                    str(raw_json['releases'][i]['basic_information']['artists'][0]['id']) + ", " +  "\"" +  
                    raw_json['releases'][i]['basic_information']['title'].replace('"', "'") + "\"" + ", " +  "\"" + 
                    raw_json['releases'][i]['basic_information']['artists'][0]['name'].replace('"', "'") + "\"" + ", " +  
                    str(raw_json['releases'][i]['basic_information']['year']) + ", " + str(raw_json['releases'][i]['rating']) + ", " + 
                    "\"\"" +  ", " + "\"\"" + ", " + "\"\"" + ")\n")     

    url = str('https://api.discogs.com/users/dwagoner/collection/folders/0/releases?sort=artist&page=' + str(totalpages) + '&per_page=50')
    headers = {"Authorization": "Discogs token=" + token}
    response = requests.get(url, headers=headers)
    raw_json = response.json()   
    #print("p is " + str(p))

#now do the final page
    #print("Length of final page: " + str(len(raw_json['releases'])))
    for i in range(remainder):
        with open('discogs_data_sql.txt', mode='a', newline='\n') as f:
            if len(raw_json['releases'][i]['notes'])==3:
                with open('discogs_data_sql.txt', mode='a', newline='\n') as f:
                    f.write('INSERT INTO discogs_data VALUES (' + 
                    str(raw_json['releases'][i]['id']) + ", " + 
                    str(raw_json['releases'][i]['instance_id']) + ", " + 
                    str(raw_json['releases'][i]['basic_information']['artists'][0]['id']) + ", " +  "\"" +  
                    raw_json['releases'][i]['basic_information']['title'].replace('"', "'") + "\"" + ", " +  "\"" + 
                    raw_json['releases'][i]['basic_information']['artists'][0]['name'].replace('"', "'") + "\"" + ", " +  
                    str(raw_json['releases'][i]['basic_information']['year']) + ", " + str(raw_json['releases'][i]['rating']) + ", " + "\"" + 
                    raw_json['releases'][i]['notes'][2]['value'] + "\"" + ", " + "\"\"" + ", " + "\"\"" + ")\n") 
                    #print((raw_json['releases'][i]['basic_information']['title']).replace('"', "'"))
   
            else:
                    f.write('INSERT INTO discogs_data VALUES (' +
                    str(raw_json['releases'][i]['id']) + ", " + 
                    str(raw_json['releases'][i]['instance_id']) + ", " + 
                    str(raw_json['releases'][i]['basic_information']['artists'][0]['id']) + ", " +  "\"" +  
                    raw_json['releases'][i]['basic_information']['title'].replace('"', "'") + "\"" + ", " +  "\"" + 
                    raw_json['releases'][i]['basic_information']['artists'][0]['name'].replace('"', "'") + "\"" + ", " +  
                    str(raw_json['releases'][i]['basic_information']['year']) + ", " + str(raw_json['releases'][i]['rating']) + ", " + 
                    "\"\"" + ", " + "\"\"" + ", " + "\"\"" + ")\n")     


        #print(dict1)
        #print("i is " + str(i))
     


#print(#text.replace('"'raw_json['releases'][i]['basic_information']['title']
