a = int(input("Введите трехзначное число: "))
b = a % 10
c = a % 100 // 10
d = a // 100
g = d+c+b
h = a-g
print (h)