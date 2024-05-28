import csv
import json

def csv_to_jsonl(csv_file, jsonl_file):
  with open(csv_file, 'r', encoding='utf-8') as file:  # Specify the encoding as 'utf-8'
    reader = csv.DictReader(file)
    with open(jsonl_file, 'w') as outfile:
      for row in reader:
        json.dump(row, outfile)
        outfile.write('\n')

# Usage example
csv_to_jsonl('./do-not-answer/data_en.csv', './data_en.jsonl')
