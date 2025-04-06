# Hard SVM margins

18-March-2025

---

$$ \text{Argmax} \ \frac{2}{||w||} \sim \frac{1}{||w||} \rarr \text{Argmin} \ ||w|| $$ 



Maximize the objective function, with the contraints $g(x)$ and $f(x)$
$\text{Max  } \mathcal{F} \\  g_i(x)=0 \\ f_j(x)_ \leq 0 $

- Build the Lagrange function 
$$ \mathcal{L}(\bold{w}, b, \bold{\alpha}) = \frac{1}{2}\bold{w^Tw} - \sum_{i=1}^N \bold{\alpha _i}[y_i(\bold{w^Tx_i} + b)-1] $$

$$ \text{Max}_\alpha (\text{Min}_{w,b}(w,b,\alpha)) $$

- Min will be a function of $\alpha$ then we maximize 