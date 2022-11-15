python3.9 tune_summarization.py \
    --model_name_or_path './model_fp16' \
    --do_predict \
    --predict_with_generate \
    --test_file='data/test.csv'\
    --source_prefix "summarize: " \
    --output_dir 'data/predictions' \
    --decoder='beam_search' \
    --beam_size=3 \
    --generation_max_length=64 \
    --per_device_eval_batch_size=1 \
    --overwrite_output_dir \
    --fp16 \
    --eval_accumulation_steps=2 \
    --summary_column='text'