while True:
    a = input()
    for i in a:
        if i.isalpha() or i.isdigit():
            k=10
            print('invalid response')
            continue
    if len(a)%2==1:
        print('no')
        continue
    b = []
    k = 1
    if a[0]==')' or a[0]=='}' or a[0]==']':
        print('no')
        continue
    for i in a:
        if i == '(' or i == '[' or i == '{':
            b.append(i)
        elif i == ')' or i == ']' or i == '}' and not len(b)==0:
            if i == ')' and b[-1] == '(' and not len(b)==0:
                b.pop()
            elif i == ']' and b[-1] == '[' and not len(b)==0:
                b.pop()
            elif i == '}' and b[-1] == '{' and not len(b)==0:
                b.pop()
            else:
                k = 10
    if len(b)!=0:
        print('no')
    elif k == 10 :
        print('no')
    else:
        print('yes')
