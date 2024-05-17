#a program that runs the summation of two numbers and outputs the results.
#uses functions.

def add_numbers(num1, num2):
    return num1 + num2

def main():
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    result = add_numbers(num1, num2)
    print("The sum is:", result)

main()    