def arm1(a):
    i=a
    sum=0
    while(i!=0):
   
        r=i%10
        i=i//10
        print("r=",r)
        sum1=sum*10 +r
        sum=r**3 + sum
        print(sum)
    if(sum==a):
        return True
    elif(sum1==a):
        return False

def fact(b):
    if(b==1):
        return 1
    else:
        su=b*b-1    
        return fact(su)
        print(su," ")
        
    
n=int(input("enter number"))
if(arm1(n)==True):
    print("The Numeber is Armstrong")
    print("the factorial of ",n,"is",fact(n))
else:
    print("The Numeber is Palindrome")
    print("the factorial of ",n,"is",fact(n))
    
    
