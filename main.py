# ufunc 'add' did not contain loop with signature matching types

import numpy as np

arr = np.array([1, 3, 5, 7, 9, 11, '13', '15'])

arr = arr.astype(float)

mean = np.mean(arr)

print(mean)  # 👉️ 8.0