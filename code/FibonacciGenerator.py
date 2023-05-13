# Function that calculates the Fibonacci number for a number n
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Function that creates a file of Fibonacci numbers up to n
def create_fibonacci_file(n):
    with open(f'fibonacci_{n}.txt', 'w') as f:
        for i in range(n+1):
            f.write(f'{fibonacci(i)}\n')

# Main function that calls create_fibonacci_file for Fibonacci numbers up to n
def main():
    n = int(input("Give a number for the Fibonacci numbers: "))
    create_fibonacci_file(n)

if __name__ == '__main__':
    main()
