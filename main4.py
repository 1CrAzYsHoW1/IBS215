a = int(input("Обьем первого= "))
b = int(input("Обьем второго= "))
k = int(input("масса первого= "))
d = int(input("масса второго= "))
p1 = a/k
p2 = b/d 
if p1>p2:
    print("Первое имеет большую плотность")
else:
    print("Второе имеет большую плотность")