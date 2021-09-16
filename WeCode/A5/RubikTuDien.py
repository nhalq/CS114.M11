U, B, L, R = range(4)
STATIC_MOVE = dict({
  "U": [(U, 0), (R, 8), (L, 4)],
  "u": [(U, 0), (U, 1), (U, 2), (U, 3), (R, 8), (R, 3), (R, 7), (R, 6), (L, 4), (L, 6), (L, 5), (L, 1)],
  "B": [(B, 0), (L, 8), (R, 4)],
  "b": [(B, 0), (B, 1), (B, 2), (B, 3), (L, 8), (L, 3), (L, 7), (L, 6), (R, 4), (R, 6), (R, 5), (R, 1)],
  "L": [(L, 0), (B, 8), (U, 4)],
  "l": [(L, 0), (L, 1), (L, 2), (L, 3), (B, 8), (B, 3), (B, 7), (B, 6), (U, 4), (U, 6), (U, 5), (U, 1)],
  "R": [(R, 0), (U, 8), (B, 4)],
  "r": [(R, 0), (R, 1), (R, 2), (R, 3), (U, 8), (U, 3), (U, 7), (U, 6), (B, 4), (B, 6), (B, 5), (B, 1)],
})

def apply(state, direct):
  move = STATIC_MOVE[direct[:1]]
  values = list(map(lambda _i: state[_i[0]][_i[1]], move))

  n = len(values) // 3
  if "'" in direct: values = values[-n:] + values[:-n]
  else            : values = values[n:] + values[:n]

  for (i, (u, v)) in enumerate(move):
    state[u][v] = values[i]
  return state

if __name__ == '__main__':
  color = input().split()
  moves = input().split()

  state = [[value for _ in range(9)] for value in color]
  for direct in reversed(moves):
    state = apply(state, direct)
  for i in range(4): print(*state[i])
