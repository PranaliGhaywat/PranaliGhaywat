

with open('writ.txt','r') as writ:
    copy = writ.readlines()
    print(copy)



new = open('cpyfilein.txt', "w+")

for line in copy:
    new.write(line)
    cursorpos = new.tell()
    new.seek(0)
    r = new.read()

print()
print('corsur position is at :',cursorpos)
print()
print(r)
