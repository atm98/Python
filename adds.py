n=int(input("enter range"))
res=" "
j=0
i=0
m=[n]
for i in range(n+1):
    for j in range(n+1):
        m[i][j]==i*j
