def changeme(mylist):
    print("Values inside the function before change", mylist)
    mylist[2]=50
    print("Values inside the function after change", mylist)
    return
mylist =[10,20,30]
changeme(mylist)
print("values outside the function",mylist)
