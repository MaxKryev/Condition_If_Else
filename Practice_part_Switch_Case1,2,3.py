"""
Задание 1
"""
K = int(input())
def get_mark(K: int) -> str:
    if K in [1, 2, 3, 4, 5]:
        result = ""
        if K == 1:
            result = "плохо"
        elif K == 2:
            result = "неудовлетворительно"
        elif K == 3:
            result = "удовдетворительно"
        elif K == 4:
            result = "хорошо"
        elif K == 5:
            result = "отлично"
        return result
    else:
        return "ошибка"


answer = get_mark(K)
print(answer)
"""
Задание 2
"""
month = int(input())
if 1 <= month <= 12:
    if month == 2:
        print("28 дней")
    elif month in [4, 6, 9, 11]:
        print("30 дней")
    else:
        print("31 день")
else:
    print("Введен некорректный номер месяца")
"""
Задание 3
"""
D = int(input("Введите день: "))
M = int(input("Введите месяц: "))
next_D = D + 1
if M == 2:
    if D == 28:
        next_D = 1
        M += 1
        print(next_D, M)
    else:
        print(next_D, M)
elif M in [4, 6, 9, 11]:
    if D == 30:
        next_D = 1
        M += 1
        print(next_D, M)
    else:
        print(next_D, M)
elif M in [1, 3, 5, 7, 8, 10]:
    if D == 31:
        next_D = 1
        M += 1
        print(next_D, M)
    else:
        print(next_D, M)
elif M == 12:
    if D == 31:
        next_D = 1
        M = 1
        print(next_D, M)
else:
    print(next_D, M)
