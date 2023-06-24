class node:
    def __init__(sdelf,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.headd=None
        self.last=None
    def enqueue(Self,data):
        if self.last is None:
            self.head=node(data)
            self,last=self.head
        else:
            self.last.next=node(data)
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
            return to_return
a_queue=queue()
while True:
    print('enqueue <val>')
    print('dequeue')
    print('quit')
    #by using split 
