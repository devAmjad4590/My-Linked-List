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

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        return slow

    def binary_to_decimal(self):
        curr = self.head
        n = 0
        while curr:
            n = n * 2 + curr.value
            curr = curr.next
        return n

    def remove_duplicates(self):
        seen = set()
        current = self.head
        prev = None

        while current:
            if current.value in seen:
                prev.next = current.next
                self.length -= 1
            else:
                seen.add(current.value)
                prev = current
            current = current.next

    def has_loop(self):
        slow = self.head
        fast = self.head
        
        while fast != None:
            slow = slow.next
            fast = fast.next
            if fast == None:
                return False
            fast = fast.next
            if fast == slow:
                return True
        return False

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        removed_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            removed_node.next = None
        self.length -= 1
        return removed_node 

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if self.length == 0:
            return None
        node = self.head
        i = 0
        while i != index:
            node = node.next 
            i += 1
        return node

    def set_value(self,index, value):
        temp = self.get(index) 
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head
    
    for _ in range(k):
       if fast is None:
           return None
       fast = fast.next
        
    while fast:
       slow = slow.next
       fast = fast.next

    return slow
    

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)
print(result.value)
