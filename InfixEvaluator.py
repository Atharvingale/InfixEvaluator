exp = "(5+5)*(5+6)svsdfb*50"
tokens = []
number = ""
for char in exp:
    if char.isdigit():
        number += char
    else:
        if number:
            tokens.append(int(number))  # Convert the number to an integer
            number = ""
        if char in "+-*/()":
            tokens.append(char)
if number:
    tokens.append(int(number))
def evaluate(values,operators):
    right = values.pop()
    left = values.pop()
    operator = operators.pop()
    if operator == "+":
        value = right + left
        values.append(value)
    elif operator == "-":
        value = left - right
        values.append(value)
    elif operator == "*":
        value = left * right
        values.append(value)
    elif operator == "/":
        if right == 0:
            raise ValueError("Division by zero!")
        values.append(left / right)
precedence = { '+' : 1 , '-' : 1 , '*' : 2 , '/' :2}   
operators = []
values = []

for token in tokens:
    if isinstance(token, int):
        values.append(token)
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