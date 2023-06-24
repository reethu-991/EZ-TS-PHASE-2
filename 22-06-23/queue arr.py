queue=[]
def enqueue():
    ele=input('enter ele')
    queue.append(ele)
    print(ele,' is added')
def dequeue():
    if not queue:
        print('q is empty')
    else:
        e=queue.pop(0)
        print('removed ele',e)
def display():
    print(queue)
while True:
    print('1.add 2. remove 3. show 4.quit')
    ch=int(input('enter ch'))
    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print('invalid ch')
