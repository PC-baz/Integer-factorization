# Check if number is Odd or Even.
def check_even_odd(number):
   if number % 2 == 0:
       return "Even"
   else:
       return "Odd"

# Check if number is Divisible by 3.
def check_divisible_by_3(number):
   if number % 3 == 0:
       return True
   else:
       return False

# Check if number is Divisible by 5.
def check_divisible_by_5(number):
   if number % 5 == 0:
       return True
   else:
       return False

# Check if number is Divisible by 7.
def check_divisible_by_7(number):
   if number % 7 == 0:
       return True
   else:
       return False

# Check if number is Divisble by 11.
def check_divisible_by_11(number):
   if number % 11 == 0:
       return True
   else:
       return False

# Check if number is Divisble by 13.
def check_divisible_by_13(number):
   if number % 13 == 0:
       return True
   else:
       return False

# Check if number is a Prime number.
def check_prime(number):
   if number < 2:
       return False
   for i in range(2, number):
       if number % i == 0:
           return False
   return True

# Check if number is a Perfect number.
def check_perfect(number):
   sum = 0
   for i in range(1, number):
       if number % i == 0:
           if i != number and i != 1:
            sum += i
            return sum