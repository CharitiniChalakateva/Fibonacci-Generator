from create_fibonacci_file import create_fibonacci_file

# Main function that calls create_fibonacci_file for Fibonacci numbers up to n
def main():
    n = int(input("Give a number for the Fibonacci numbers: "))
    create_fibonacci_file(n)

if __name__ == '__main__':
    main()