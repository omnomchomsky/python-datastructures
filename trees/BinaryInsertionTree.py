class Node:
    def __init__(self, data, left="", right=""):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.data) + ", " + str(self.left) + ", " + str(self.right) + ")"


def insert(data, tree=""):
    if tree is "":
        return Node(data)
    elif data > tree.data:
        return Node(tree.data, tree.left, insert(data, tree.right))
    else:
        return Node(tree.data, insert(data, tree.left), tree.right)


a = insert(5)
b = insert(6, a)
c = insert(4, b)
print(a)
print(b)
print(c)
