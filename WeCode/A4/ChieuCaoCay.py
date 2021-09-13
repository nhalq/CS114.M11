import sys

class Node:
  def __init__(self, value=None) -> None:
    self.m_value      = value
    self.m_left :Node = None
    self.m_right:Node = None

def insert(root: Node, value: int) -> Node:
  if not root: root = Node(value)
  elif root.m_value < value: root.m_left = insert(root.m_left, value)
  elif root.m_value > value: root.m_right = insert(root.m_right, value)
  return root

def countLeaves(root: Node) -> int:
  if not root: return 0
  if not root.m_left and not root.m_right: return 1

  numberOfLeaves = 0
  numberOfLeaves += countLeaves(root.m_left)
  numberOfLeaves += countLeaves(root.m_right)
  return numberOfLeaves

root = None
while True:
  value = int(sys.stdin.readline())
  if not value: break
  root = insert(root, value)
print(countLeaves(root))
