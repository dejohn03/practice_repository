def second_largest(numbers):
    largest = None
    second = None 

    for number in numbers:
        if largest is None or number > largest:
           second = largest
           largest = number
        elif number != largest and (second is None or number > second):
            second = number
    return second            

print(second_largest([10, 5, 8, 10, 3]))
print(second_largest([4, 4, 4]))
print(second_largest([-5, -2, -8 -3]))