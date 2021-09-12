import sys

online = set()
while True:
  op = list(map(int, sys.stdin.readline().split()))
  try:
    if op[0] == 0: break
    elif op[0] == 1: online.add(op[1])
    elif op[0] == 2: print(int(op[1] in online))
    elif op[0] == 3: online.remove(op[1])
  except: pass
