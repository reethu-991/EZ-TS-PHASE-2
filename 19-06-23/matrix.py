
r,c=int(input('enter row')),int(input('enter col'))
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        l.append(int(input()))
    m.append(l)
for i in range(r):
    for j in range(c):
        print(m[i][j],end=' ')
    print()
print('de')
for i in range(r):
    for j in range(c):
        if i==j:
            print(m[i][j],end=' ')
        else:
            print(" ",end=" ")
    print()
print('nde')
for i in range(r):
    for j in range(c):
        if i!=j:
            print(m[i][j],end=' ' )
        else:
            print(" ",end=" ")
    print()
print('lt')
for i in range(r):
    for j in range(c):
        if i>j:
            print(m[i][j],end=' ')
        else:
            print(" ",end=" ")
    print()
print('ut')
for i in range(r):
    for j in range(c):
        if i<j:
            print(m[i][j],end=' ')
        else:
            print(" ",end=" ")
    print()
    
