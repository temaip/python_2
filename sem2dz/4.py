#4 - Реализуйте выдачу случайного числа
#не использовать random.randint и вообще библиотеку random
#Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
#Учтите, что есть диапазон: от(минимальное) и до (максимальное)


numbers = int(input('введите кол-во цифр '))
def random(a):
    count = 0
    import datetime
    time = datetime.datetime.now()
    time = str(time)
    time_now = int(time[-6])
    randoms = a
    while count < a:
        randoms = randoms * time_now
        count +=1
        if randoms > 99:
            randoms = randoms/10
        print(round(randoms),end=' ')
random(numbers)