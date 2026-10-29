""" Write a Python function named find_largest(numbers)
 that takes a list of numbers and returns the largest number in the list."""


def find_largest(numbers):
    if len(numbers) == 0:
        return None 
    
    largest = numbers[0]
    for number in numbers:
          if number > largest:
                largest = number 
    return largest

print(find_largest([3, 14, 56, 76, 9]))        
print(find_largest([-10, -5, -2, -18]))
print(find_largest([]))
