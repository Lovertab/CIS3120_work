# 5. Write a function called fizz_buzz that takes a number.
# - If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# - If the number is divisible by only 3, it should return “Fizz”.
# - If it is divisible by only 5, it should return “Buzz”.
# - Otherwise, it should return the same number.

def fizz_buzz(n):
    if n%3 == 0 and n%5 ==0:
        return 'FizzBuzz'
    elif n%3 ==0:
        return 'FizzBuzz'
    elif n%5 ==0:
        return 'FizzBuzz'
    else:
        return n
    
fizz_buzz(15)
fizz_buzz(10)
fizz_buzz(11)
fizz_buzz(20)