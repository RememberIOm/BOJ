import sys

input = sys.stdin.readline
sys.setrecursionlimit(10001)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = 0
        self.right = 0


def post_trv(node):
    if node:
        post_trv(node.left)
        post_trv(node.right)
        print(node.value)


inputs = []
while True:
    try:
        inputs.append(int(input()))
    except:
        break

root = Node(inputs[0])

for num in inputs[1:]:
    node_check = root

    while True:
        if num < node_check.value:
            if node_check.left:
                node_check = node_check.left
            else:
                node_check.left = Node(num)
                break
        else:
            if node_check.right:
                node_check = node_check.right
            else:
                node_check.right = Node(num)
                break

post_trv(root)
