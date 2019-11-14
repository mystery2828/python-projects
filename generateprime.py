lst = []
for n in range(2,100):
    if ((6*n+1)%5 != 0 and (6*n+1)%7 != 0):  
        lst.append(6*n+1)
    if ((6*n+5)%5 != 0 and (6*n+5)%7 != 0):
        lst.append(6*n+5)
print(lst)
