def input(n):
# проверяем является ли число целым
    n = input("Введите число: ")

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("неправильно ввели!")
        n = input("Введите целое число: ")



