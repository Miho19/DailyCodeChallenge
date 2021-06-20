

from typing import Deque


class Node:
    def __init__(self, val, left=None, right= None):
        self.val = val
        self.left = left
        self.right = right

def _deserialize(node, string):
    if node is None:
        return Node(string)
    
    if node.val > string:
        return _deserialize(node.left, string)
    else:
        return _deserialize(node.right, string)
        

def deserialize(string):
    string = string.split()
    node = Node(string[0])

    for str in string:
        if(node.val > str):
            print(str)
            node.left = _deserialize(node, str)
        else:
            node.right = _deserialize(node, str)

    return node
    


def serialize(node):
    ans = ' '
    
    if node is None or node.val == None:
        return None

    stack = Deque()
    discovered = list()

    stack.append(node)

    while stack:
        root = stack.pop()

        if root in discovered:
            continue

        if root is None:
            ans += '#' + ' '
            continue
        
        discovered.append(root)

        ans += root.val + ' '

        if root.right not in discovered:
            stack.append(root.right)

        if root.left not in discovered:
            stack.append(root.left)

    return ans





node = Node('root', Node('left', Node('left.left')), Node('right'))



print(serialize(node))