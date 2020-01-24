try:
    a=int(input('Введите начальную скорость'))
    b=int(input('Введите конечную скорость'))
    t=int(input('Введите время'))


    if t==0:
        raise MyException('Время не должно быть равно 0')
except ValueError:
    print('Вы должны были ввести числа')
except MyException:
    print('Завершение программы')


def Decorator(Uskorenie):
    def wrapper():
        Uskorenie()
        d=(a+b)*t/2
        print(d)
    return wrapper

@Decorator
def Uskorenie():
    s=(b**2-a**2)/2*((a+b)*t/2)
    print(s)

Uskorenie()





