from test3 import is_year_leap

def input_year():
    # проверяем является ли число целым
    while True:
        try:
            n = int(input("Введите год: "))
            if n > 0:
                if n > 2050:
                    print('max 2050')
                    continue
                return n
        except:
            print("ошибка")

def main():
    while True:
        year = input_year()
        if is_year_leap(year):
            print('високосный')
        else:
            print('невисокосный')
        answer = input('Хотите еще проверить (y/n)')
        if answer == 'n':
            break


if __name__ == '__main__':
    main()

