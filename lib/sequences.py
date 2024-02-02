#!/usr/bin/env python3

def print_fibonacci(length):
    fib_seq = []
    # if (length == 0):
    #     return fib_seq
    for i in range(length):
        if (i == 0):
            fib_seq.append(0)
        elif i == 1:
            fib_seq.append(1)
        else:
            prev_2_num = fib_seq[-2]
            prev_1_num = fib_seq[-1]
            new_num = prev_2_num + prev_1_num
            fib_seq.append(new_num)
    print(fib_seq)
    pass

print_fibonacci(9)