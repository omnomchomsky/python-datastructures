class Node:

    def __init__(self, data, left=(), right=()):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        print("(" + self.data + ", " + str(self.left) + ", " + str(self.right) + ")")

# Depth First Traversal Routine


def prefix(tree):
    print(tree.data, end="")
    if tree.left is not ():
        prefix(tree.left)
    if tree.right is not ():
        prefix(tree.right)


def infix(tree):
    if tree.left is not ():
         infix(tree.left)
    print(tree.data, end="")
    if tree.right is not ():
         infix(tree.right)


def postfix(tree, expression=""):
    if tree.left is not ():
        postfix(tree.left)
    if tree.right is not ():
        postfix(tree.right)
    print(tree.data, end="")
    return expression

# Parser


chars = list("ab+cd-*")
stack = []
operators = ["+", "-", "*", "/"]

for i in chars:
    if i in operators:
        right_node = stack.pop()
        left_node = stack.pop()
        stack.append(Node(i, left_node, right_node))
    else:
        stack.append(Node(i))

parse_tree = stack.pop()
prefix(parse_tree)
print()
infix(parse_tree)
print()
postfix(parse_tree)
