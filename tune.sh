python3.9 tune_summarization.py \
    --model_name_or_path google/mt5-small \
    --do_train \
    --train_file='data/train.csv'\
    --source_prefix "summarize: " \
    --output_dir './model_fp16' \
    --per_device_train_batch_size=2 \
    --overwrite_output_dir \
    --fp16
