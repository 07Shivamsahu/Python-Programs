# Maximum of two Numbers in Python.

# Create a maximum Function
def maximum(a, b):
    if a>=b:
        return a
    else:
        return b
# Getting input from user 
a=int(input("Enter your first number "))
b=int(input("Enter your second number "))

# If you want  you can dirctly declare values of a and b without taking input.
print(maximum(a, b))