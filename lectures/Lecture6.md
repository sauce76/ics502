# Evaluation Metrics

$$ TPR = Sensitivity = Recall = \frac{TP}{TP+FN} $$

$$ FPR = \frac{FP}{FP+TN} $$

$$ TNR = Specificity = \frac{TN}{TN+FP}
$$

$$
FNR = \frac{FN}{FN+TP}
$$

$$ Accuracy = \frac{T}{Null}  $$ 
    :revise the slides

- Increasing the threshold, decrease the $FP$ and thus increases the precision. By doing that we decrease the $Recall$ as well. 

- Our goal to make $Precision$ and $Recall$ high as much as possible but that not always achievable. Therefore we balance it using the F score 
$$ F_1 = 2\frac{P * R}{P+R} $$


- Another approach, is to consider all possible threshold.
- Area under the curve of TPR vs FPR across every possible threshold, is called area under the RoC curve - AUC-RoC. 

- If the dataset is imbalanced, accuracy and AUR-RoC could me misleading depiction of the model. F score is better.
-  Area under $Precision \ vs \  Recall$ across all possible threshold is a good metric for imbalanced dataset. 

---

$$ \frac{\partial x^T A x}{\partial x} = 2Ax $$, where $A$ is symmetric.
