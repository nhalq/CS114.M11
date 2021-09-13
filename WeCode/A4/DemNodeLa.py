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

def count(root) -> int:
  if not(root.m_left and root.m_right): return 1

  num_leaves = 0
  if root.m_left: num_leaves += count(root.m_left)
  if root.m_right: num_leaves += count(root.m_right)
  return num_leaves

root = None
while True:
  value = int(input())
  if not value: break
  root = insert(root, value)
print(count(root))
