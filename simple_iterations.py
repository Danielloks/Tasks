x1, x2, x3, x4 = 0, 0, 0, 0
tolerance = 0.001

while True:
    # Следующее приближение
    x1_new = (0.06*x1 + 0.17*x2 + 0.34*x3 + 0.16*x4 + 2.43) / (1 - 0.06)
    x2_new = (0.32*x1 + 0.23*x2 - 0.35*x4 - 1.12) / (1 - 0.23)
    x3_new = (0.16*x1 - 0.08*x2 - 0.12*x4 + 0.43) / 1
    x4_new = (0.09*x1 + 0.21*x2 - 0.13*x3 + 0.83) / 1

    # Проверка условия сходимости
    if (abs(x1 - x1_new) <= tolerance and abs(x2 - x2_new) <= tolerance and
        abs(x3 - x3_new) <= tolerance and abs(x4 - x4_new) <= tolerance):
        break

    # Обновление переменных
    x1, x2, x3, x4 = x1_new, x2_new, x3_new, x4_new

print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}")
