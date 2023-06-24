#create node
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_pos(self,pos):
        n=node(44)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp  #44's prev=20
        n.next=temp.next  #44's next=30
        temp.next.prev=n  #30's prev =44
        temp.next=n   # 20's next= new node
    def display(self):
        if self.head is None:
            print('empty')
        else:
            temp=self.head
            while temp:
                 if temp.next!=None:
                    print(temp.data,end=" <--> ")
                 else:
                    print(temp.data,end=" ")
            #temp.data means first node's data
                 temp=temp.next
l=dll()
n1=node(10)
l.head=n1
n2=node(20)
n2.prev=n1
n1.next=n2
n3=node(30)
n3.prev=n2
n2.next=n3
l.display()
print()
l.insert_pos(3)
l.display()
