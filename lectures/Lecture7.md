# Lecture 7 

02-Feb-2025

--- 

- Hypothesis Space
    : Is the space of all possible solution/fitting to the dataset.

- We care more about the unseen data, no matter how much the model fit the training data (over fitting), we only focus on the unseen data. 


## Ordinary Least Square (OLS) Regression: 

Error - Loss
    : The absolute value of difference between the real value (from seen data) and predicted value (predicted from the model) at the same $x$ or input.

$$
Loss = Error = L(y_i, y_i')=\frac{1}{N} \sum_{i=1}^N (y_i - y_i')^2    
$$


$$
y_i' = f(x_i) 
$$


--- 


$$ 
w_1x_1 + w_2x_2 + ... + w_dx_d = W^TX
$$

- Where $w_i$ are the coefficient or weight of the model. 

$$
E(w)=L(w)=\frac{1}{N} \sum^N_{i=1}(y_i - w^Tx_i)^2
$$ 

    Is known as Mean Square Error, where  
- $w^T$, and $x_i$ are vectors, their multiple result in a scalar.
- $y_i$ is a label (i.e. a scalar)

where, $x_i =(x_{i1}, x_{i2}, ...., x_{id})$ is a vector of variables. 

$$ f(x) = x^2 +1 $$
- $min \ f(x) = 1$
    :   Is the minimum of the function
- $arg \ min \ f(x) = $
    :   Is the value of $x$ that make $f(x)$ minimum. 



$$
\frac{\partial L}{\partial w_j} = \frac{2}{N}\sum^N_{i=1} (w^Tx_i-y_i)x_{ij} = 0
$$

- When taking the derivative of the term $w^Tx_i$ all term zeros except the coefficient of $x_j$ which is $x_{ij}$






