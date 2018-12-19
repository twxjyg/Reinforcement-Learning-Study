# 文字作业

## 1 计算MRPs

由于markov奖励过程中的值函数:
$V(s) = R(s) + \gamma \sum_{s^{\prime} \in S} P_{ss^{\prime}}V(s^{\prime})$
可以写成矩阵的形式：
$v = R + \gamma P v$
$\begin{bmatrix}
V(s_1) \\
. \\
V(s_n) \\
\end{bmatrix} = \begin{bmatrix}
R(s_1) \\
. \\
R(s_n) \\
\end{bmatrix} + \gamma \begin{bmatrix}
P_{s_1s_1} & ... & P_{s_1s_n} \\
. & . & . \\
P_{s_ns_1} & ... & P_{s_ns_n} \\
\end{bmatrix} \begin{bmatrix}
V(s_1) \\
. \\
V(s_n) \\
\end{bmatrix}
$
所以有:
$v = (I - \gamma P)^{-1}R$
P为：
$
\begin{bmatrix}
0 & 0.5 & 0 & 0 & 0.5 & 0 & 0 \\
0 & 0 & 0.8 & 0 & 0 & 0.2 & 0 \\
0 & 0 & 0 & 0.6 & 0 & 0 & 0.4 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 \\
0.1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0.2 & 0.4 & 0.4 & 0 & 0 & 0 & 0 \\
\end{bmatrix}
$
R为:
$
\begin{bmatrix}
-2 \\
-2 \\
-2 \\
10 \\
-1 \\
0 \\
-5
\end{bmatrix}
$
v为:

```python
import numpy as np
reward = np.array([-2, -2, -2, 10, -1, 0, -5])
probability = np.array([(0, 0.5, 0, 0, 0.5, 0, 0),
(0, 0, 0.8, 0, 0, 0.2, 0),
(0, 0, 0, 0.6, 0, 0, 0.4),
(0, 0, 0, 0, 0, 1, 0),
(0.1, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 0, 0),
(0.2, 0.4, 0.4, 0, 0, 0, 0)])
v = np.linalg.inv(np.identity(7) - 0.5 * probability).dot(reward)
print(v)
# [ -2.79939798
# -2.05762202
# -0.14405504
# 10.
# -1.1399699
# 0.
# -5.72027521]
```

$
\begin{bmatrix}
V(科目一) \\
V(科目二) \\
V(科目三) \\
V(通过) \\
V(玩手机) \\
V(睡觉) \\
V(挂科) \\
\end{bmatrix} =
\begin{bmatrix}
-2.79939798 \\
-2.05762202 \\
-0.14405504 \\
10. \\
-1.1399699 \\
0. \\
-5.72027521 \\
\end{bmatrix}
$

## 2