# Lecture 4

21 - Jan - 2025

---

## Weights - KNN

- Choosing a weight for distances between points?
  - $W_i=\frac{1}{d_i}$
  - $W_i = 1 - \frac{d_i}{\sum^{k}_{j=1} d_j} $
  - As long it follows common sense you can propose new weight system. 
  

## Evaluating the Model

- Given a data (e.g. a comma separated file or .CSV file). 

We will split the data into train and test. The percentage of the split is dependent on the size of the dataset and the required accuracy of the model, but usually 80% train set and 20% for most uses. Always prioritize the training since the test is meaningless on non existing model/poor model.


## KNN parameters 
- In KNN, you can choose different type of parameters, K {2, 3, 4, 5},and distances {Euclidean, Cosine, Man.}

    : From the previous parameters we can make $3x4=12$ models. We do a grid search of each combination of parameters and choose the best performance based on the evaluating metrics. 

- Why do we need validation split ? 
    : Because usually you may don't have control/access of the test data. (Data leakage? - look it up).

- In case we only have one choice of parameters then validations is not required but not it plays an important rule when deciding between different models as well. 



- What problem would occur when training without a validation split ? 
    : ?


## Misleading Mode
- If the model is showing high performance because validation have easier datapoint to detect characterstic/classification for example. Then wen can do the following: 

1. Shuffle the data and train them for each shuffle. 
2. Cross validation: x-fold cross validation. split the data into x segment and train/validate/test for every possible segment to produce x models  

The question is how then can we choose the best one ? 
    : .