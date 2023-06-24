l1=[]
while(True):
    print("1.Insert\n2.Search\n3.Delete\n4.Sort\n5.Quit")
    z=int(input("Enter your choice"))
    match z:
        case 1:
            n=int(input("Enter size of the array"))
            for i in range(n):
                o=int(input("Enter your element"))
                l1.append(o)
            print(l1)
        case 2:
            k=int(input("Enter element to be searched"))
            if k in l1:
                print(k,"Element found")
            else:
                print("Element not found")
        case 3:
            k=int(input("Enter element to delete"))
            if k in l1:
                l1.remove(k)
                print("Deletion Successful")
                print(l1)
            else:
                print("Element not in the list")
        case 4:
            l1.sort()
            print("sorted elements")
            print(l1)
        case 5:
            break
