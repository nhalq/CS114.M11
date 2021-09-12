n = input()
arr = map(int, input().split())
k, x = map(int, input().split())
print(' '.join(map(str, sorted(map(lambda e: e[1], sorted(map(lambda e: (abs(e - x), e), arr))[:k])))))
