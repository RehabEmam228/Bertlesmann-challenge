import numpy as np
import torch
a = np.random.rand(4, 5)
print(a)
# creates a tensor from the numpy array
b = torch.from_numpy(a)
print(b)
# multiplies tensor b by 2 in place which changes a as well
print(b.mul_(2))
print(a)