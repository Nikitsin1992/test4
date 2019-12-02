from test3 import is_year_leap #делаем импорт функции test3

def input_year(): #название функции
    while True: #задаем то что проверяет цикл
        try: #пробуем что-то выполнить
            n = int(input("Введите год: "))  #просим с экрана ввести данные (число)
            if n > 0: #проверяем что n ,больше 0
                if n > 2050: #проверяем чтобы число не было больше чем 2050
                    print('max 2050') #выводим на экран это значение если число больше 2050
                    continue #в случае ошибки, продолжает работу цикла со след операции
                return n #возвращает н
        except: #кроме ощибки
            print("ошибка") #выводит ошибку на экран

def main(): #название функции
    while True: #задаем то что проверяет цикл
        year = input_year() #присваем новое значение
        if is_year_leap(year): #проверяем является ли год високосным
            print('високосный') #выводим на экран такое значение если год високосный
        else: #еще
            print('невисокосный') #выводим на экран такое значение если год не високосный
        answer = input('Хотите еще проверить (y/n)') #просим с экрана подтвердить повтор проверки года
        if answer == 'n': #если ответ равен н, то прерываем цикл
            break #прерываем весь цикл


if __name__ == '__main__': #меняем расширения файла питон
    main()

