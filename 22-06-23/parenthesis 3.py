stack=[]
s=input()
n=len(s)
c=0
flag=1
if s[0]==']' or s[0]=='}' or s[0]==')':
    print(False)
else:
    for i in range(n):
        if s[i]=='[' or s[i]=='(' or s[i]=='{':
            stack.append(s[i])
            c+=1
        elif s[i]==']' or s[i]=='}' or s[i]==')':
            if stack==[]:
                flag=0
                break
            if (stack[-1]=='{' and s[i]=='}') or (stack[-1]=='[' and s[i]==']') or (stack[-1]=='(' and s[i]==')'):
                stack.pop()
                c-=1
            else:
                flag=0
                break
        else:
            flag=-1
            break
    if flag==0 or c!=0:
        print(False)
    elif flag==-1:
        print("Invalid Paranthesis")
    else:
        print(True)
