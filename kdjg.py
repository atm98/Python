import random
choice=input("enter choice5")
while(choice!='x'):
    if(choice=="roll"):
        result=random.randint(1,6)
        print(result)
    choice=input("enter choice5")

         
