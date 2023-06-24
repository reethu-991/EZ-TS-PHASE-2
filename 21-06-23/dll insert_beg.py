#create node
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_beg(self):
        n=node(400)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
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
n1=node(100)
l.head=n1
n2=node(200)
n2.prev=n1
n1.next=n2
n3=node(300)
n3.prev=n2
n2.next=n3
l.display()
print()
l.insert_beg()
l.display()
