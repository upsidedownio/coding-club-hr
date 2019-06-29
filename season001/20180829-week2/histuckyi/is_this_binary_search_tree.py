""" 
hackerrank : Is This a Binary Search Tree
https://www.hackerrank.com/challenges/is-binary-search-tree/problem

Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
before = 0
result = True

def checkBST(root):
    global before
    global result
    if root is None:
        pass
    else:
        checkBST(root.left)
        if before < root.data:
            before = root.data
        else:
            result = False
        checkBST(root.right)

def solve(root):
    global before
    global result
    checkBST(root)
    return result

def check_binary_search_tree_(root):
    return solve(root)