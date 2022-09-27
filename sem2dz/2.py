#2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
#Не используйте функцию math.factorial.
#Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.



try: 
    n = int(input('Input number n and output mult list'))
 
    factorial = 1
    print(factorial)
    for i in range(2, n+1): 
        factorial *= i 
        print(factorial)
        
    
except ValueError:
    print('error input')

n = int(input("input n")) 
f = 1

while n > 1:
    f = f * n
    n = n - 1 
print(f)

n = int(input("input n")) 
f = 1

for i in range(2, n+1):
    f = f * i
print(f)