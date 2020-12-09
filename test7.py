#расчитываем факториал

def factorial (number : int):
    result = 1
    for item in range(1,number + 1):
        result = result * item
    return result

print(factorial(int(input())))