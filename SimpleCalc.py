def Add(a, b):
	return "TODO";

def Subtract(a, b):
	return "TODO";

def Multiply(a, b):
	return "TODO";

def Divide(a, b):
	return "TODO";

num1 = input("Enter a number: ")
num2 = input("Enter a second number: ")
op = input("Choose an operation (+, -, *, /): ")

result = "Your answer is: "

if (op == "+"):
	result += str(Add(num1, num2))
elif (op == "-"):
	result += str(Subtract(num1, num2))
elif (op == "*"):
	result += str(Multiply(num1, num2))
elif (op == "/"):
	result += str(Divide(num1, num2))
else:
	result = "Invalid operator"

print(result)