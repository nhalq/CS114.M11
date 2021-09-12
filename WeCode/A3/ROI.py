import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

a, b, c, d = map(int, sys.stdin.readline().split())
result = [[0 for _ in range(m)] for _ in range(n)]
for u in range(a, c + 1):
  for v in range(b, d + 1):
    result[u][v] = arr[u][v]

answer = list()
for u in range(n):
  answer.append(' '.join(map(str, result[u])))
sys.stdout.write('\n'.join(answer))
