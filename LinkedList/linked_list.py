class ListNode:
    def __init__(self,data=0,next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(None)

    def shift(self,new_value):
        temp_node = self.head
        self.head = ListNode(new_value,temp_node)

    def unshift():
        self.head = self.head.next

    def search(self,target):
        L = self.head
        while L:
            if L.data == target:
                return True
            else:
                L = L.next
        return False


linkedlist1 = LinkedList()
linkedlist1.shift(5)
linkedlist1.shift(7)
print(linkedlist1.search(5))
