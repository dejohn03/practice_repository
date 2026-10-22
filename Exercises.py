# 1. Print a box like the one below.
for i in range(5):
    print("*" * 30)
print("=" * 30)

# 2. Print a box like the one below.

for i in range (6):
    print("*" * i)

print("=" * 30)
# 3. Print a triangle like the one below.


for i in range(4):
    if i == 0 or i == 3:
        print("*" * 30)
    else:
        print("*"," " * 26,"*")

print("=" * 30)
# 4. Write a program that computes and prints the result of 512 − 282
# 47 · 48 + 5
# . It is roughly .1017

print((512-282)/(47*48+5))

print("=" * 30)
# 5. Ask the user to enter a number. Print out the square of the number, but use the sep optional
# argument to print it out in a full sentence that ends in a period. Sample output is shown
# below.
# Enter a number: 5
# The square of 5 is 25



def number(num):

    return(f"The square of {num} is {num * num}")
num1 = int(input("Enter number: "))
print(number(num1))

print("=" * 30)

# 6. Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x,
# and 5x, each separated by three dashes, like below.
# Enter a number: 7
# 7---14---21---28---35



def sep(sep):
    cell = []    
    for i in range(1, 6):
        cell.append(str(sep * i))
    return ("---".join(cell))

num = int(input("Enter: ")) 
print(sep(num))

print("=" * 30 )
# 7. Write a program that asks the user for a weight in kilograms and converts it to pounds. There
# are 2.2 pounds in a kilogram.


kilogram = float(input("Enter the weight in kilogram: "))
pounds = 2.2
print(f"{kilogram} kilogramn is equal to {pounds} pounds.")

# 8. Write rate input statements). a program that asks the user to enter three numbers 
# (use three sepaCreate variables called total and average that hold the sum and average of the
# three numbers and print out the values of total and average.
print("=" * 30)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

total = num1 + num2 + num3 
average = total / 3
print(f"total: {average}")
print(f"average: {total}")

print("=" * 30)
# 9. A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
# the percent tip they want to leave. Then print both the tip amount and the total bill with the
# tip included.

meal_price = float(input("Enter the price of the meal: ₦ "))
tip_percent = float(input("Enter the tip percent you want to leave (10): "))
tip_amount = meal_price * (tip_percent/ 100)
total_bill = meal_price + tip_amount

print(f"Tip amonut: #{tip_amount}")
print(f"Total bill (with tip): ₦{total_bill}")