
##def table():
##    for i in  columns:
##        for j in rows:
##            a = i*j
##            
##            print(a, end = "")
##            
##            print()
##
##columns = [1,2,3,4,5,6,7,8,9,10]
##rows = [1,2,3,4,5,6,7,8,9,10]
##table()

def sortstr():
    a = input("enter:")
   
    c= []
    b= []

    for i in a:
        if i.isalpha():
            c.append(i)
        else:
            b.append(i)
    print(sorted(c))
    print(b)


    joining = ''.join((sorted(c))+(sorted(b)))
    print(joining)
sortstr()
