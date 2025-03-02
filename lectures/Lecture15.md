# Logistic Regression 

02-March-2024 

---

- Find the probability $p(y=1|x)$ (probability of x belong to class 1) for classification using linear regression we need a special function. 

### Sigmoid Function $\sigma(x)$

- Since linear regression have a range of $ ( -\infty, \infty ) $, we need a function that can squeeze the range to $[0,1]$. 

$$
\sigma(x) = \frac{e^x}{e^x +1} = \frac{1}{1+e^{-1}}
$$

- Applying the sigmoid function the solution $w^Tx_i$.

$$
\sigma (w^Tx_i) = \frac{1}{1+e^{w^Tx_i}}
$$

- $\sigma$(x) is a monotonic function (i.e. both x and y increase/decrease together)

$$ if: \ x_1 > x_2 => f(x_1) > f(x_2) $$
$$ if: \ x_1 < x_2 => f(x_1) < f(x_2) $$


### Linear Regression

1. Make the hypothesis:
$$ h_w(x) = p(x) = \frac{1}{1+e^{-w^Tx}}$$ 
    - If $p(x) \geq 0.5, y=1$, otherwise $0$

2. Odds $=\frac{p(x)}{1-p(x)} \ =>  \ Log(odds) =w^Tx $ 
    - I define the odds, also when increase $p(x)$ all other variables increases

    $$p(x) <=> Odds <=> Log(odds) <=> w^Tx$$ 
    All increase with $p(x)$ i.e. directly proportional 

---
After simplifying the Odds
$$Odds =\frac{\frac{1}{1+e^{-w^Tx}}}{1-\frac{1}{1+e^{-w^Tx}}} = e^{w^Tx}$$ 
$$ln(Odds) = ln(e^{w^Tx}) = w^Tx$$

---

$$  p(x)=p(y=1|x) \\ => p(y=0|x)=1-p(y=1|x)\\  = 1-p(x) $$
Therefore:
$$p(y|x) = p(x)^y . (1-p(x))^{1-y} $$

$ y=1:  \ \ p(y=1|x) = p(x)  $
$ y=0:  \ \ p(y=0|x) = 1 - p(x)  $


### Likelyhood Function 

$ \mathcal{L} = P(D|\theta) = p(y_1 ... y_m|x_1 .. x_m, \theta)$

Conditional independent
    : $p(x_1, x_2|\theta)=p(x_1|\theta)\cdot p(x_2|\theta)$ They are independent only if $\theta$ is known.

$$ \mathcal{L} = p(y_1|x_y1,\theta)\cdot p(y_2|x_y2,\theta) ... \  p(y_m|x_ym,\theta) \\ = \prod_{i=1}^N p(y_i|x_i,\theta)$$ Here theta is $w$, or weights of our model.


### Key points

- 

