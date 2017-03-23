def s(a,b ):
   return a+b
def sub(a1 , b1):
    return a1-b1
def d( a12, b12):
    return a12/b12
def m( a13 , b13 ):
    return a13*b13
def p( a14 , b14):
    return a14**b14


choice=input("Enter choice")
while(choice!='x'):
    if(choice=='+'):
        num1=int(input("input num1"))
        num2=int(input("input num2"))
        print("Sum=",s(num1,num2))
    elif(choice=='-'):
        num12=int(input("input num1"))
        num22=int(input("input num2"))
        print("Difference",sub(m12,m22))
    elif(choice=='/'):
        num13=int(input("input num1"))
        num23=int(input("input num2"))
        print("Quotuint=",d(num13,num23))
    elif(choice=='*'):
        num14=int(input("input num1"))
        num24=int(input("input num2"))
        print("Product=",m(num14,num24))
    elif(choice=='^'):
        num15=int(input("input num1"))
        num25=int(input("input num2"))
        print("Result",p(num15,num25))
    else:
        print("Wrong inputed choice")
    choice=input("Enter choice")
    

                 
