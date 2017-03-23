x=int(input("ENTER NUMBER"))
y=int(input("ENTER NUMBER"))
z=int(input("ENTER NUMBER"))
if(not(x>y or x>z)):
    print(x,y,z)
    if((x**2)==((y**2)+(z**2))):
        print("the triangle is right handed")
    else:
        print("not a right handed traingle")

elif(not(y>x or y>z)):
    
    print(y,z,x)
    if((y**2)==((x**2)+(z**2))):
        print("the triangle is right handed")
    else:   
        print("not a right handed traingle")
elif (not(z>x or z>y)):
    print(z,x,y)
    if((z**2)==((x**2)+(y**2))):
       print("the triangle is right handed")
    else:
         print("not a right handed traingle")
        
    

            


    
