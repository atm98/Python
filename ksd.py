for char in "abcdefghijklmnopqrstuvwxyz":
    perc=100*count(text,char)/len(text)
    print("{0}-{1}%".format(char,round(perc,2)))
