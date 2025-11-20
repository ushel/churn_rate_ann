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


How to determine optimal number of hidden layers and neurons for an Artificial Neural Network ANN

Start Simple: Begin with a simple architecture and gradually increase complexity if needed.
Grid Search/ Random Search: Use grid search or random search to try different architectures.
Cross-Validation: Use cross-validation to evaluate the performance of different architectures.
Heuristics and Rules of Thumb: Some heuristics and empirical rules can provide starting points such as:
    1. The number of neurons in the hidden layer should be between size of the input layer and the size of output layer
    2. A common practice is to start with 1-2 hidden layer