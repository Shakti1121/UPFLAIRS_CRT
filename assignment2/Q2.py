# 2. Explanation of `continue`:
"""
The `continue` statement skips the remaining code inside the loop for the current iteration and moves to the next iteration.
It is useful when we want to avoid executing certain code under specific conditions without breaking the entire loop.

Example: Filtering numbers divisible by 3
"""
numbers = [1, 3, 5, 6, 9, 12, 15, 20]
for num in numbers:
    if num % 3 != 0:
        continue  # Skip numbers not divisible by 3
    print(num)  # Output: 3, 6, 9, 12, 15