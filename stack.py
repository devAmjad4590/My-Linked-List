# There are two ways to implement a stack:
# 1. List
# 2. Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# class Stack:
#     def __init__(self, value):
#         new_node = Node(value) # The head of the linked list acts as the top of the tail for O(1) pop and push
#         self.top = new_node
#         self.height = 1
#
#     def print_stack(self):
#         temp = self.top
#         while temp:
#             print(temp.value)
#             temp = temp.next
#
#     def push(self, value):
#         new_node = Node(value)
#         if self.height == 0:
#             self.top= new_node
#         else:
#             new_node.next = self.top
#             self.top = new_node
#         self.height += 1
#         return True
#
#     def pop(self):
#         if self.height == 0:
#             return None
#         temp = self.top
#         self.top = temp.next
#         temp.next = None
#         self.height -= 1
#         return temp


## List Version of Stack
class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)
        return True

    def pop(self):
        if not self.stack_list:
            return None
        return self.stack_list.pop()


    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

def reverse_string(string):
    my_stack = Stack()
    res = ''
    for i in string:
        my_stack.push(i)

    while not my_stack.is_empty():
        s = my_stack.pop()
        res += str(s)
    return res


def is_balanced_parentheses(string):
    my_stack = Stack()
    for i in string:
        if i == '(':
            my_stack.push(i)

        elif i == ')':
            if my_stack.is_empty() and i != my_stack.pop():
                return False
    return True if my_stack.is_empty() else False


def sort_stack(stack):
    new_stack = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        
        while not new_stack.is_empty() and new_stack.peek() > temp:
            stack.push(new_stack.pop())

        new_stack.push(temp)

    while not new_stack.is_empty():
        stack.push(new_stack.pop())

 
