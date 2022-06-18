# ADL2022final
## 訓練
取得訓練資料
`bash run_sim.sh`
前處理
`python to_csv.py`
`python write_csv.py`
訓練
`bash train.sh`
## 測試
`bash run_sim_test.sh`
`python hti.py --prediction <...>`

### 備註
路徑相關參數目前還是直接寫死在檔案裡，有需要自行修改。