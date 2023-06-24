class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
    def pop(self):
        if self.head in None:
            return None
 
        else:
            popped=self.head.data
            self.head=self.head.next
            return popped
obj_stack=stack()
while True:
    print('push <val>')
    print('pop')
    print('quit')
    do=input('what would u like to do') .split()
    print('do',do)
    print('do[0]',do[0])
    oper=do[0].strip().lower()
    if oper=='push':
        obj_stack.push(int(do[1]))
    elif oper=='pop':
        popped=obj_stack.pop()
        if popped is None:
            print('stack is empty')
        else:
            print('popped val',int(popped))
    elif oper=='quit':
        break
    
