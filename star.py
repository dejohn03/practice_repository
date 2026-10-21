for i in range(5):
    print("*" * 30)


print()

for i in range (6):
    print("*" * i)

print()


for i in range(4):
    if i == 0 or i == 3:
        print("*" * 30)
    else:
        print("*"," " * 26,"*")

print()

print((512-282)/(47*48+5))

print()

def number(num):

    return(f"The square of {num} is {num * num}")
num1 = int(input("Enter number: "))
print(number(num1))

print()

def sep(sep):
    cell = []    
    for i in range(1, 6):
        cell.append(str(sep * i))
    return ("---".join(cell))

num = int(input("Enter: ")) 
print(sep(num))