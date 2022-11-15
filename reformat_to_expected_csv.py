import csv
import json

if __name__ == '__main__':
    articles = []
    with open('data/test.jsonl', 'r') as file:
        for line in file:
            articles.append(json.loads(line))
    processed = []
    for article in articles:
        processed.append({'text': article['maintext']})
    with open('data/test.csv', 'w', encoding='utf8') as pred_file:
        writer = csv.writer(pred_file)
        print('text', file=pred_file)
        for article in processed:
            writer.writerow([article['text']])



