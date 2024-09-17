def iterations(x):
    print(f"Вызов функуции iterations({x})")
    result = 0
    while x >= 10:
        x -= 10
        result += 1
    return result

def recursive(x):
    print(f"\tВызов функуции recursive({x})")
    if x < 10:
        return 0
    else:
        return 1 + recursive(x - 10)


while 1:
    try:
        x = int(input("Введите значение x: "))
        print(f"\nИтеративный способ: f({x}) = {iterations(x)}")
        print(f"\tРекурсивный способ: f({x}) = {recursive(x)}")
    except Exception as e:
        print("Пожалуйста, введите корректное целое число.")
       