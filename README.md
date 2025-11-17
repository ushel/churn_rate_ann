# churn_rate_ann
Churn rate detection


conda create --prefix ./m/myenvname python==3.11
conda activate ./m/myenvname

open .gitignore file and add

m/

if still environment folder then 

git rm -r --cached m/
git commit -m "Stop tracking env folder"


Create ANN

1. Sequential N/W
2. Dense(Hidden layer)
3. Activation function(ReLU, Sigmoid, Tanhm Leaky ReLU)
4. Optimizer -> for Backpropagation to update the weights
5. Loss Function reduce
6. Metrics -> Accuracy
7. Training information logs to store in folder -> Tensorboard