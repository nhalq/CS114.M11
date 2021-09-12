import sys

n, m = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
matrix = ''.join(sys.stdin.readlines()).split()

if (p * q) != (n * m): p, q = n, m
sys.stdout.write('\n'.join([' '.join(matrix[u * q:(u + 1) * q]) for u in range(p)]))
