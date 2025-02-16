# Lecture 11 

16-Feb-2025

Linear regression slides 

---

## Regression Model Evaluation 

### Ridge Regression
Ridge regression is regularization technique aims to push $w$ to be smaller 

$$ 
L(w) = ||Xw-y||_2^2 + \lambda ||w||_2^2
$$


- Since $\lambda$ is a hyper parameters that we choose. Having it at high value will force the optimization to push $w$ to lower value, approaching zero. 
- On another case having $\lambda$ to be low value will let $w$ be flexible (high or low) which is not favorable since we want to make $w$ small?

- How to choose the perfect $\lambda$ ? 
    : You cant until you try. 


### Lasso Regression

Similar to ridge by the second term we take norm 1 $||w||_1$ 

- Lasso enable us to use feature selection (i.e. removing unnecessary features). 


## Why Lasso Can Perform Feature Selection but Ridge Cannot

### 1. **Mathematical Explanation**
- **Lasso (L1 regularization):**  
  \[
  \min \sum (y_i - \hat{y}_i)^2 + \lambda \sum |\beta_j|
  \]
  - The L1 norm (absolute values of coefficients) encourages sparsity.  
  - When optimizing, some coefficients are **exactly zero**, effectively removing those features from the model.  
  - This happens because the L1 penalty creates a sharp, non-differentiable point at zero, making it more likely for coefficients to shrink completely to zero.

- **Ridge (L2 regularization):**  
  \[
  \min \sum (y_i - \hat{y}_i)^2 + \lambda \sum \beta_j^2
  \]
  - The L2 norm (squared values of coefficients) **shrinks** coefficients but does not set them exactly to zero.  
  - It distributes shrinkage across all features, meaning all variables remain in the model, even if they have very small weights.

### 2. **Geometric Intuition**
- The Lasso constraint forms a **diamond-shaped** feasible region, which forces some coefficients to hit exactly zero at the corners.  
- The Ridge constraint forms a **circular** feasible region, which shrinks coefficients but never forces them to be exactly zero.

### 3. **Practical Implication**
- **Lasso is useful for feature selection**, as it automatically removes irrelevant or redundant features.  
- **Ridge is better when all features contribute to the prediction**, preventing overfitting by keeping all features but reducing their impact.

$_{from \ chatGBT}$