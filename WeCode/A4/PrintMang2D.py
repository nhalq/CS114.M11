n, m = map(int, input().split())
arr = [input().split() for _ in range(n)]

fmt = [max([len(arr[u][v]) for u in range(n)]) for v in range(m)]
fmt = ' '.join(map(lambda length: "{{:{}d}}".format(length), fmt))
for u in range(n): print(fmt.format(*map(int, arr[u])))
