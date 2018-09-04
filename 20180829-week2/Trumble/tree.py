# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def check(root):
    if root.left is not None:
        left = check(root.left)
    else:
        print('l' + str(root.data))
        
    if root.right is not None:
        right = check(root.right)
    else:
        print('r' + str(root.data))

def check_binary_search_tree_(root):
    return check(root)