class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def Traversal(self):
        curr=self.head
        if self.head==None:
            print("Linked List is empty")
        while curr is not None:
            print(curr,end=" ")
            curr=curr.next

sll=SinglyLinkedList()
sll.Traversal()
