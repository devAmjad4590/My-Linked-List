# Queue can be implemented by using Linked List
# The process of Enqueing and Dequeing is O(1). 
# It wouldn't work with arrays because removing the first element in an array is O(n).
# However, Linkedlist adding last element (Enqueue) and removing first element (Dequeue) is O(1)
# So, Head is First of the Queue. Tail is the Last of the Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
