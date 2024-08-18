"""
Задание 4
"""
C = input("Введите направление: ")
N = int(input("Введите действие: "))
if N == 1 and C == "N":
    C = "W"
elif N == 1 and C == "W":
    C = "S"
elif N == 1 and C == "S":
    C = "E"
elif N == 1 and C == "E":
    C = "N"
elif N == -1 and C == "N":
    C = "E"
elif N == -1 and C == "W":
    C = "N"
elif N == -1 and C == "S":
    C = "W"
elif N == -1 and C == "E":
    C = "S"
print("Направление робота:", C)

"""
Задание 5
"""
hundreds = ["сто","двести","триста","четыреста","пятьсот","шестьсот","семьсот","восемьсот","девятьсот"]
tens = ["двадцать","тридцать","сорок","пятьдесят","шестьдесят","семьдесят","восемьдесят","девяносто"]
units = ["один","два","три","четыре","пять","шесть", "семь","восемь","девять"]
first_tens = ["одиннадцать","двенадцать","тринадцать","четырнадцать","пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать"]
number = int(input())
if number not in range(100, 1000):
    breakpoint("Число вне диапазона")
hun = int(number // 100)
ten = number % 100 // 10
un = number % 10
number_name = []
number_name.append(hundreds[hun - 1])
if ten != 1:
    number_name.append("" if ten == 0 else tens[ten - 2])
    number_name.append("" if un == 0 else units[un - 1])
else:
    number_name.append(first_tens[un - 1])

print(*number_name)

"""
Задание 6
"""
number_1 = float(input("Введите число: "))
number_2 = float(input("Введите число: "))
operation = input("Операция: ")
math_oper = ["*", "/", "+", "-"]


def get_result(number_1: float, number_2: float, operation: str) -> float | str:
    if operation == math_oper[0]:
        return number_1 * number_2
    elif operation == math_oper[1]:
        try:
            return number_1 / number_2
        except ZeroDivisionError:
            return 0
    elif operation == math_oper[2]:
        return number_1 + number_2
    elif operation == math_oper[3]:
        return number_1 - number_2
    else:
        return "Введена не математическая операция"


result = get_result(number_1, number_2, operation)
print(result)
