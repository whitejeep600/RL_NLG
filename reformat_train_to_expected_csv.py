import csv
import json

if __name__ == '__main__':
    articles = []
    with open('data/train.jsonl', 'r') as file:
        for line in file:
            articles.append(json.loads(line))
    processed = []
    for article in articles:
        processed.append({'text': article['maintext'],
                          'summary': article['title']})
    with open('data/train.csv', 'w', encoding='utf8') as pred_file:
        writer = csv.writer(pred_file)
        print('text,summary', file=pred_file)
        for article in processed:
            writer.writerow([article["text"], article["summary"]])

    with open('data/train.csv', 'r', encoding='utf8') as pred_file:
        csvreader = csv.reader(pred_file)
        header = next(csvreader)
        rows = []
        for row in csvreader:
            rows.append(row)
            assert len(row) == 2
    assert len(rows) == len(processed)
