def add(n1, n2):
    return  n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def calc():

    operators = {"+": add, "-":subtract, "*":multiply, "/": divide}

    n1 = float(input("What is the first number?: "))

    for symbols in operators:
        print(symbols)
    should_continue = True


    while should_continue:
        operations = input("Choose an operation from above: ")
        n2 = float(input("What is the second number?: "))

        calculation = operators[operations]
        answer = round(calculation(n1, n2) ,3)

        print(f"{n1} {operations} {n2} = {answer}")

        if input(f"Type 'y' to continue with the calculation, or type 'n' to start a new calculatio: ") == "y":
            n1 = answer
        else:
            should_continue = False
            calc()
 
calc()


