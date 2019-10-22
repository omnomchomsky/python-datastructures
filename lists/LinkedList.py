import sys

class Node:
    def __init__(self, data=""):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    # Constructor
    def __init__(self, arr=None):
        if not arr:
            self.head = None
            self.tail = None
            self.size = 0
        elif len(arr) is 1:
            self.head = Node(arr[0])
            self.tail = self.head
            self.size = 1
        # Else convert list into linked list TODO

    # Read Only/Information Operations
    def size(self):
        return self.size

    def is_empty(self):
        return not self.head

    def top(self):
        return self.head.data

    def bottom(self):
        return self.tail.data

    def at(self, index=0):
        current_node = self.head
        count = 0
        while current_node is not None:
            if count is index:
                return current_node.data
            count += 1
            current_node = current_node.next
        raise IndexError


    # Mutation Operations (create/destroy/update)
    # def clear(self):

    def append(self, x):
        if self.is_empty():
            self.__init__([x])
        else:
            new_node = Node(x)
            self.tail.next = new_node
            self.tail.previous = self.tail
            self.tail = self.tail.next
            self.size += 1

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        new_node.previous = None # Redundent
        self.head.previous = new_node
        self.size += 1
        self.head = new_node

    def pop_front(self):
        x = self.head.data
        old_node = self.head
        self.head = self.head.next
        self.previous = None
        del old_node
        self.size -= 1
        return x

    def pop_back(self):
        x = self.tail.data
        old_node = self.tail
        self.tail = self.tail.previous
        self.tail.next = None
        self.size -= 1
        del old_node
        return

    def __str__(self):
        if self.is_empty():
            return "[]"
        else:
            return_string = "["
            current_node = self.head
            while current_node.next is not None:
                return_string += str(current_node.data) + ", "
                current_node = current_node.next
            return return_string + str(current_node.data) + "]"


linked_list = LinkedList()
linked_list.append(11)
linked_list.push(9)
print(linked_list.at(0))
print(linked_list.at(1))
try:
    print(linked_list.at(2))
except IndexError as misc:
    print("Raised IndexError exception as expected")
print(linked_list)
