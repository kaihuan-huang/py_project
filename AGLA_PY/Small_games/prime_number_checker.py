#    质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；否则称为合数。
#   0和1既不是质数也不是合数，最小的质数是2

def prime_checker(number):
    is_prime_number = True
    for i in range (2,number):
        if number % i == 0:
            is_prime_number = False
    if is_prime_number:
         print('Prime')
    else:
         print('Not prime')





n = int(input("Check this number: "))
prime_checker(number=n)