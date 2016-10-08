num = int(input("Enter number"))
if num%2 ==0:
    if num%3==0:
        print("number divisible by 3 and 2")
    else:
        print("number divisible by 2 and not divisible by 3")
else:
    if (num%3 ==0):
        print("Divisible by 3 not divisible by 2")
    else:
        print("not divisible by 2 and 3")
