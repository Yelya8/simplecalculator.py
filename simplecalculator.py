choose_operator = input('''Please type in the operation you would like to complete: 
                        + for addition
                        - for subtraction
                        / for division
                        * for multiplication''') # User to select their mathematical operation 

number1 = float(input("Please enter the first number:")) # User prompt for 1st number
number2 = float(input("Please enter the second number:")) # User prompt for 2nd number

if choose_operator == '+': # Addition
    print(number1 + number2) # User is given answer to their sum 

elif choose_operator == '-': # Subtraction
    print(number1 - number2) # User is given answer to their sum 

elif choose_operator == '/': # Division
    if number2 == 0: # If user tries to divide by zero
        raise Exception('ZeroDivisionError') # Zero division error message given
    else:
        print(number1 / number2) # User is given answer to their sum 

elif choose_operator == '*': # Multiplication
    print(number1 * number2) # User is given answer to their sum 
else: 
    print("Invalid input detected. Please select an mathmatical operation.") #If no operation is selected, print error message
       
