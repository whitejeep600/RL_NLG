To run prediction, the following packages are required:

- a source install of transformers (pip install git+https://github.com/huggingface/transformers)
- protobuf, version 3.20 (pip install protobuf==3.20.*)
- datasets
- sentencepiece
- nltk
- torch

To fine-tune, first install another version of the transformers library:

git clone https://github.com/huggingface/transformers.git
cd transformers
git checkout t5-fp16-no-nans
pip install -e .

then call

./tune.sh path/to/train.jsonl

If I understand correctly, it is not required that the training process does not exceed the 8 GiB limit set for run.sh. Indeed the process can go up to 9 GiB (about 8839MiB).
