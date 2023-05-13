from fibonacci import fibonacci

def create_fibonacci_file(n):
    with open(f'fibonacci_{n}.txt', 'w') as f:
        for i in range(n+1):
            f.write(f'{fibonacci(i)}\n')
