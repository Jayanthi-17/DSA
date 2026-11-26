class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def InsertAtPosition(self,val,position):
        new_node=Node(val)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            curr=self.head
            previous=None
            count=0
            while curr is not None and count < position:
                previous=curr
                curr=curr.next
                count+=1
            if previous is None:
                print("Invalid position")
                return
            previous.next=new_node
            new_node.next=curr
sll=SinglyLinkedList()
sll.InsertAtPosition(2,0)
                