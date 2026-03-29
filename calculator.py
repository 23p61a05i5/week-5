num1 = 10
num2 = 5
op = "+"

print("Basic Calculator")
print(f"Inputs: {num1} {op} {num2}")

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
else:
    result = "Invalid operator"

print("Result:", result)
