Fibonacci-Generator:

This repository contains a Python program to create a file with the numbers of the Fibonacci series.

Description:

The Fibonacci sequence is a sequence of numbers where each number consists of the sum of the previous two numbers. The sequence starts with the numbers 0 and 1.

This particular implementation of the Fibonacci sequence uses a generator function to calculate the Fibonacci number for a given number n. The generator function is defined in the file fibonacci_generator.py.

In addition, there is a function to create a file with the numbers of the Fibonacci series up to a certain number n. This function is defined in the file create_fibonacci_file.py. The file is created with the format "fibonacci_n.txt", where n is the number up to which the Fibonacci numbers are generated.

Usage:

To generate the Fibonacci numbers and create the file, you can run the main.py script. The script will prompt you to input a number n, and then it will generate the first n Fibonacci numbers and save them in a file named fibonacci_n.txt.

To run the program, use the following command:
                        python main.py

About the tests:

There are two test scripts, test_fibonacci.py and test_create_fibonacci_file.py, that check the correctness of the functions fibonacci and create_fibonacci_file, respectively.

To run the tests, you can use the following commands:
                            python test_fibonacci.py
                            python test_create_fibonacci_file.py

These tests will ensure that the functions calculate the correct Fibonacci numbers and create the file with the correct content. If all tests pass, it means that the program is working as expected.
