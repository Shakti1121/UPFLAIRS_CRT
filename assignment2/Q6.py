# 6. Fibonacci sequence up to n terms
def fibonacci(n):
    fib_series = [0, 1]
    for _ in range(n - 2):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

num_terms = int(input("Enter number of terms: "))
print(fibonacci(num_terms))