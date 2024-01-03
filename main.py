<<<<<<< HEAD
from lib_s import *

def main(num):
    # Check if number is Odd or Even by using lib_s.
    # lib_s.py is a library file that contains a function to check if a number is odd or even.
    # The function is called check_even_odd() and takes a single integer parameter.
    # The function returns a string "odd" or "even".
    # The function is imported at the top of the script using "from lib_s import *".
    Parsing_bar = "1"
    if num == 1:
        print(Parsing_bar)
        return
    if check_prime(num):
        print(Parsing_bar + "*" + str(num))
        return
    if check_even_odd(num) == "Odd":
        pr = num
        while check_prime(num) == False:
            Parsing_bar = "1"
            if check_divisible_by_3(num):
                Parsing_bar += "*3"
                num = num // 3
            if check_divisible_by_5(num):
                Parsing_bar += "*5"
                num = num // 5
            if check_divisible_by_7(num):
                Parsing_bar += "*7"
                num = num // 7
            if check_divisible_by_11(num):
                Parsing_bar += "*11"
                num = num // 11
            if check_divisible_by_13(num):
                Parsing_bar += "*13"
                num = num // 13
            if check_prime(num):
                Parsing_bar += "*" + str(num)
                print(Parsing_bar)
                break
            elif num == 1:
                pass
            else:
                Parsing_bar += "*" + str(check_perfect(num))
                num = num // check_perfect(num)
            if check_prime(num):
                Parsing_bar += "*" + str(num)
            if eval(Parsing_bar) == pr:
                print(Parsing_bar)
                break
    else:
        pr = num
        while check_prime(num) == False:
            if check_even_odd(num) == "Even":
                Parsing_bar += "*2"
                num = num // 2
            if check_divisible_by_3(num):
                Parsing_bar += "*3"
                num = num // 3
            if check_divisible_by_5(num):
                Parsing_bar += "*5"
                num = num // 5
            if check_divisible_by_7(num):
                Parsing_bar += "*7"
                num = num // 7
            if check_divisible_by_11(num):
                Parsing_bar += "*11"
                num = num // 11
            if check_divisible_by_13(num):
                Parsing_bar += "*13"
                num = num // 13
            if check_prime(num):
                Parsing_bar += "*" + str(num)
            if eval(Parsing_bar) == pr:
                print(Parsing_bar) 
=======
from lib_s import *

def main(num):
    # Check if number is Odd or Even by using lib_s.
    # lib_s.py is a library file that contains a function to check if a number is odd or even.
    # The function is called check_even_odd() and takes a single integer parameter.
    # The function returns a string "odd" or "even".
    # The function is imported at the top of the script using "from lib_s import *".
    # Check if the number is odd or even and print the result.
    Parsing_bar = "1"
    if num == 1:
        print(Parsing_bar)
        return
    if check_prime(num):
        print(Parsing_bar + "*" + str(num))
        return
    if check_even_odd(num) == "Odd":
        pr = num
        while check_prime(num) == False:
            Parsing_bar = "1"
            if check_divisible_by_3(num):
                Parsing_bar += "*3"
                num = num // 3
            if check_divisible_by_5(num):
                Parsing_bar += "*5"
                num = num // 5
            if check_divisible_by_7(num):
                Parsing_bar += "*7"
                num = num // 7
            if check_divisible_by_11(num):
                Parsing_bar += "*11"
                num = num // 11
            if check_divisible_by_13(num):
                Parsing_bar += "*13"
                num = num // 13
            if check_prime(num):
                Parsing_bar += "*" + str(num)
                print(Parsing_bar)
                break
            elif num == 1:
                pass
            else:
                Parsing_bar += "*" + str(check_perfect(num))
                num = num // check_perfect(num)
            if check_prime(num):
                Parsing_bar += "*" + str(num)
            if eval(Parsing_bar) == pr:
                print(Parsing_bar)
                break
    else:
        pr = num
        while check_prime(num) == False:
            if check_even_odd(num) == "Even":
                Parsing_bar += "*2"
                num = num // 2
            if check_divisible_by_3(num):
                Parsing_bar += "*3"
                num = num // 3
            if check_divisible_by_5(num):
                Parsing_bar += "*5"
                num = num // 5
            if check_divisible_by_7(num):
                Parsing_bar += "*7"
                num = num // 7
            if check_divisible_by_11(num):
                Parsing_bar += "*11"
                num = num // 11
            if check_divisible_by_13(num):
                Parsing_bar += "*13"
                num = num // 13
            if check_prime(num):
                Parsing_bar += "*" + str(num)
            if eval(Parsing_bar) == pr:
                print(Parsing_bar) 
>>>>>>> b4557b3 (Edited)
                break