import sys
""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
SYS_MIN = -1 * (sys.maxsize - 1)
SYS_MAX = sys.maxsize

def check_binary_search_tree_(root):
    return walk(root, SYS_MIN, SYS_MAX)
 
def walk(node, mini, maxi):
    # End condition of recursive call
    if node is None:
        return True
    # Check violation
    if node.data < mini or node.data > maxi:
        return False
    # shrink
    return (walk(node.left, mini, node.data -1) and
          walk(node.right, node.data+1, maxi))
