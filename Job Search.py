import csv
import requests
import pandas as pd
import json
from itertools import chain


response = requests.get(
    'https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=53632e0e&app_key=c8bdbb41ad1981780266399065dd8630&results_per_page=1000&what=associate%20associates&what_and=remote%20troubleshoot&what_or=associate%20associates%20troubleshoot&max_days_old=3&sort_by=date', 
    headers={'Accept': 'application/json'},
    )
    

data = response.json()



#function to find nested dictionary keys in json data
def recursive_items(dictionary):
    for key, value in dictionary.items():

        if type(value) is list and len(value) > 0 and type(value[0]) is dict:
            yield from recursive_items(value[0])
        
        else:
            yield (key, value)


    



for posting in data['results']:
    
    print(f"Company: {posting['company']['display_name']}")
    print(f"Job title: {posting['title']}")
    print(f"Salary minimum: {posting['salary_min']}")
    print(f"Date Created: {posting['created']}")
    print()
    print(f"Description: {posting['description']}")
    print(posting['redirect_url'])
    print()
    print()
    print()
    print()
    
    #function call to check for nested keys in in results dictionary
    #for key, value in recursive_items(posting):
        #print(key, end='\n\n\n\n\n\n\n\n\n\n')
        

    

