maximum = int(input(" Please Enter any Maximum Value : "))
if(maximum%2!=0):
    for number in range(1,(2*maximum)+1):
        if(number % 2 != 0):
            print("{0}".format(number))
else:
    for number in range(1,((2*maximum)-2)+1):
        if(number % 2 != 0):
            print("{0}".format(number))

