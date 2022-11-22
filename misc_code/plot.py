import json
import matplotlib
from pathlib import Path

from matplotlib.pyplot import show, savefig


def get_rouge(name):
    evaluation = json.loads(Path('../../ADL22-HW3/evaluation/' + name + '.txt').read_text())
    return evaluation['rouge-l']['f']


if __name__ == '__main__':
    names = ['ckpt_500', 'ckpt_8500', 'ckpt_16500', 'ckpt_24500', 'final']
    rouges = [get_rouge(name) for name in names]

    matplotlib.pyplot.plot(names, rouges)
    matplotlib.pyplot.title("ROUGE-L per checkpoint")
    savefig('train_rouges.png')
    show()



