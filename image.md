# Deep CNN + LSTM siamese network for video similarity
## Image-based siamese Results can be found here

[Website for  Visualizing Data](http://10.2.132.196/gta/gta_data.php) (Only visible inside IIIT's network)

| Exp #  | Conv Layer | l2-reg | batch-size | num-epochs | loss | plots | train-accuracy | val-accuracy | train-val-test split  | Data-Augmentations | Runtime | learning-rate | tied-weights | convNet training | pretrained-weights |
|-----------| -----------|-----------------|---------------|------------|------------------|--------|-------| ---------- | ---- | ------ | -------------- | ------------ | -------------------| ----------------- |---------------| ------- | ---------- | ------ |
| 1a | conv6 | 0.0 | 64 | 50 | contrastive | [accuracy](images/image-siamese/exp1/accuracy_1a.pdf)   [loss](images/image-siamese/exp1/loss_1a.pdf)| 9300/10167=91% | 1027/1129=91% | 10167-1129-0 | NO |  3hrs | 1e-6 with a deacy of 0.85x after every epoch | YES | all layers | AmosNet weights | 
| 1b | conv6 | 0.0 | 64 | 50 | contrastive | [accuracy](images/image-siamese/exp1/accuracy_1b.pdf)   [loss](images/image-siamese/exp1/loss_1b.pdf)| 9263/10167=91% | 1024/1129=91% | 10167-1129-0 | NO |  3hrs | 1e-5 with a deacy of 0.85x after every epoch | YES | all layers | AmosNet weights | 
| 1c | fc6 | 0.0 | 64 | 50 | contrastive | [accuracy](images/image-siamese/exp1/accuracy_1c.pdf)   [loss](images/image-siamese/exp1/loss_1c.pdf)| 9300/10167=91% | 1027/1129=91% | 10167-1129-0 | NO |  3hrs | 1e-6 with a deacy of 0.85x after every epoch | YES | all layers | AmosNet weights | 
| 1d | fc7 | 0.0 | 64 | 50 | contrastive | [accuracy](images/image-siamese/exp1/accuracy_1d.pdf)   [loss](images/image-siamese/exp1/loss_1d.pdf)| 9300/10167=91% | 1027/1129=91% | 10167-1129-0 | NO |  3hrs | 1e-6 with a deacy of 0.85x after every epoch | YES | all layers | AmosNet weights | 
| 1e |  | 0.0 | 64 | 50 | contrastive | [accuracy](images/image-siamese/exp1/accuracy_1e.pdf)   [loss](images/image-siamese/exp1/loss_1e.pdf)| 9300/10167=91% | 1027/1129=91% | 10167-1129-0 | NO |  3hrs | 1e-6 with a deacy of 0.85x after every epoch | YES | all layers | None | 


### Some Jargons used above  
all_layers --> all-layers in the CNN were finetuned
