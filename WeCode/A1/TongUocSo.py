import math
n = int(input())
print(sum([i if n % i == 0 else 0 for i in range(1, n)]))
