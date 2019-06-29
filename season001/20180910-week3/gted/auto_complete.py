#!/bin/python3


class Node(object):

    def __init__(self, data=""):
        self._children = []
        self.data = data

    @property
    def children(self):
        return self._children

    def append_child(self, node):
        self._children.append(node)

    def append_children(self, children):
        self._children.extend(children)

    def empty_children(self):
        del self._children[:]

    def append_child_with_data(self, data):
        node = Node(data=data)
        self.append_child(node)


FULLY_MATCHED = 0
NOT_MATCHED = 1
PARTIALLY_MATCHED = 2


class WordsTree(object):

    def __init__(self):
        self.root = Node()
        self.find_cost = 0

    def reconstruct(self, word):
        remaining_chars = word
        root = self.root
        while root and remaining_chars:
            next_root = None
            matched_len = 0
            for child in root.children:
                matched_type, matched_len = self._sub_matched(child.data, remaining_chars)
                if matched_type == FULLY_MATCHED:
                    # Stop function, the word is already existing.
                    return
                elif matched_type == NOT_MATCHED:
                    # Go to next child if there are remaining children.
                    continue
                elif matched_type == PARTIALLY_MATCHED:
                    # Found, break
                    next_root = child
                    break
            if not next_root:
                root.append_child_with_data(remaining_chars)
                root = None
            else:  # Partially matched
                self._partially_reconstruct(next_root, matched_len)
                remaining_chars = remaining_chars[matched_len:]
                root = next_root

    def get_cost(self, word):
        remaining_chars = word
        root = self.root
        cost = 0
        while root and remaining_chars:
            next_root = None
            matched_len = 0
            for child in root.children:
                matched_type, matched_len = self._sub_matched(child.data, remaining_chars)
                if matched_type == FULLY_MATCHED:
                    if child.children:
                        cost += matched_len
                    else:
                        cost += 1
                    return cost
                elif matched_type == NOT_MATCHED:
                    continue
                elif matched_type == PARTIALLY_MATCHED:
                    next_root = child
                    break
            if next_root:  # Partially matched
                remaining_chars = remaining_chars[matched_len:]
                root = next_root
                cost += matched_len
        return 0

    def print_tree_by_level(self):
        queue = []
        queue.append(self.root)
        level = 0
        while queue:
            cur_level = []
            cur_level.extend(queue)
            del queue[:]
            s = ""
            for node in cur_level:
                s += node.data + " "
                queue.extend(node.children)
            level += 1
            print(str(level) + ": " + s)

    def _partially_reconstruct(self, root, matched_len):
        if root.data[matched_len:]:
            remaings = root.data[matched_len:]
            root.data = root.data[:matched_len]
            mid_root = Node(remaings)
            mid_root.append_children(root.children)
            root.empty_children()
            root.append_child(mid_root)

    def _sub_matched(self, root_word, new_word):
        matched_len = 0
        matched_type = NOT_MATCHED
        if root_word == new_word:
            matched_type = FULLY_MATCHED
            matched_len = len(root_word)
        else:
            shorter_len = len(root_word) if len(root_word) < len(new_word) else len(new_word)
            for i in range(1, shorter_len+1):
                if root_word[:i] == new_word[:i]:
                    matched_len = i
                else:
                    break
            if matched_len != 0:
                matched_type = PARTIALLY_MATCHED
        return matched_type, matched_len


def solution(words):
    answer = 0
    words_tree = WordsTree()
    for word in words:
        words_tree.reconstruct(word)
        words_tree.print_tree_by_level()
    for word in words:
        cost = words_tree.get_cost(word)
        print(word + ": " + str(cost))
        answer += cost
    return answer


words = ['go', 'gone', 'guild']
# words = ["abc", "def", "ghi", "jklm"]
# words = ["word", "war", "warrior", "world"]
# words = ['go', 'gone', 'guild', 'gui', 'guru', 'father', 'feed', 'feature']
# words = ['goto', 'gone', 'guild']


if __name__ == '__main__':
    print(solution(words))
