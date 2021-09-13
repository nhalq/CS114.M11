n, m = input().split()
print(int('0' + m[:-len(n)]) + 1 - (int(m[-len(n):]) < int(n)))
