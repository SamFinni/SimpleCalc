def Add(a, b):
	return a + b
def TestAdd():
	assert Add(12.0, 7.0) == 19.0
	assert Add(5.0, 36.0) == 41.0
	assert Add(61.0, 532.0) == 593.0

def Subtract(a, b):
	return a - b
def TestSubtract():
	assert Subtract(12.0, 7.0) == 5.0
	assert Subtract(5.0, 36.0) == -31.0
	assert Subtract(61.0, 532.0) == -471.0

def Multiply(a, b):
	return "TODO"

def Divide(a, b):
	return "TODO"


# start execution #

#testMode = True
testMode = False

if (not testMode):
	num1 = float(input("Enter a number: "))
	num2 = float(input("Enter a second number: "))
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
else:
	TestAdd()
	TestSubtract()

	print("All tests passed")