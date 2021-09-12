import math
a, b, c = sorted([int(input()) for _ in range(3)])

if a + b <= c: print('Khong phai tam giac')
else:
  _Type = 'thuong'
  if   a == b and b == c: _Type = 'deu'
  elif a == b or  b == c: _Type = 'can'
  elif a ** 2 + b ** 2 == c ** 2: _Type = 'vuong'

  p = (a + b + c) / 2
  _Area = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)

  if _Area == int(_Area): _Area = int(_Area)
  print('Tam giac {}, dien tich = {}'.format(_Type, _Area))
