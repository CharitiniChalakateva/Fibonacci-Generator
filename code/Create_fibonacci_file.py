from fibonacci_generator import fibonacci_generator

# Function that creates a file of Fibonacci numbers up to n
def create_fibonacci_file(n):
    with open(f'fibonacci_{n}.txt', 'w') as f:
        for num in fibonacci_generator(n):
            f.write(f'{num}\n')