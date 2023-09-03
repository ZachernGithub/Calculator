operator = ""

while len(operator) == 0:
    operator = input("Choose Your Operator (+, -, *, /) : ")

if operator == '+':
    first_number = ""
    second_number = ""
    
    while first_number == "":
        try:
            first_number = int(input("What Is Your First Number? : "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while second_number == "":
        try:
            second_number = int(input("What Is Your Second Number? : "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    answer = first_number + second_number
    
    print("First Number + Second Number = " + str(answer))
    
elif operator == '-':
    first_number = ""
    second_number = ""
    
    while first_number == "":
        try:
            first_number = int(input("What Is Your First Number? : "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while second_number == "":
        try:
            second_number = int(input("What Is Your Second Number? : "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    answer = first_number - second_number
    
    print("First Number - Second Number = " + str(answer))
   
elif operator == '*':
    first_number = ""
    second_number = ""
    
    while first_number == "":
        try:
            first_number = int(input("What Is Your First Number? : "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while second_number == "":
        try:
            second_number = int(input("What Is Your Second Number? : "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    answer = first_number * second_number
    
    print("First Number * Second Number = " + str(answer))
    
elif operator == '/':
    first_number = ""
    second_number = ""
    
    while first_number == "":
        try:
            first_number = int(input("What Is Your First Number? : "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while second_number == "":
        try:
            second_number = int(input("What Is Your Second Number? : "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if second_number == 0:
        print("Error: Division by zero is not allowed.")
    else:
        answer = first_number / second_number
        print("First Number / Second Number = " + str(answer))
    
else:
    print("That Was An Invalid Operator.")
    print("Please Use These Operators (+, -, *, /)")