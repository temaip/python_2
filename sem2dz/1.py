#1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
#Учтите, что числа могут быть отрицательными


from sre_parse import DIGITS
from string import digits


num = input('Введите число ') 
num=num.replace('.','')  
num=int(num) 
num = abs(num) 
655
sum = 0
while num != 0:
    sum = sum + num % 10 
    num = num // 10
print(f'sum=: {sum}')
