""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def check_binary_search_tree_(root):
    node_queue = []
    root.max = 10001
    root.min = -1
    node_queue.append(root)
    while node_queue:
        cur_node = node_queue.pop(0)
        if cur_node.left:
            if cur_node.left.data < cur_node.data and cur_node.left.data > cur_node.min:
                cur_node.left.max = cur_node.data
                cur_node.left.min = cur_node.min
                node_queue.append(cur_node.left)
            else:
                return False
        if cur_node.right:
            if cur_node.right.data > cur_node.data and cur_node.right.data < cur_node.max:
                cur_node.right.min = cur_node.data
                cur_node.right.max = cur_node.max
                node_queue.append(cur_node.right)
            else:
                return False
    return True
