#!/bin/python3


class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.level = 0

    def __str__(self):
        return str(self.data)


def _get_next(sub_root, data):
    if data < sub_root.data:
        return sub_root, sub_root.left
    else:
        return sub_root, sub_root.right


class BasicBST(object):

    def __init__(self, root):
        self._root = root

    def add_node(self, data):
        node = Node(data)
        self._add_node(node)

    def add_node_and_print(self, data):
        self.add_node(data)
        self.print_tree()

    def _add_node(self, node):
        _sub_root, _next = _get_next(self._root, node.data)
        while _next is not None:
            _sub_root, _next = _get_next(_next, node.data)
        node.level = _sub_root.level + 1
        if node.data < _sub_root.data:
            _sub_root.left = node
        else:
            _sub_root.right = node

    def print_tree(self):
        s = ""
        node_queue = []
        node_queue.append(self._root)
        s += "[" + str(self._root.data) + "]\n"
        prev_node = self._root
        level = self._root.level
        while node_queue:
            cur_node = node_queue.pop(0)
            if cur_node.level > level:
                level = cur_node.level
                s += "\n"
            if cur_node.left:
                node_queue.append(cur_node.left)
                s += "[" + str(cur_node.left.data)
            else:
                s += "[-"
            s += "|"
            if cur_node.right:
                node_queue.append(cur_node.right)
                s += str(cur_node.right.data) + "]"
            else:
                s += "-]"
        print(s)


if __name__ == '__main__':
    root = Node(6)
    bst = BasicBST(root)
    bst.print_tree()
    bst.add_node_and_print(2)
    bst.add_node_and_print(1)
    bst.add_node_and_print(10)
    bst.add_node_and_print(8)
    bst.add_node_and_print(9)
    bst.add_node_and_print(7)
    bst.add_node_and_print(0)
    bst.add_node_and_print(5)
