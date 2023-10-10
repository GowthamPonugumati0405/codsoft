import os
def add(x,y):
    return(x+y)
def subtract(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def divide(x,y):
    return(x/y)
operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
} 
def calculator():
    number1=int(input('Enter the first number:'))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input('Pick an operation: ')
        number2=int(input('Enter next number:'))
        calculator_function=operations_dict[op_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2}={output}")

        should_contain=input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit").lower()
        if should_contain=='y':
            number1=output  
        elif should_contain=='n':
            continue_flag=False
            os.system('cls')
            calculator()
        
        else:
            continue_flag=False
            print("End")
calculator()
        
     

        
    


