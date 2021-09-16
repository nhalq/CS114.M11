from collections import deque

LEFT, UP, RIGHT, DOWN = range(4)
SNAKE_HEAD   = ['<', '^', '>', 'v']
SNAKE_DIRECT = [(0, -1), (-1, 0), (0, 1), (1, 0)]
SNAKE_MOVE   = ['L', 'F', 'R']


class Snake:
  def __init__(self, head, direct) -> None:
    self.direct = direct
    self.snake  = deque([head])
    self.alive  = True

  def addNode(self, node) -> None:
    self.snake.append(node)

  def setDirect(self, direct) -> int:
    self.direct += direct + len(SNAKE_DIRECT)
    self.direct %= len(SNAKE_DIRECT)
    return self.direct

  def forward(self, inRange) -> bool:
    if not self.alive: return False

    u, v = self.snake[0]
    du, dv = SNAKE_DIRECT[self.direct]

    u, v = u + du, v + dv
    last = self.snake.pop()
    if not inRange(u, v) or (u, v) in self.snake:
      self.snake.append(last)
      self.alive = False
      return False

    self.snake.insert(0, (u, v))
    return True

  def visualize(self, width, height):
    headSign, nodeSign = SNAKE_HEAD[self.direct], '*'
    if not self.alive: headSign, nodeSign = 'X', 'X'

    table = [['.' for _ in range(width)] for _ in range(height)]
    for (u, v) in self.snake: table[u][v] = nodeSign

    headu, headv = self.snake[0]
    table[headu][headv] = headSign

    for u in range(height): print(*table[u], sep='')


class Table:
  def __init__(self, width, height, table) -> None:
    self.width  = width
    self.height = height
    self.table  = table

  def inRange(self, u, v) -> bool:
    return 0 <= min(u, v) and u < self.height and v < self.width

  def getSnakeHead(self):
    for u in range(self.height):
      for v in range(self.width):
        if self.table[u][v] in SNAKE_HEAD:
          return (u, v)
    return (-1, -1)

  def getSnakeNodes(self):
    return list(filter(None, [
      (u, v) if self.table[u][v] == '*' else None
      for v in range(self.width)
      for u in range(self.height)
    ]))

  def getSnake(self):
    head = self.getSnakeHead()
    if head == (-1, -1): return None

    nodes = self.getSnakeNodes()
    snake = Snake(head, SNAKE_HEAD.index(self.table[head[0]][head[1]]))

    last = head
    added = set()
    for _ in range(len(nodes)):
      found = False
      for (du, dv) in SNAKE_DIRECT:
        u, v = last
        u, v = u + du, v + dv
        if self.inRange(u, v) and (u, v) in nodes and not (u, v) in added:
          last = (u, v)
          added.add(last)
          snake.addNode(last)
          found = True
          break
      if not found: return None
    return snake


if __name__ == '__main__':
  n, m, c = map(int, input().split())
  table = [input() for _ in range(n)]
  moves = list(map(lambda m: SNAKE_MOVE.index(m.upper()) - 1, input()))

  table = Table(m, n, table)
  snake = table.getSnake()

  for move in moves:
    snake.setDirect(move)
    if move == 0: snake.forward(table.inRange)

  snake.visualize(m, n)
