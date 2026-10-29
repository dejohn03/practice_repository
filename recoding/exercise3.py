def find_smallest(numbers):
    if len(numbers) == 0:
        return None 
    smallest = numbers[0]
    for number in numbers:
       if number < smallest:
        smallest = number
    return smallest # if smallest != float('-inf') else None
print(find_smallest([8, 3, 12, 1, 7])) 
print(find_smallest([-3, -10, -1, -6]))   
print(find_smallest([-3, -3, -10, -1, -6, -99]))   


