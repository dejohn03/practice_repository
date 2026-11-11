def two_middle(items):
    if len(items) < 1:
        return
    mid = len(items) // 2
    if len(items) % 2 == 0:
        return [items[mid], items[mid+1]]
    else:
        return [items[mid+1]]

print(two_middle("DEBORAH"))

