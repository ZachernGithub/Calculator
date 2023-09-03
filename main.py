operator = input("Choose Your Operator (+, -, *, /) : ")

if operator == '+' :
    first_number = int(input("What Is Your First Number? : "))
    second_number = int(input("What Is Your Second Number? : "))
    answer = first_number + second_number
    
    print("First Number + Second Number = " + str(answer))
    
elif operator == '-' :
    first_number = int(input("What Is Your First Number? : "))
    second_number = int(input("What Is Your Second Number? : "))
    answer = first_number - second_number
    
    print("First Number - Second Number = " + str(answer))
    
elif operator == '*' :
    first_number = int(input("What Is Your First Number? : "))
    second_number = int(input("What Is Your Second Number? : "))
    answer = first_number * second_number
    
    print("First Number × Second Number = " + str(answer))
    
elif operator == '/':
    first_number = int(input("What Is Your First Number? : "))
    second_number = int(input("What Is Your Second Number? : "))
    answer = first_number / second_number
    
    print("First Number ÷ Second Number = " + str(answer))
    
else:
    print("That Was An Invalid Operator.")
    print("Please Use This Operators (+, -, *, /)")