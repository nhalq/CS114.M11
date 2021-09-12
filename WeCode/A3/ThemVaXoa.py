from sys import stdin, stdout

arr = list()
while True:
  op = list(map(int, stdin.readline().split()))
  if op[0] == 0: arr.insert(0, op[1])
  elif op[0] == 1: arr.append(op[1])
  elif op[0] == 2:
    try: arr.insert(arr.index(op[1]) + 1, op[2])
    except: arr.insert(0, op[2])
  elif op[0] == 3:
    try: arr.remove(op[1])
    except: pass
  elif op[0] == 4: arr = list(filter(lambda e: e != op[1], arr))
  elif op[0] == 5: arr.pop(0) if len(arr) != 0 else None
  else: break
stdout.write(' '.join(map(str, arr)) if len(arr) else 'blank')
