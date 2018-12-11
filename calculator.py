# Simple calculator 
  
# ADD  
def add(num1, num2): 
    return num1 + num2 
  
# Substract  
def subtract(num1, num2): 
    return num1 - num2 
  
# Multiply 
def multiply(num1, num2): 
    return num1 * num2 
  
# Divide 
def divide(num1, num2): 
    return num1 / num2 
  
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
  
  
# Take input from the user  
select = raw_input("Select the operation from the menu: ") 

n1 = int(input("Enter your first number: ")) 
n2 = int(input("Enter your second number: ")) 
  
if select == '1':
    print(add(n1, n2)) 
elif select == '2': 
    print(subtract(n1, n2)) 
elif select == '3': 
    print(multiply(n1, n2)) 
elif select == '4': 
    print(divide(n1, n2)) 
else: 
    print("Invalid input") 