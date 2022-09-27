#3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
 

def check_pal(n):
    res = 0
    while n != 0:
        digit=n%10
        res = res*10+digit 
        n = n//10
    return res
    
try:
    num = int(input('input number and check palindrom'))
    palindrom = check_pal(num)
    if num == palindrom:
        print('input number is palindrom')
    else:
        while num != palindrom:
            num = num + palindrom
            palindrom=check_pal(num)
        print(f'output palindrom {num}')

except ValueError:
    print('error')

