min = 0     #initialize the minimum value
max = 100   #initialize the maximum value
mid = 50    #initialize the mid value
print("Assume a number between 1 and 100 and I will try to guess it!!!")
for i in range(7):
    def gre():
        global min,mid
        min = mid    #Changing the value of min to a higher value
        mid = (max+min)//2
    def les():
        global max,mid
        max = mid    #Changing the value of max to a lower value
        mid = (max+min)//2
    def equ():
        print("Your answer is %d" % mid)    #Print the correct answer
    print("Is this your answer? %d" % mid)
    ans = input("Is the number greater or lesser than %d? Type G for greater and L for Lesser and yes if it is correct.\n" %mid)
    if ans is 'l':
        les()   #call function less
    elif ans is 'g':
        gre()   #call function gre
    elif ans in 'yes':
        equ()   #call function equ
        break
    else:
        print("Enter correct input")
        break