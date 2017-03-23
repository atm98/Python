filename=input("filename")
with open(filename) as f:
    text=f.read()
print(text)
def count1(text1,char):
    count=0
    for c in text1:
        if(c==char):
            count=count+1
    return count
print(count1(text,'a'))
for char in "abcdefghijklmnopqrstuvwxyz":
    perc=100*count1(text,char)/len(text)
    print("{0}-{1}%".format(char,round(perc,2)))
