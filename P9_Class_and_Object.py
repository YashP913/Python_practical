class CSE:
    def sum(a,b):
       print(a+b)
    
Object = CSE
a = int(input("Enter the first number :- "))
b = int(input("Enter the second number :- "))
print("\nSum of above entered number is :-  ",end = " ")
Object.sum(a,b)
