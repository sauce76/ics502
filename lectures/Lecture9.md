# Lecture 9

09-Feb-2024 

--- 

Continuing last lecture derivation, after finding the loss function we take its derivative 

$$
 L(w) = w^TX^TXw-w^TX^Ty-y^TXw+y^Ty
$$
$$
\frac{\partial L}{\partial w} = 2X^TXw-X^Ty - X^Ty  = 0
$$

Solving for $w$ 

$$ (X^Xw - X^Ty) = 0 \\ 
X^TXw = X^Ty \\
w = (X^TX)^{-1}X^Ty
$$

This value of $w$ will minimize the loss function $L(w)$. 

### Gradient Descent 

\- Gradient descent  
    : is an iterative optimization algorithm to find the functions optimum.

- Stopping point of gradient descent ? 
    - Large number of iterations, and stop afterwards.
    - The difference in slope between the steps is small.

- Bigger steps might  cause divergence since it will skip a local minima. 

#### Method

1. Pick a starting point $w$ - randomly. 
2. Iteratively update $w$ until convergence. 

$$ w \larr w - \alpha * \Delta L $$ 

where $\alpha$ is the learning rate, and $\Delta L$ is

$$ \Delta L = \left[\frac{\partial L}{\partial w_1} \frac{\partial L}{\partial w_2} \  ... \   \frac{\partial L}{\partial w_d} \right]^T $$

or for OLS 

$$ \Delta L = X^TXw - X^Ty $$ Therefore:

$$ w^{t+1} = w^t - \alpha (X^TXw^t - X^Ty) $$


## Type of error in ML

1. Irreducible error
2. Reducible error 
    - Bias
    - Variance 
$$Total \ Error \ = Bias^2 \ + \ Variance + \ Irreducible \ Error  $$ 

### Bias and Variance 

Bias 
    : The average of output of multiple models $y'_1, y'_2, y'_3$ and subtract it from $y$

Variance 
    : The variance of output of multiple models. 