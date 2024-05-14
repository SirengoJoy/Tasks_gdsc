#a program that runs the summation of two numbers and outputs the results.
#uses functions.

def add_numbers(num1, num2):
    return num1 + num2

#here we declare the subtraction function
def subtract_numbers(num1,num2):
    return num1-num2

def multiply_numbers(num1,num2):
    return num1*num2

def divide_numbers(num1,num2):
    return num1/num2



def main():
    print("Hello and welcome, choose an operation(reply with 1, 2, 3, 4 ):\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n") #This is just a basic instruction statement telling the user what to do 
    users_choice=input("Enter your choice: ")    #we obtain the user choice either '1' or '2'

    #using the for loop to eliminate value error when the user enters an invalid input.
    for _ in range(3):  
            try: 
                num1 = float(input("Please enter the first number: "))
                break
            except ValueError:
                print("Invalid input. Please try again")
    else:
            print("Too many attempts.Time out!") 
            return 


    for _ in range(3):
            try: 
                num2 = float(input("Please enter the second number: "))
                break
            except ValueError:
                print("Invalid input. Please try again")
    else:
            print("Too many attempts.Time out!") 
            return 
    #end of for loop.            
        
    #here we have the logic, depending on the user input, a different function is called
    if users_choice =='1':
        result = add_numbers(num1, num2)
        print("The sum is:", result)
    elif users_choice =='2':
        result = subtract_numbers(num1, num2)
        print("The answer is:", result)
    elif users_choice == '3':  
        result = multiply_numbers(num1, num2)
        print("The product is:", result) 

    elif users_choice == '4':  
        result = divide_numbers(num1, num2)
        print("The answer is:", result)     
    else:
        print("Invalid input")
main() #calling the main function  