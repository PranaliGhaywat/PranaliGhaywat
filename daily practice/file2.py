

##with open('writ.txt',"a") as file:
##    fi =  "\nthis is another thing wriiteten in same file that is writ.txt file..!"
##    file.writelines(fi)
n = 0
c= 0
space =0
with open('writ.txt', "r") as writ:
    r = writ.readlines()
    for line in r:
        n += 1
        for ch in line:
            if ch == ' ':
                space += 1
            else:
                c += 1

    print()
    
    print('total numbers of lines:',n)
    print('total number of characters:',c)
    print('total number of spaces',space)
