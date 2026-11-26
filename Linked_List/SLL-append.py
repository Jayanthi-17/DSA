class Node:
    def __init__(self,val)->None:
        self.val=val
        self.next=None
class SinglyLinkedList:
    def __init__(self)->None:
        self.head=None
    def append(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
    def Traversal(self):
            curr=self.head
            if self.head==None:
                print("Linked List is empty")
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next

sll=SinglyLinkedList()
sll.append(1)
sll.append(15)
sll.append(11)
sll.append(20)
sll.Traversal()
