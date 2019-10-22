"""
Basic List operations are:
size (returns then number of elements in the list)
clear (removes all the elements from the list)
empty (returns true if the container contains no elements, false otherwise

append(x) (adds x to the end of the list)
push(x) (adds x to the front of the list)
pop_back() (removes the last element of the list)
pop_front() (removes the first element of the list)
back ([-1]) (returns the object at the end of the list)
push ([0]) (returns the object at the front of the list)

operator[](x) (returns the object at index x in the list with no bounds-checking, which could generate a runtime error)
at (x) (returns the object at index x with bounds checking)
"""
from math import floor
from typing import Optional, Any


def half_len(l):
    return floor(len(l)/2)


def split(l):
    half=half_len(l)
    return (l[:half], l[half+1:]) if half > 2 else l


def m_sort(l):
    return sorted(l)
    # value = split(l)
    # print(value)
    # if len(first_half) > 1:
    #     sorted_fh = m_sort(first_half)
    # else:
    #     sorted_fh = first_half
    # if len(second_half) > 1:
    #     sorted_sh = m_sort(second_half)
    # else:
    #     sorted_sh = second_half
    # return sorted_fh + sorted_sh if sorted_fh and sorted_sh else sorted_fh if sorted_fh else sorted_sh


print(m_sort([5, 4, 6, 3 ,10, 2, 7]))


def list_longer(l1, l2):
    return l1 if (len(l1) >= len(l2)) else l2


def list_shorter(l1, l2):
    return l2 if (len(l1) >= len(l2)) else l1


# 3.4 Given two sorted lists, L1 and L2, write a procedure to compute L1 intersects L2 using only basic list operations.


def intersect(l1, l2):
    # Make sure lists are in order
    list1 = m_sort(l1)
    list2 = m_sort(l2)

    # Determine which list is longer
    longer = list_longer(list1, list2)
    shorter = list_shorter(list1, list2)

    j = 0
    intersection = []

    # Iterate through both lists and add matching elements to the intersection list
    for i in longer:
        while i < shorter[j]:
            break
        while j < len(shorter) - 1 and shorter[j] < i:
            j += 1
        if i is shorter[j]:
            intersection += [i]
    return intersection


print(intersect(
    [1, 2, 3],
    [2, 3, 4]
))

print(intersect(
    [1, 2, 3, 4, 5],
    [2, 3, 4]
))

try:
    print(intersect(
        [1, "two", 3],
        [2, 3, 4]
    ))
except TypeError as err:
    print("Successfully caught TypeError: ", err)

print(intersect(
    [5, 3, 5, 2, 7, 1],
    [1, 6, 4, 8, 5, 2, 10]
))

print(intersect(
    [5, 3, 5, 2, 7, 1],
    [1, 6, 4, 8, 5, 2, 10, 5]
))

print(intersect(
    ["one", "two", "three"],
    ["three", "one", "nine"]
))


# 3.5 Same as 3.4 but union instead of intersection
def union(l1, l2):
    # Union is trivial in Python
    return l1 + l2


class Stack:
    def __init__(self, arr=[]):
        self.array = arr
        print("Stack initialized")

    def is_empty(self):
        return not len(self.array)

    def top(self):
        return self.array[0] if not self.is_empty() else None

    def pop(self):
        top = self.top()
        if top:
            self.array.remove(top)
        return top

    def push(self, x):
        self.array.append(x)

    @property
    def __str__(self):
        return str(self.array)


class Queue:
    def __init__(self, arr=[]):
        self.array = arr

    def enqueue(self, x):
        self.array = [x] + self.array

    def next(self):
        return self.array[-1]

    def dequeue(self):
        x = self.next()
        del self.array[-1]
        return x


q = Queue([1])

q.enqueue(3)
q.enqueue(100)
print(q.next())
print(q.dequeue())
print(q.next())
print(q.dequeue())
"""
Basic List operations are:
size (returns then number of elements in the list)
clear (removes all the elements from the list)
empty (returns true if the container contains no elements, false otherwise

append(x) (adds x to the end of the list)
push(x) (adds x to the front of the list)
pop_back() (removes the last element of the list)
pop_front() (removes the first element of the list)
bottom ([-1]) (returns the object at the end of the list)
top ([0]) (returns the object at the front of the list)

operator[](x) (returns the object at index x in the list with no bounds-checking, which could generate a runtime error)
at (x) (returns the object at index x with bounds checking)
"""
