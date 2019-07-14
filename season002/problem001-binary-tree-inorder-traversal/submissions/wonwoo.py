# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        output = []
        cursor = root

        while cursor is not None or not len(stack) is 0:
            while cursor is not None:
                stack.append(cursor)
                cursor = cursor.left

            cursor = stack.pop()
            output.append(cursor.val)
            cursor = cursor.right

        return output
