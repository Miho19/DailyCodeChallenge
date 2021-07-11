
class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class Linked_List:
    def __init__(self):
        self.head = None
        self.length = 0
    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return
        curr = self.head

        while(curr.next != None):
            curr = curr.next
        curr.next = new_node
        self.length += 1

    def print_list(self):
        if self.head is None or self.length == 0:
            return
        curr = self.head
        i = 0
        while(curr != None):
            print(i, "|" , curr.value)
            curr = curr.next
            i += 1
    def remove(self, k: int):
        if self.head is None or self.length == 0:
            return
        curr = self.head
        tail = self.head
        i = 0

        while (curr != None and i < k):
            curr = curr.next
            i += 1

        while(curr != None):
            curr = curr.next
            tail = tail.next
        
        temp = tail.next
        tail.value = temp.value
        tail.next = temp.next

        

        
        
new_list = Linked_List()

new_list.add(1)
new_list.add(0)
new_list.add(4)
new_list.add(3)
new_list.add(2)


new_list.print_list()

new_list.remove(3)
print("Removing 3rd last element")
new_list.print_list()