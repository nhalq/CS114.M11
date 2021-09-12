x = int(input()) - 1
if not x in range(30): print('So', x + 1, 'khong nam trong khoang [1,30].')
else:
  a, b = 1, 1
  for i in range(x):
    a, b = b, a + b
  print(a)
