# Lecture 8 

04-Feb-2024

---


## Closed Form Solution


$$ 
Arg \ min\ ||y'-y||^2  = Arg \ min\ ||Xw - y||^2 
$$ 

$$
Arg \ min \ ||Xw-y|| = (Xw-y)^T(Xw-y)
\\
= \left[(Xw)^T -y^T \right](Xw-y) = (w^TX^T - y^T)(Xw-y) \\
= w^TX^TXw-w^TX^Ty-y^TXw+y^Ty
$$

Now we take the derivative with respect of $w$

$$
\frac{\partial ||Xw-y||^2}{\partial w} = 0 \\
= 2X^TXw + 
$$



