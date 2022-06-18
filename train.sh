#bin/bash
python train.py \
--model_name_or_path "/home/yantingye/ytye/HWs/ADL_final/runs/v1_hit_hard/" \
--dataset_root "/home/yantingye/ytye/HWs/ADL_final/data/bot_hit_hard_v2/" \
--output_dir "runs/v2_hit_hard" \
--max_epoch 10 \
--train_bsize 16 \
--eval_bsize 16 \
