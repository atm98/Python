import random
num=random.randint(0,100)
def chec(n,h):
    if(n<h):
        cho=int(input("enter guess"))
        return check(n,cho)
    elif(n>h):
        cho=int(input("enter guess"))
        return check(n,cho)
    else:
        return 1
i=1
choice=int(input("enter guess"))
while(i!=10 or num!=choice):
    if(chec(num,choice)==1):
        print("you gusessed the number after",i,"tries")
        
        
