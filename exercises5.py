
intervals = [
    [1, 3],
    [2, 6],
    [8, 10],
    [9, 12]
]


def merge_intervals(intervals):
    if not intervals:
        return []

    # Step 1: Sort intervals by their starting number
    intervals.sort(key=lambda interval: interval[0])

    # Step 2: Create a list to store merged intervals
    merged = []

    # Step 3: Start with the first interval
    current = intervals[0]

    # Step 4: Check the remaining intervals
    for next_interval in intervals[1:]:

        # Check if the intervals overlap
        if next_interval[0] <= current[1]:

            # Merge them by keeping the start
            # and choosing the larger ending number
            current[1] = max(current[1], next_interval[1])

        else:
            # No overlap: save the current interval
            merged.append(current)

            # Start a new current interval
            current = next_interval

    # Step 5: Save the final interval
    merged.append(current)

    return merged


result = merge_intervals(intervals)
print(result)
