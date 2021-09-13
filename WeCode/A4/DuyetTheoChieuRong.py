class Node:
  def __init__(self, value=None) -> None:
    self.m_value = value
    self.m_left  = None
    self.m_right = None

def insert(root: Node, value: int) -> Node:
  if not root              : root = Node(value)
  elif root.m_value > value: root.m_left = insert(root.m_left, value)
  elif root.m_value < value: root.m_right = insert(root.m_right, value)
  return root

def browse(root) -> int:
  queue, i = [root], 0
  while i < len(queue):
    u = queue[i]
    if u.m_left: queue.append(u.m_left)
    if u.m_right: queue.append(u.m_right)
    i += 1
  return queue

root = None
while True:
  value = int(input())
  if not value: break
  root = insert(root, value)
print(*map(lambda n: n.m_value, browse(root)))
