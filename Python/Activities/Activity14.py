
def generate_fibonacci(n):
    fib_sequence = [1, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

num_fibonacci = int(input("How many Fibonacci numbers would you like to generate? "))

fib_sequence = generate_fibonacci(num_fibonacci)
print("The first", num_fibonacci, "Fibonacci numbers are:")
print(fib_sequence)
