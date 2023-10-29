from calculator_art import logo
#from thonny import clear
#Calculator

#Add
def add(n1, n2):
    return n1+n2

#Subtract
def subtract(n1, n2):
    return n1-n2

#Multiplication
def multiply(n1, n2):
    return n1*n2

#Divison
def divide(n1, n2):
    return n1/n2

#modulus
#def modulus(n1, n2):
    #return n1%n2

operations={
  "+":add, 
  "-":subtract, 
  "*":multiply, 
  "/":divide
  #"%":modulus
           }
def calculator():
    print(logo)
    
    num1 = float(input("What is the first number:"))
    for symbols in operations:
        print(symbols)
    #create flag
    should_continue = True

    while should_continue:
        
        operation_symbols = input("Pick the operation: ")
        num2 = float(input("What is the next number:"))
        calculation_functions = operations[operation_symbols]
        answer = round(calculation_functions(num1, num2), 2)

        print(f"{num1} {operation_symbols} {num2} = {answer}")

        if(input("Type 'y' to continue the calculating with {answer} or type 'n' to start a new calculation: ")) == 'y':
            num1 = answer
        else:
           should_continue = False
           #clear()
           #calculator()
       
calculator()
