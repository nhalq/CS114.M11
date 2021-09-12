import math
for _ in range(int(input())):
  a, b = map(int, input().split())
  g = math.gcd(a, b)
  print(a // g, str(b // g) if b // g != 1 else '')
