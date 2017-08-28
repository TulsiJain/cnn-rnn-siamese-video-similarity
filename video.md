# Deep CNN + LSTM siamese network for video similarity

[Website for  Visualizing Data](http://10.2.132.196/gta/gta_data.php) (Only visible inside IIIT's network)

Following parameters were fixed
+ Convolutional Networks -- features (pool6 - layer), initialized with amos-Net weights.
+ No-projection-layer
+ lstm layer (with 50 hidden units)
+ batch-size : 4
+ No-data-augmentation
+ Dynamic-LSTM-cells
+ Adam Optimizer
+ Tied Weights in LSTM/CNN
+ NO-regularization
+ Contrastive Loss

| Exp #  |  images | train-accuracy | val-accuracy | positive-negative | weather-type in pair of videos | trajectory-type | learning-rate | convNet training | features from LSTM | Num LSTM Layers| train-val ratio |
|--------| ------- | -------------- | ------------ | -------------------- | ---------------- | ------------ | ------------- | --------- | ---------------- | ----------- | ----- |
| 1a | [accuracy](images/exp1/accuracy_1a.pdf)   [loss](images/exp1/loss_1a.pdf)| 707/707=100% | 77/77=100% | 375/404 | same-weather | same-direction | 1e-5 | NO | CELL-STATE | 1 | 9:1 |
| 2a | [accuracy](images/exp2/accuracy_2a.pdf)   [loss](images/exp2/loss_2a.pdf)| 1011/1011=100% | 111/112=100% | 443/680 | all-weather | same-direction | 1e-5 | NO | CELL-STATE |  1 | 9:1 |
| 2b | [accuracy](images/exp2/accuracy_2b.pdf)   [loss](images/exp2/loss_2b.pdf)| 782/1011=77.3% | 83/112=74% | 443/680 | all-weather | same-direction | 1e-5 | NO |  OUTPUT(LAST Frame) | 1 | 9:1 |
| 2c | [accuracy](images/exp2/accuracy_2c.pdf)   [loss](images/exp2/loss_2c.pdf)| 782/1011=77.3% | 86/112=77% | 443/680 | all-weather | same-direction | 1e-4 | NO |  OUTPUT(LAST Frame) | 1 | 9:1 |
| 2d | [accuracy](images/exp2/accuracy_2d.pdf)   [loss](images/exp2/loss_2d.pdf)| 733/1011=72.5% | 84/112=75% | 443/680 | all-weather | same-direction | 1e-5 | YES |  OUTPUT(LAST Frame) | 1 | 9:1 |
| 2e | [accuracy](images/exp2/accuracy_2e.pdf)   [loss](images/exp2/loss_2e.pdf)| 791/1011=78.2% | 93/112=83% | 443/680 | all-weather | same-direction | 1e-5 | YES |  OUTPUT(LAST Frame) | 3 | 9:1 |
| 3a | [accuracy](images/exp3/accuracy_3a.pdf)   [loss](images/exp3/loss_3a.pdf)| 808/813=100% | 89/89=100% | 498/404 | same-weather | same/overlap-directions | 1e-5 | NO | CELL-STATE | 1 | 9:1 |
| 4a | [accuracy](images/exp4/accuracy_4a.pdf)   [loss](images/exp4/loss_4a.pdf)| 932/937=100% | 101/103=100% | 636/404 | all-weather | same/overlap-directions | 1e-5 | NO | CELL-STATE | 1 | 9:1 |
| 4b | [accuracy](images/exp4/accuracy_4b.pdf)   [loss](images/exp4/loss_4b.pdf)| | | 636/404 | all-weather | same/overlap-directions | 1e-5 | NO | CELL-STATE | 1 | 1:1 |
| 4c | [accuracy](images/exp4/accuracy_4c.pdf)   [loss](images/exp4/loss_4c.pdf)| | | 636/404 | all-weather | same/overlap-directions | 1e-5 | NO | CELL-STATE | 1 | 1:9 |
| 4d | [accuracy](images/exp4/accuracy_4d.pdf)   [loss](images/exp4/loss_4d.pdf)| | | 636/404 | all-weather | same/overlap-directions | 1e-5 | NO | CELL-STATE | 1 | 1:3 |
| 4e | [accuracy](images/exp4/accuracy_4e.pdf)   [loss](images/exp4/loss_4e.pdf)| | | 636/404 | all-weather | same/overlap-directions | 1e-5 | NO | CELL-STATE | 1 | 3:2 |
| 4f | [accuracy](images/exp4/accuracy_4f.pdf)   [loss](images/exp4/loss_4f.pdf)| | | 636/404 | all-weather | same/overlap-directions | 1e-5 | NO | HIDDEN-STATE | 1 | 9:1 |
| 5a | [accuracy](images/exp5/accuracy_5a.pdf)   [loss](images/exp5/loss_5a.pdf)| 501/501=100% | 55/55=100% | 152/404 | same-weather | inverse-direction | 1e-5 | NO | CELL-STATE | 1 | 9:1 |
| 6a | [accuracy](images/exp6/accuracy_6a.pdf)   [loss](images/exp6/loss_6a.pdf)| 502/502=100% | 52/55=95% | 153/404 | all-weather | inverse-direction | 1e-5 | NO | CELL-STATE | 1 | 9:1 |
| 7a | [accuracy](images/exp7/accuracy_7a.pdf)   [loss](images/exp7/loss_7a.pdf)| 612/612=100% | 67/67=100% | 275/404 | same-weather | inverse/overlap-direction | 1e-5 | NO | CELL-STATE | 1 | 9:1 |
| 8a | [accuracy](images/exp8/accuracy_8a.pdf)   [loss](images/exp8/loss_8a.pdf)| 635/635=100% | 70/70=95% | 301/404 | all-weather | inverse/overlap-direction | 1e-5 | NO | CELL-STATE | 1 | 9:1 |
| 9a | [accuracy](images/exp9/accuracy_9a.pdf)   [loss](images/exp9/loss_9a.pdf)|  |  |  | all-weather | all-directions | 1e-5 | NO | CELL-STATE | 1 | 9:1 |




<!---
| Exp #  | Conv Layer | Embedding / Projection Layer | Embedding / Projection Dim | Num LSTM-layer | LSTM-hidden-dims | l2-reg | batch-size | num-epochs | loss | images | train-accuracy | val-accuracy | train-val-test split| dataset-type | Data-Augmentations | Runtime| learning-rate | tied-weights | convNet training |
|-----------| -----------|-----------------|---------------|------------|------------------|--------|-------| ---------- | ---- | ------ | -------------- | ------------ | -------------------| ----------------- |---------------| ------- | ---------- | ------ |
| 1a | conv6 | NO | NA | 1 | 10 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_10.pdf)   [loss](images/exp1/loss_10.pdf)| 696/1323=53% | 82/147=55% | 1323-147-0 | Full | NO | 1.7 hrs | 1e-3 | NO | YES |
| 1b | conv6 | NO | NA | 1 | 20 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_20.pdf)   [loss](images/exp1/loss_20.pdf) | 724/1323 | 83/147 | 1323-147-0 | Full | NO | 1.7 hrs | 1e-3| NO | YES |
| 1c | conv6 | NO | NA | 1 | 30 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_30.pdf)   [loss](images/exp1/loss_30.pdf) | 712/1323=53.8 | 80/147=54.5% | 1323-147-0 | Full | NO | 1.7 hrs | 1e-3| NO | YES |
| 1d | conv6 | NO | NA | 1 | 40 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_40.pdf)   [loss](images/exp1/loss_40.pdf) | 704/1323=31% | 76/147=51.7% | 1323-147-0 | Full | NO| 1.7 hrs | 1e-3 | NO | YES |
| 1e | conv6 | NO | NA | 1 | 50 | 0.0 | 8 | 10 | AAAI,16 | [accuracy](images/exp1/accuracy_50.pdf)   [loss](images/exp1/loss_50.pdf) | 704/1323=31% | 76/147=52% | 1323-147-0 | Full | NO | 1.7 hrs | 1e-3| NO | YES |
| 2a | conv6 | YES | 1000 | 3 | 10 | 0.0 | 8 | 6  | contrastive | [accuracy](images/exp2/accuracy_10.pdf)   [loss](images/exp2/loss_10.pdf) | - | - | 1041-116-0 | Simplified | BASIC | 4.5 hrs| 1e-2| NO | NO |
| 2b | conv6 | YES | 1000 | 3 | 50 | 0.0 | 8 | 17 | contrastive | [accuracy](images/exp2/accuracy_50.pdf)  [loss](images/exp2/loss_50.pdf) | - | - | 1041-116-0 | Simplified | INTERMEDIATE | 16hrs | 1e-2 with decay at 100 steps to 0.95x | NO |
| 4a | conv6 | YES | 1000 | 3 | 50 | 0.0 | 8 | 25 | contrastive | [accuracy](images/exp4/accuracy_4a.pdf)  [loss](images/exp4/loss_4a.pdf) | - | - | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | 15hrs | 1e-2 with decay at 200 steps to 0.95x | YES | NO | 
| 4b | conv6 | NO | NA | 3 | 50 | 0.0 | 8 | 25 | contrastive |  [accuracy](images/exp4/accuracy_4b.pdf)  [loss](images/exp4/loss_4b.pdf) | - | - | 1042-115-0| Simplified (Ratio Maintained) | INTERMEDIATE(different) | - | 1e-2 with decay at 200 steps to 0.95x | YES | NO |
| 4c | conv6 | NO | NA | 1 | 50 | 0.0 | 8 | 8 | contrastive | [accuracy](images/exp4/accuracy_4c.pdf)  [loss](images/exp4/loss_4c.pdf) | - | - | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | - | 1e-2 with decay at 200 steps to 0.95x | YES | NO |
| 4e | conv6 | NO| NA | 3 | 100 | 0.0 | 8 | 9 | contrastive |  [accuracy](images/exp4/accuracy_4e.pdf)  [loss](images/exp4/loss_4e.pdf) | - | - | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | - | 1e-2 with decay at 200 steps to 0.95x | YES| NO |
| 4f | conv6 | YES| 1000 | 1 | 80 | 0.0 | 8 | 4 | contrastive |  [accuracy](images/exp4/accuracy_4f.pdf)  [loss](images/exp4/loss_4f.pdf) | - | - | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | - | 1e-2 with decay at 200 steps to 0.95x | YES| YES |
| 4g | conv6 | NO| NA | 1 | 80 | 0.0 | 8 | 6 | contrastive |  [accuracy](images/exp4/accuracy_4g.pdf)  [loss](images/exp4/loss_4g.pdf) | - | - | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | - | 1e-2 with decay at 200 steps to 0.95x | YES| YES |
| 4h | conv6 | NO| NA | 2 | 80 | 0.0 | 8 | 9 | contrastive |  [accuracy](images/exp4/accuracy_4h.pdf)  [loss](images/exp4/loss_4h.pdf) | - | - | 1042-115-0 | Simplified (Ratio Maintained) | INTERMEDIATE(different) | - | 1e-2 with decay at 200 steps to 0.95x | YES| YES |
| 5a | conv6 | YES| 1000 | 3 | 50 | 0.0 | 8 | 25 | contrastive |  [accuracy](images/exp5/accuracy_5a.pdf)  [loss](images/exp5/loss_5b.pdf) | 702/878=80% | 78/98=80% | 878-97-0 | Ultra Simplified (Ratio Maintained) | INTERMEDIATE(different) | 7.5hrs | 1e-2 with decay at 200 steps to 0.95x | YES| YES |
| 5b | conv6 | YES| 1000 | 3 | 250 | 0.0 | 8 | 25 | contrastive |  [accuracy](images/exp5/accuracy_5a.pdf)  [loss](images/exp5/loss_5b.pdf) | 650/947=69% | 76/105=72% | 947-105-0 | Ultra Simplified (Ratio Maintained) | INTERMEDIATE(different) | 6hrs | 1e-2 with decay at 200 steps to 0.95x | YES| YES |


### Some Jargons used above  
* Full -> originally collected dataset (~750 pairs of negative and positve videos each)
* Simplified -> Positive Samples have been refined to pairs in opposite or same directions
* Simplified(Ratio Maintained) -> Positive Samples/Negative Samples ratio maintained in training and validation
* UltraSimplified(Ratio Maintained) -> Only same direction videos as hosted on website 
* BASIC -> Basic data-augmentation/transformations only
* INTERMEDIATE -> Intermediate level of data-augmentataions/transformations
* INTERMEDIATE(different) -> In a pair of videos both videos transformed seprately.

-->