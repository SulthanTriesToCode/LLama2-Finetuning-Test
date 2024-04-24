import json

with open('./coedit/validation.jsonl', 'r') as infile, open('validation.jsonl', 'w') as outfile:
    for line in infile:
        data = json.loads(line)
        formatted_text = f'<|user|> {data["src"]} <|assistant|> {data["tgt"]}'
        json.dump({'text': formatted_text}, outfile)
        outfile.write('\n')
