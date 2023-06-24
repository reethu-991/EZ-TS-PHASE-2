class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    #insert a new node at the beg
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def detectandremoveloop(self):
        if self.head is None:#ll empty
            return
        if self.head.next is None: #ll has one node
            return
        slow_p=self.head
        fast_p=self.head
        while slow_p and fast_p and fast_p.next:
            slow_p=slow_p.next
            fast_p=fast_p.next.next
         # if slow_p and fast_p meet at some point there is a loop
            if slow_p==fast_p:
                print('meeting pt ',slow_p.data)
                slow_p==self.head
               #finding the beg of loop
                while slow_p.next != fast_p.next:
                    slow_p=slow_p.next
                    fast_p=fast_p.next
                   # sinc fastnode is the looping pt
                print('start of loop ',fast_p.next.data)
                fast_p.next=None # remove loop
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data,end='  ')
            temp=temp.next
llist=linkedlist()
llist.head=Node(50)
llist.head.next=Node(20)
llist.head.next.next=Node(15)
llist.head.next.next.next=Node(4)
llist.head.next.next.next.next=Node(10)
#create a loop for testing
extra=Node(1)
llist.head.next.next.next.next=extra
extra.next=llist.head.next
#llist.printlist()
llist.detectandremoveloop()
print(' ll after removing loop')
llist.printlist()
