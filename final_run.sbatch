#!/bin/bash
#SBATCH --partition=cosmos
#SBATCH --nodelist=fusor
#SBATCH --time=17:59:00
#SBATCH --gres=gpu:1,gpu_mem:5000
#SBATCH --mem=6000
#SBATCH --qos=intermediate

source activate my_venv_2_7
python train.py --return_outputs 1 --name=14a --lr 0.00001 > result_14a
python train.py --return_outputs 0 --name=14b --lr 0.00001 > result_14b
#python eval.py --model  --filename --label 

