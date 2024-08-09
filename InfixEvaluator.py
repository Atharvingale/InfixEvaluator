exp = "(5+5)*(5+6)*50"
tokens = []
number = ""
for char in exp:
    if char.isdigit():
        number += char
    else:
        if number:
            tokens.append(int(number))  #Converts the current element to integer if it is a digit
            number = ""
        if char in "+-*/()":
            tokens.append(char)
if number:
    tokens.append(int(number))   #pushes the remaining elements to the stack if available
def evaluate(values,operators):   #Checks the current operator which is present at the top of the stack
    right = values.pop()   #it pops the top most vale from the stack and assign the value to the right variable  
    left = values.pop()   #Same are right but it assigns the value to the left operator
    operator = operators.pop() #it assigns the value of top most operator to operator variable
    if operator == "+":   #Checks for operator and perform the operation
        value = right + left
        values.append(value)
    elif operator == "-":    #Checks for operator and perform the operation
        value = left - right
        values.append(value)
    elif operator == "*":    #Checks for operator and perform the operation
        value = left * right
        values.append(value)
    elif operator == "/":    #Checks for operator and perform the operation
        if right == 0:
            raise ValueError("Division by zero!")
        values.append(left / right)
precedence = { '+' : 1 , '-' : 1 , '*' : 2 , '/' :2}    #Gives precedence to the operation with greater value
operators = []
values = []

for token in tokens:
    if isinstance(token, int): #Checks if the token is int or not
        values.append(token) #If int the appends it to token
    elif(token =="(" ): 
        operators.append(token)
    elif(token ==")"):
        while(operators and operators[-1]!="("):
            evaluate(values,operators)
        operators.pop()
    else:
        while (operators and operators[-1] in precedence and precedence[operators[-1]] >= precedence[token]):
            evaluate(values,operators)
        operators.append(token)  
while(operators):
    evaluate(values,operators)


print(f"The Answer of {exp} is : {values[-1]}")
