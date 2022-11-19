To run prediction, the following packages are required:

- a source install of transformers (pip install git+https://github.com/huggingface/transformers)
- protobuf, version 3.20 (pip install protobuf==3.20.*)
- datasets
- sentencepiece
- nltk
- torch

To fine-tune (with the same packages available), call

./tune.sh path/to/train.jsonl
