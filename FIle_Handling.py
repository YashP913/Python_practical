def Read():
    file = open("python.txt", "r")
    print (file.read())
def Write():
    file = open("python.txt", "w")
    file.write("I am from CSE \n")
    file.write("Division B\n")
def append():
    file = open("python.txt", "a")
    file.write("This is python practical")
print(Write())  
print(append())
print(Read())