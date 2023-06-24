s1=[]
s2=[]
n=int(input('size:'))
def  push():
    for i in range(n):
        s=int(input('enter ele'))
        if s%2==0:
            s1.append(s)
        else:
            s2.append(s)
def pop():
     p=input('s1 or s2')
     if  p=='s1':
         if not s1:
             print('stack is empty')
         else:
            e=s1.pop()
            print('removed ele',e)
            print(s1)
     else:
         if not s2:
             print('stack is empty')
         else:
            o=s2.pop()
            print('removed ele',o)
            print(s2)
def display():
    d=input('s1 or s2')
    if d=='s1':
        print(s1)
    else: 
        print(s2)
            
while True:
    print('1.push 2. pop 3. show 4.quit')
    ch=int(input('enter ch'))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print('invalid ch')
