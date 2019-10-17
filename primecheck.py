import math
n = 33


def find(n):
    for i in range(2,int(math.sqrt(n))):
        if n%i == 0:
            return -1
    return n


y = find(n)
print(y)