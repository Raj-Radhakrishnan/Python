def fib(n):
    resutl =[]
    a,b,c= 0,1,0
    while c <n:
        resutl.append(b)
        a,b = b, a+b
        c +=c
    return resutl

