i=int(input("enter range"))
j=0 
def fact(n):
    fact=1
    if(n==0):
        return 1
    else:
        while(n!=1):
            fact=fact*n
            n=n-1
    return fact
def val(a):
    h=0
    res=""
    for h in range(a+1):
        vv=str(fact(a)//(fact(h)*fact(a-h)))+" " 
        res=res + vv
        h=h+1
    return res
    
while(i!=(-1)):
    print(i*" "+ val(j))
    i=i-1
    j=j+1




    
