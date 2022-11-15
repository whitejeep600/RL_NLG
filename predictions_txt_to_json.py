import json

if __name__ == '__main__':
    articles = []
    with open('data/test.jsonl', 'r') as file:
        for line in file:
            articles.append(json.loads(line))
    with open('data/predictions/generated_predictions.txt', 'r') as file:
        predictions = file.readlines()
    pass
    assert len(predictions) == len(articles)
    with open('data/result.jsonl', 'w', encoding='utf8') as file:
        for article, prediction in zip(articles, predictions):
            pair = {"title": prediction, "id": article['id']}
            file.write(json.dumps(pair))
            file.write("\n")

