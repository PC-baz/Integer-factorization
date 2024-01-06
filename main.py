import argparse
import math as mt

parser = argparse.ArgumentParser(description="Takes a number and returns the Prime-Factor bar.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("number", help="Number that takes")
args = parser.parse_args()

config = vars(args)
num = int(config['number'])
def check_prime(number):
   if number < 2:
       return False
   for i in range(2, number):
       if number % i == 0:
           return False
   return True

def main(num):
        while num % 2 == 0:
            yield 2
            num = num // 2
        for i in range(3,int(mt.sqrt(num))+1,2):
            if num <= i:
                break
            while num % i == 0:
                yield i
                num = num // i
        if num > 2:
            yield num
def generator2str(number):
    return '*'.join(map(lambda x: str(x), main(number)))
if __name__ == '__main__':
    print(generator2str(num))
    pass

