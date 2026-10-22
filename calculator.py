print("=" * 30)
print("MY TERMINAL CALCLULATOR")
print("=" * 30)

num1 = float(input("Enter first number:"))
operator = input("Enter operator(+,-,*,/):")
num2 = float(input("Enter second number:"))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2        
elif operator == "/":
    result = num1 / num2
    if num2 == 0:
        result = "error divide by zero is not allow"

    else:    
        result = num1 / num2

else:

    result = "invaild operator enter"


print("=" * 30)
print("Result:", result)
print("=" * 30)          


