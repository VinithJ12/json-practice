#!/usr/bin/python3


import json 
import csv

with open('chacon.json', 'r') as file:
    data=json.load(file)


with open('chacon.csv', 'w', newline= '') as csvfile:
    writer= csv.writer(csvfile)

    for repo in data[:5]:

        name= repo.get('name')
        html_url= repo.get('html_url')
        updated_at= repo.get('updated_at')
        visibility= repo.get('visibility')
        writer.writerow([name, html_url, updated_at, visibility])
