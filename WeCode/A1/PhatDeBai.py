n, k, p, q = [int(input()) for _ in range(4)]
l = (p - 1) * 2 + (q - 1)

if (l - k) < 0 and (l + k) >= n: print('-1')
else:
  l = l - k if (l - k) >= 0 else l + k
  print(l // 2 + 1, l % 2 + 1)
