"""
Asks the user for two numbers and prints the result
of the first number minus the second number.
"""

def main():
    print("This program subtracts one number from another.")
    v1=input("Enter first number: ")
    v2=input("Enter second number: ")
    result= (float(v1))-(float(v2))
    print("The result is",result)

if __name__ == '__main__':
    main()
