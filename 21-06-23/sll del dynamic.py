class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class SLL:
    def delete_at_begin(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            self.head=self.head.next
            print(temp.data,"is deleted successfully")
            del(temp)
        print("Delete at Begin operation is completed successfully")
    
    def delete_at_position(self,pos):
        if self.head is None:
            print("List is Empty")
        else:
            count=0
            temp=self.head
            if pos==0:
                temp=self.head
                self.head=self.head.next
                print(temp.data,"is deleted successfully")
                del(temp)
            else:
                prev=None
                while (pos)!=count and temp is not None:
                    prev=temp
                    temp=temp.next
                    count+=1
                if temp==None:
                    print("Index out of range")
                else:
                    prev.next=temp.next
                    print(temp.data,"is deleted successfully")
                    del(temp)
            print('Delete at Position operation completed successfully')
    
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            prev=None
            while temp.next:
                prev=temp
                temp=temp.next
            prev.next=None
            print(temp.data,"is deleted successfully")
            del(temp)
        print("Delete at End operation is completed successfully")

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=' ')
                if temp.next!=None:
                    print('->',end=' ')
                temp=temp.next
        print("\nDisplay operation completed successfully")

print("1.Delete at Begin\n2.Delete at Position\n3.Delete at end\n4.Search\n5.Display\n6.Exit\n")
o=SLL()
while True:
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        o.delete_at_begin()
    elif ch==2:
        pos=int(input("Enter Position to delete:"))
        o.delete_at_position(pos)
    elif ch==3:
        o.delete_at_end()
    elif ch==4:
        num=int(input("Enter Number to Search:"))
        o.search(num)
    elif ch==5:
        o.display()
    elif ch==6:
        print('\n\t***Your Exited**\n\t\tTHE END*\n')
        break
    else:
        print("Invalid Entry\nTry Once Again")
