mkdir data
cp ${1} data/train.jsonl
python3.9 reformat_train_to_expected_csv.py
python3.9 tune_summarization.py \
    --model_name_or_path google/mt5-small \
    --do_train \
    --train_file='data/train.csv'\
    --source_prefix "summarize: " \
    --output_dir './model' \
    --per_device_train_batch_size=2 \
    --overwrite_output_dir \
    --fp16
rm -rf data/
