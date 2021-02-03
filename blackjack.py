
import itertools
import numpy as np
s1 = set([])
a = input().split()
b = input().split()
print(a)
print(b)

c = list(itertools.combinations(b, 3))
c = list(map(int, a))
print(c)
np.sum(c, axis=1)
