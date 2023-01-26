
from itertools import permutations

nums = [1, 2, 3]
result = set(permutations(nums, 3))
print(len(result))