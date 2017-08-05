# Deep CNN + LSTM siamese network for video similarity


| Expeirment  | Conv Layer | Embedding-Layer | Embedding-Dim | LSTM-layer | LSTM-hidden-dims | l2-reg | batch-size | num-epochs | loss | images | train-accuracy | val-accuracy | train-val-test split| dataset-type|
|-----------| -----------|-----------------|---------------|------------|------------------|--------|------------| ---------- | ---- | ------ | -------------- | ------------ | -------------------| ------------ |
| 1a | conv6 | NO | NA | 1 | 10 | 0.0 | 8 | 10 | AAAI,16 | - | - | - | 1323-147-0 | Full |
| 1b | conv6 | NO | NA | 1 | 20 | 0.0 | 8 | 10 | AAAI,16 | - | - | - | 1323-147-0 | Full |
| 1c | conv6 | NO | NA | 1 | 30 | 0.0 | 8 | 10 | AAAI,16 | - | - | - | 1323-147-0 | Full |
| 1d | conv6 | NO | NA | 1 | 40 | 0.0 | 8 | 10 | AAAI,16 | - | - | - | 1323-147-0 | Full |
| 1e | conv6 | NO | NA | 1 | 50 | 0.0 | 8 | 10 | AAAI,16 | - | - | - | 1323-147-0 | Full |
|-----------| -----------|-----------------|---------------|------------|------------------|--------|------------| ---------- | ---- | ------ | -------------- | ------------ | -------------------| ------------ |
| 2a | conv6 | yes | 1000 | 3 | 10 | 0 | 8 | 5  | contrastive | - | - | - | Simplified |
| 2b | conv6 | yes | 1000 | 3 | 50 | 0 | 8 | 20 | contrastive | - | - | - | Simplified |
