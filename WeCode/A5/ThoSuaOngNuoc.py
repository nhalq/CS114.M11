from collections import deque # Linked-list

UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3
DIRECT = [(-1, 0), (0, -1), (1, 0), (0, 1)]
TUPE_DIRECT = [
  [None , None, None , None ], # 0
  [UP   , None, DOWN , None ], # 1
  [None , LEFT, None , RIGHT], # 2
  [RIGHT, DOWN, None , None ], # 3
  [LEFT , None, None , DOWN ], # 4
  [None , None, LEFT , UP   ], # 5
  [None , UP  , RIGHT, None ], # 6
  [UP   , LEFT, DOWN , RIGHT], # 7
]

n = int(input())
diagram = [list(input()) for _ in range(n)]
m = len(diagram[-1])

def inRange(u, v) -> bool:
  return 0 <= min(u, v) and u < n and v < m

def getVolumn() -> int:
  queue = deque()
  bumps = deque(filter(None, [(u, v) if diagram[u][v].islower() else None for v in range(m) for u in range(n)]))

  for bump in bumps:
    for (dr, (du, dv)) in enumerate(DIRECT):
      u, v = bump
      nextu, nextv = u + du, v + dv
      if inRange(nextu, nextv):
        if diagram[nextu][nextv].isdigit():
          dr = TUPE_DIRECT[int(diagram[nextu][nextv])][dr]
          if dr != None: queue.append((nextu, nextv, dr, diagram[u][v]))

  volumn = 0
  visited = set(map(lambda q: (q[0], q[1]), queue))
  while len(queue):
    nextq = deque()
    volumn += len(queue)

    rVolumn = 0
    for (u, v, dr, bp) in queue:
      du, dv = DIRECT[dr]
      nextu, nextv = u + du, v + dv

      if (nextu, nextv) in visited: rVolumn += 1
      visited.add((nextu, nextv))

      if not inRange(nextu, nextv): return -volumn
      if diagram[nextu][nextv].isdigit():
        nextd = TUPE_DIRECT[int(diagram[nextu][nextv])][dr]
        if nextd == None: return -volumn
        nextq.append((nextu, nextv, nextd, bp))
      else:
        if diagram[nextu][nextv] != bp.upper():
          return -volumn

    queue = nextq
    volumn -= rVolumn
  return volumn

print(getVolumn())
