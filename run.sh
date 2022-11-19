mkdir data
cp ${1} data/test.jsonl
python3.9 reformat_to_expected_csv.py
./predict.sh
python3.9 predictions_txt_to_json.py
mv data/result.jsonl ${2}
rm -rf data/
