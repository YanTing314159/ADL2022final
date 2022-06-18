import json
import csv
from tqdm import tqdm
import os
path = "./data/bot_hit_hard_v2/"
jsonl_name = "train_hit_hard_v2.jsonl"

with open(os.path.join(path, "source.csv"), "w") as fs:
    writer_s = csv.writer(fs)
    with open(os.path.join(path, "target.csv"), "w") as ft:
        writer_t = csv.writer(ft)
        
        with open(os.path.join(path, jsonl_name), "r") as f:
            idx = 1
            dialog = [json.loads(line) for line in f]
            
            for d in tqdm(dialog):
            # start with the second utterance from the simulator
                if len(d["dialog"]) > 3:
                    for index in range(1, len(d["dialog"])-2, 2):
                        writer_s.writerow([idx, d["dialog"][index-1], d["dialog"][index+1]])
                        writer_t.writerow([idx, d["dialog"][index]])
                        idx += 1
                else:
                    writer_s.writerow([idx, d["dialog"][0], d["dialog"][2]])
                    writer_t.writerow([idx, d["dialog"][1]])
                    idx += 1