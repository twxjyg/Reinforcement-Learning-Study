import numpy as np
reward = np.array([-2, -2, -2, 10, -1, 0, -5])
probability = np.array([(0, 0.5, 0, 0, 0.5, 0, 0),
(0, 0, 0.8, 0, 0, 0.2, 0),
(0, 0, 0, 0.6, 0, 0, 0.4),
(0, 0, 0, 0, 0, 1, 0),
(0.1, 0, 0, 0, 0.9, 0, 0),
(0, 0, 0, 0, 0, 0, 0),
(0.2, 0.4, 0.4, 0, 0, 0, 0)])
gamma = 1
v = np.linalg.inv(np.identity(7) - gamma * probability).dot(reward)
print(v)
