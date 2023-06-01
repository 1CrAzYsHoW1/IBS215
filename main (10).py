years= int(input("Введите количество лет для вклада:"))
a = int(input("Введите сумму вклада:"))
def bank(a, years):
    vsego= a*1.1**years
    return print("Итоговый вклад составляет:", vsego,"рублей")
bank(a,years)