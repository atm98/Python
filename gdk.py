def fib(x,y):
    return x+y
i=0
n=int(input("enetr integer"))
j=[]
for i in range(n):
    if(i==0):
        j.append(1)
        print(j[i])
    else:
       fibval=fib(j[i-2],j[i-1])
       j.append(fibval)
       print(j[i])
    
        
