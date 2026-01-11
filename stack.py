# There are two ways to implement a stack:
# 1. List
# 2. Linked List

# And in this example we will implement Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value) # The head of the linked list acts as the top of the tail for O(1) pop and push
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top= new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True


