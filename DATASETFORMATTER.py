import json

# The first opens the source dataset, the second saves the modified dataset.
with open('./data_en.jsonl', 'r') as infile, open('clean.jsonl', 'w') as outfile:
    for line in infile:
        data = json.loads(line)
        # Change "Question" to the question column, and change "llama2-7b-chat_response" to the column that has the answer.
        formatted_text = f'<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n {data["question"]} <|eot_id|>\n <|start_header_id|>assistant<|end_header_id|>\n {data["llama2-7b-chat_response"]} <|eot_id|>'
        json.dump({'text': formatted_text}, outfile)
        outfile.write('\n')
