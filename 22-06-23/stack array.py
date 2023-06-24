stack=[]
def push():
    ele=int(input('enter ele'))
    stack.append(ele)
    print(stack)
def pop():
    if not stack:
        print('stack is empty')
    else:
        e=stack.pop()
        print('removed ele',e)
        print(stack)
def display():
    print(stack)
def peek():
    if not stack:
        print('stack is empty')
    else: 
            print(stack[-1])
            
while True:
    print('enter ch 1.push 2.pop 3.quit 4.display 5.peek()')
    ch=int(input())
    if ch==1:
        push()
    elif ch==2:
        pop ()
    elif ch==3:
        break
    elif ch==4:
        display()
    elif ch==5:
        peek()
    else:
        print('invalid ch')
        
