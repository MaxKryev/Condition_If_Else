"""
Задание 1
"""
first_number = int(input("Введите первое число "))
second_number = int(input("Введите второе число "))
third_number = int(input("Введите третье число "))

positive_num = 0
if first_number > 0:
    positive_num +=1
if second_number > 0:
    positive_num += 1
if third_number > 0:
    positive_num += 1
print(positive_num)

"""
Задание 2
"""
first_number = int(input("Введите первое число "))
second_number = int(input("Введите второе число "))
if first_number > second_number:
    print(first_number)
else:
    print(second_number)

"""
Задание 3
"""
first_number = int(input("Введите первое число "))
second_number = int(input("Введите второе число "))
print(*([first_number, second_number] if first_number > second_number else [second_number, first_number]))

"""
Задание 4
"""
first_number = int(input("Введите первое число "))
second_number = int(input("Введите второе число "))
third_number = int(input("Введите третье число "))

if ((first_number < second_number) and (first_number < third_number)) or (second_number == third_number):
    print(first_number)
elif ((second_number < first_number) and (second_number < third_number)) or (first_number == third_number):
    print(second_number)
elif ((third_number < first_number) and (third_number < second_number)) or (first_number == second_number):
    print(third_number)

"""
Задание 5
"""
X = int(input("Введите X  "))
Y = int(input("Введите Y  "))

if X > 0 and Y > 0:
    print("I четверть")
elif X < 0 and Y > 0:
    print("II четверть")
elif X < 0 and Y < 0:
    print("III четверть")
elif X > 0 and Y < 0:
    print("IV четверть")