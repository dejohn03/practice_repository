#ractice Problem: Iterate through the first 10 numbers (0–9). In each iteration,
#  print the current number, the previous number, and their sum.
print("printing current and provious number  sum in a range(10)")

previous_num = 0
#loop form 0 to 9

for current_num in range(10):
    current_sum = current_num + previous_num
    print(f"current Number {current_num} provious Number {previous_num} sum: {current_sum}")
    #update previous_num for the next loop

    previous_num = current_num
