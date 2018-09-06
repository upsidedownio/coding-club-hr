class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      
  def getData(self):
    return self.data

  def getLeft(self):
    return self.left
    
  def setLeft(self, node):
    self.left = node
    
  def getRight(self):
    return self.right
    
  def setRight(self, node):
    self.right = node
    
root = node(3)

node1 = node(5)
node2 = node(2)
root.setLeft(node1)
root.setRight(node2)

node3 = node(1)
node4 = node(4)
node1.setLeft(node3)
node1.setRight(node4)

node5 = node(6)
node2.setLeft(node5)

# root = node(7)

# node1 = node(5)
# node2 = node(9)
# root.setLeft(node1)
# root.setRight(node2)

# node3 = node(3)
# node4 = node(6)
# node1.setLeft(node3)
# node1.setRight(node4)

# node5 = node(8)
# node2.setLeft(node5)

def checkBinarySearchTree(root):
  return check(root, root.getLeft(), root.getRight())
  
def check(data, left, right):
  if left is None and right is None:
    return True

  resultLeft = False
  if left.getData():
    resultLeft = data.getData() > left.getData()
    if resultLeft is True:
      return check(left, left.getLeft(), left.getRight())
  
  resultRight = False
  if right.getData():
    resultRight = data.getData() < right.getData()
    if resultRight is True:
      return check(right, right.getLeft(), right.getRight())
  
  return False
  
if __name__ == '__main__':
  print(checkBinarySearchTree(root))
    
