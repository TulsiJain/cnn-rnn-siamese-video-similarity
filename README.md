# Deep CNN + LSTM siamese network for video similarity


| Exp #  | Conv Layer | Embedding / Projection Layer | Embedding / Projection Dim | Num LSTM-layer | LSTM-hidden-dims | l2-reg | batch-size | num-epochs | loss | images | train-accuracy | val-accuracy | train-val-test split| dataset-type | Data-Augmentations | Runtime| learning-rate | tied-weights | convNet training |
|-----------| -----------|-----------------|---------------|------------|------------------|--------|-------| ---------- | ---- | ------ | -------------- | ------------ | -------------------| ----------------- |---------------| ------- | ---------- | ------ |
| 1a | conv6 | NO | NA | 1 | 10 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_10.pdf)   [loss](images/exp1/loss_10.pdf)| 696/1323 | 82/147 | 1323-147-0 | Full | NO | 1.7 hrs | 1e-3 | NO | YES |
| 1b | conv6 | NO | NA | 1 | 20 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_20.pdf)   [loss](images/exp1/loss_20.pdf) | 724/1323 | 83/147 | 1323-147-0 | Full | NO | 1.7 hrs | 1e-3| NO | YES |
| 1c | conv6 | NO | NA | 1 | 30 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_30.pdf)   [loss](images/exp1/loss_30.pdf) | 712/1323 | 80/147 | 1323-147-0 | Full | NO | 1.7 hrs | 1e-3| NO | YES |
| 1d | conv6 | NO | NA | 1 | 40 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_40.pdf)   [loss](images/exp1/loss_40.pdf) | 704/1323 | 76/147 | 1323-147-0 | Full | NO| 1.7 hrs | 1e-3 | NO | YES |
| 1e | conv6 | NO | NA | 1 | 50 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_50.pdf)   [loss](images/exp1/loss_50.pdf) | 704/1323 | 76/147 | 1323-147-0 | Full | NO | 1.7 hrs | 1e-3| NO | YES |
| 2a | conv6 | YES | 1000 | 3 | 10 | 0.0 | 8 | 6  | contrastive | [accuracy](images/exp2/accuracy_10.pdf)   [loss](images/exp2/loss_10.pdf) | - | - | 1041-116-0 | Simplified | BASIC | 4.5 hrs| 1e-2| NO | NO |
| 2b | conv6 | YES | 1000 | 3 | 50 | 0.0 | 8 | 17 | contrastive | [accuracy](images/exp2/accuracy_50.pdf)  [loss](images/exp2/loss_50.pdf) | - | - | 1041-116-0 | Simplified | INTERMEDIATE | 16hrs | 1e-2 with decay at 100 steps to 0.95x | NO |
| 4a | conv6 | YES | 1000 | 3 | 50 | 0.0 | 8 | 25 | contrastive | [accuracy](images/exp4/accuracy_4a.pdf)  [loss](images/exp4/loss_4a.pdf) | /1041 | /115 | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | 15hrs | 1e-2 with decay at 200 steps to 0.95x | YES | NO | 
| 4b | conv6 | NO | NA | 3 | 50 | 0.0 | 8 | 25 | contrastive |  | | | 1042-115-0| Simplified (Ratio Maintained) | INTERMEDIATE(different) |  | 1e-2 with decay at 200 steps to 0.95x | YES | NO |
| 4c | conv6 | NO | NA | 1 | 50 | 0.0 | 8 | 8 | contrastive | [accuracy](images/exp4/accuracy_4c.pdf)  [loss](images/exp4/loss_4c.pdf) | - | - | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | - | 1e-2 with decay at 200 steps to 0.95x | YES | NO |
| 4d | conv6 | YES | 1000 | 1 | 50 | 0.0 | 8 | 25 | contrastive |   |  |  | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) |  | 1e-2 with decay at 200 steps to 0.95x | YES| NO |
| 4e | conv6 | NO| NA | 3 | 100 | 0.0 | 8 | 9 | contrastive |  [accuracy](images/exp4/accuracy_4e.pdf)  [loss](images/exp4/loss_4e.pdf) | - | - | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | - | 1e-2 with decay at 200 steps to 0.95x | YES| NO |
| 4f | conv6 | YES| 1000 | 1 | 80 | 0.0 | 8 | 4 | contrastive |  [accuracy](images/exp4/accuracy_4f.pdf)  [loss](images/exp4/loss_4f.pdf) | - | - | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | - | 1e-2 with decay at 200 steps to 0.95x | YES| YES |
| 4g | conv6 | NO| NA | 1 | 80 | 0.0 | 8 | 6 | contrastive |  [accuracy](images/exp4/accuracy_4g.pdf)  [loss](images/exp4/loss_4g.pdf) | - | - | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | - | 1e-2 with decay at 200 steps to 0.95x | YES| YES |
| 4h | conv6 | NO| NA | 2 | 80 | 0.0 | 8 | 9 | contrastive |  [accuracy](images/exp4/accuracy_4h.pdf)  [loss](images/exp4/loss_4h.pdf) | - | - | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | - | 1e-2 with decay at 200 steps to 0.95x | YES| YES |


### Some Jargons used above  
* Full --> originally collected dataset (~750 pairs of negative and positve videos each)
* Simplified --> Positive Samples have been refined to pairs in opposite or same directions
* Simplified(Ratio Maintained) --> Positive Samples/Negative Samples ratio maintained in training and validation
* BASIC --> Basic data-augmentation/transformations only
* INTERMEDIATE --> Intermediate level of data-augmentataions/transformations
* INTERMEDIATE(different) --> In a pair of videos both videos transformed seprately.
