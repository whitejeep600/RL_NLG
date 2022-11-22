# I used this program to reformat the predictions generated for their respective checkpoints to the expected submission format. Then I ran eval.py from the ADL22-HW3 repository to get ROUGE scores.

import json

if __name__ == '__main__':
    articles = []
    with open('../data/summarization/public.jsonl', 'r') as file:
        for line in file:
            articles.append(json.loads(line))
    for name in ['final', 'ckpt_500', 'ckpt_8500', 'ckpt_16500', 'ckpt_24500']:
        with open('../data/outputs/' + name + '/generated_predictions.txt', 'r') as file:
            predictions = file.readlines()
        assert len(predictions) == len(articles)
        with open('../data/outputs/' + name + '.json', 'w', encoding='utf8') as file:
            for article, prediction in zip(articles, predictions):
                pair = {"title": prediction, "id": article['id']}
                file.write(json.dumps(pair))
                file.write("\n")

