class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length < 2:
            self.head = None
            self.tail = None
        else:
            node = self.head
            for i in range(self.length - 2):
                node = node.next
            self.tail = node
            self.tail.next = None
        self.length -= 1
        return temp

linkedlist = LinkedList(4)
linkedlist.append(9)
linkedlist.pop()
linkedlist.pop()
linkedlist.append(10)
linkedlist.printList()


