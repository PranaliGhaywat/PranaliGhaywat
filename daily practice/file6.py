
a = input('enter a string:')

c= ''
for i in a:
    
    c = i + c
    print(c)
print(c)

b= ['apple','banana',[],'kaju','bcd',2,4,5]
h = []
for i in b:
    try:
        if i == []:
            b.remove(i)
            print(b)
        if i == str:
            g = i.title()
            h.append(i)
            

    

    except:
        if i != "":
            
            h.append(i*5)
            print(h)

