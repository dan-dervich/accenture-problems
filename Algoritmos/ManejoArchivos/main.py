import csv
import json
import os

cwd = os.getcwd()
input_file_path = cwd + "/archivos/input.txt"
output_file_path = cwd + "/archivos/output.txt"

with open(input_file_path, "r") as input_file:
    content = input_file.read()

with open(output_file_path, "w") as output_file:
    output_file.write(content)

with open(input_file_path, "r") as input_file:
    content = input_file.read()
    words = content.split()
    print(len(words))
    

with open(cwd + "/archivos/annual-enterprise-survey-2021-financial-year-provisional-csv.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
file_paths = [cwd + "/archivos/input.txt", cwd + "/archivos/input1.txt"]
with open(cwd + "/archivos/output2.txt", "w") as output_file:
    for file_path in file_paths:
        with open(file_path, "r") as input_file:
            content = input_file.read()
            output_file.write(content)

file_path = cwd + "/archivos/annual-enterprise-survey-2021-financial-year-provisional-csv.csv"
json_file_path = cwd + "/archivos/annual-enterprise-survey-2021-financial-year-provisional-csv.json"

with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    with open(json_file_path, "w") as json_file:
        json.dump(rows, json_file)
