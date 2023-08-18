#!/usr/bin/env python3

def print_fibonacci(length):
    a= 0; b= 1
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) <= length:
        new_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(new_number)

    print(fibonacci_sequence)


print_fibonacci(9) 