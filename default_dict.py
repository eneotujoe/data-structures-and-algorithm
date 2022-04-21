
from collections import defaultdict 

# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
s = [(0, 1), (0, 2), (1, 2), (2, 0), (3, 3)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d)
