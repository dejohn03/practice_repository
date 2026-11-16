def flatten(numbers: list) -> list:
    flat_list = []
    for item in numbers:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

print(flatten([1, 3, 5, [5, 7], 2]))  # Output: [1, 3, 5, 5, 7, 2]
