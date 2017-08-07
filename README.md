# Deep CNN + LSTM siamese network for video similarity


| Expeirment  | Conv Layer | Embedding-Layer | Embedding-Dim | LSTM-layer | LSTM-hidden-dims | l2-reg | batch-size | num-epochs | loss | images | train-accuracy | val-accuracy | train-val-test split| dataset-type| Data-Augmentations | Runtime| learning-rate | 
|-----------| -----------|-----------------|---------------|------------|------------------|--------|-------| ---------- | ---- | ------ | -------------- | ------------ | -------------------| ----------------- |---------------| ------- | ---------- |
| 1a | conv6 | NO | NA | 1 | 10 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_10.pdf)   [loss](images/exp1/loss_10.pdf)| 696/1323 | 82/147 | 1323-147-0 | Full | NO | 1.7 hrs | 1e-3 |
| 1b | conv6 | NO | NA | 1 | 20 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_20.pdf)   [loss](images/exp1/loss_20.pdf) | 724/1323 | 83/147 | 1323-147-0 | Full | NO | 1.7 hrs | 1e-3|
| 1c | conv6 | NO | NA | 1 | 30 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_30.pdf)   [loss](images/exp1/loss_30.pdf) | 712/1323 | 80/147 | 1323-147-0 | Full | NO | 1.7 hrs | 1e-3|
| 1d | conv6 | NO | NA | 1 | 40 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_40.pdf)   [loss](images/exp1/loss_40.pdf) | 704/1323 | 76/147 | 1323-147-0 | Full | NO| 1.7 hrs | 1e-3 |
| 1e | conv6 | NO | NA | 1 | 50 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_50.pdf)   [loss](images/exp1/loss_50.pdf) | 704/1323 | 76/147 | 1323-147-0 | Full | NO | 1.7 hrs | 1e-3|
| 2a | conv6 | YES | 1000 | 3 | 10 | 0.0 | 8 | 6  | contrastive | [accuracy](images/exp2/accuracy_10.pdf)   [loss](images/exp2/loss_10.pdf) | - | - | 1041-116-0 | Simplified | BASIC | 4.5 hrs| 1e-2|
| 2b | conv6 | YES | 1000 | 3 | 50 | 0.0 | 8 | 17 | contrastive | [accuracy](images/exp2/accuracy_50.pdf)  [loss](images/exp2/loss_50.pdf) | - | - | 1041-116-0 | Simplified | INTERMEDIATE | 16hrs | 1e-2 with decay at 100 steps to 0.95x |
| 3a | conv6 | YES | 1000 | 3 | 50 | 0.0 | 8 | 25 | contrastive |  [accuracy](images/exp3/accuracy_3a.pdf)  [loss](images/exp3/loss_3a.pdf) | 704/1042 | 81/115 | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | 9.2hrs | 1e-2 with decay at 200 steps to 0.95x |
| 3b | conv6 | NO | NA | 3 | 50 | 0.0 | 8 | 25 | contrastive |  [accuracy](images/exp3/accuracy_3b.pdf)  [loss](images/exp3/loss_3b.pdf) | 702/1042 | 81/115 | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | 9hrs | 1e-2 with decay at 200 steps to 0.95x |
| 3c | conv6 | NO | NA | 1 | 50 | 0.0 | 8 | 1(online) | contrastive |   | - | - | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | - | 1e-2 with decay at 200 steps to 0.95x |
| 3d | conv6 | YES | 1000 | 1 | 50 | 0.0 | 8 | 25 | contrastive |   | - | - | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | - | 1e-2 with decay at 200 steps to 0.95x |
