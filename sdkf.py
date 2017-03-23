i=0
n=int(input("enetr integer"))
j=[]
for i in range(n):
    if(i==0):
        j.append(1)
    elif(i==1):
        j.append(1)
    else:
        j.append(j[i-2]+j[i-1])
for i in range(n):
    print(j[i])
