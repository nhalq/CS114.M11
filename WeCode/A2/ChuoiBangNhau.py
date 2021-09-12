for _ in range(int(input())):
  print('YES' if len(set(input()).intersection(set(input()))) else 'NO')
