# My Python Program
# Task:  Use the function myFunction to output a simple "Hello World!" statement

def myFunction(name):
    return f"Hello, {name}!"

# Example of calling the function
first_name = input("Enter your first name: ")
greeting = myFunction(first_name)
print(greeting)
