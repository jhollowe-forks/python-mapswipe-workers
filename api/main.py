from typing import Optional

from fastapi import FastAPI

import sys

import csv

import json

app = FastAPI()

'''
Taken from GeeksForGeeks:

https://www.geeksforgeeks.org/convert-csv-to-json-using-python/
'''

@app.get("/api/projectStats/{project_id}")
def read_item(project_id: str):

    maxInt = sys.maxsize

    while True:
        
        try:
            csv.field_size_limit(maxInt)
            break
        
        except OverflowError:
            maxInt = int(maxInt/10)

    data = {}

    output = None


    with open('projects.csv',encoding='utf-8') as csvf:
        
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:

            key = rows['project_id']

            print("key: " + key)

            data[key] = rows

            if key == project_id:

                output = data[key]
            
            print("data[key]: " + str(data[key]))

   
        print(output)

    return {"project_id": output}


