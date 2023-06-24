# Q . Create one dynamic array for a size  and do DS operations on it

n=int(input('enter size\n'))
l=[]
print('enter ele\n')
for i in range (1,n+1):
    a=int(input())
    l.append(a)

while(1):
    print('''1- insert')
     2-delete
     3-search
     4-sort
     5-display
     6- quit''')
    print('enter oper\n')
    opr=int(input())
    if (opr==1):
        p=int(input('enter how many to insert'))
        for i in range(1,p+1):
            a=int(input())
            l.append(a)
    if opr==2:
        for i in l:
            l.remove

    if opr==4:
        l.sort()
    if opr==5:
        print(
        
        
    
    
    
