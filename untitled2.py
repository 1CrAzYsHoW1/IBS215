#1
def zahadka():
    popitka=0
    while popitka<5:
        print("Загадка 1: Без окон и дверей, полна глазами лес.Что это?")
        answer1 = input()
        if answer1.lower() == "елка" or answer1.lower() == "ёлка":
            print("Правильно!")
            
        else:
            print("Неправильно!")
        print("Загадка 2: Никто не видит, а все знают. Разговаривает, а не шевелится.Что это?")
        answer2 = input()
        if answer2.lower() == "эхо":
            print("Правильно!")
            break
        else:
            print("Неправильно!")
        print("Загадка 3: Два брата — венцокардиналова,Старший б без труда родился в Ватикане, младший – в любой точке земного шара.Что это?")
        answer3 = input()
        if answer3.lower() == "северный и южный полюс":
            print("Правильно!")
            break
        else:
            print("Неправильно!")
            popitka+=1
            if popitka>=5:
                print("Все попытки использованы")

zahadka()