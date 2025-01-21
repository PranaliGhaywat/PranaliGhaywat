

file = open('writ.txt',"w")  ##openfile with open attribute always has to close()..

txtfile = 'thisss iss aan  sentenceeeeeee to you wrritttenn byy youu \n'

##writing content stored in txtfile in wrt.txt file

file.write(txtfile)

sf = ("this is the tuple \n")
sd = ['this is list\n']
st= {'this','is','a','set'}

file.writelines(sf)
file.writelines(sd)
file.writelines(st)

inlist = [1,2,3,4,5]
for i in inlist:
    file.writelines(str(i))
    file.writelines(' ')

file.close()
