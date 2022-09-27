def add(x, y):       
   return x + y   
def subtract(x, y):      
   return x - y   
def multiply(x, y):      
   return x * y   
def divide(x, y):       
   return x / y        
print ("Please select the operation.")    
print ("1. Add")    
print ("2. Subtract")    
print ("3. Multiply")    
print ("4. Divide")    
    
choice = input("Please enter choice (1/ 2/ 3/ 4): ")    
    
a = int (input ("Please enter the first number: "))    
b = int (input ("Please enter the second number: "))    
    
if choice == '1':    
   print (a, " + ", b, " = ", add(a, b))    
    
elif choice == '2':    
   print (a, " - ", b, " = ", subtract(a, b))    
    
elif choice == '3':    
   print (a, " * ", b, " = ", multiply(a, b))    
elif choice == '4':    
   print (a, " / ", b, " = ", divide(a, b))    
else:    
   print ("This is an invalid input")







series program 2
n=int(input("Enter a number: "))
a=[]
for i in range(1,n+1):
    print(i,end=" ")
    if(i<n):
        print(end=",")
    a.append(i)
print(" ",)