 #sll using dyanmic I/P
'''__init__'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def display (self):
        current=self.head
        while current is not None:
            print(current.data,end=' ')
            current=current.next
a_list=linkedlist()
b_list=linkedlist()
n=int(input('how many ele u would like to enter'))

for i in range(n):
      data=int(input('enter data items a list'))
      a_list.append(data)
print('the ll  - ',end='   ')
a_list.display()   
print()
for i in range(n):
      data=int(input('enter data items b list'))
      b_list.append(data)
print('the ll  - ',end='   ')
b_list.display()

if a_list==b_list:
    print('\nsame')
else:
    print('\nno')
