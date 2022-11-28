import time


def tim(x):
    time.sleep(x)
    y = int(input("Введите число \n"))
    if y >= 0:
        tim(y)
    else:
        print("Заверешно")


a = int(input("Введите число \n"))
if a >= 0:
    tim(a)
else:
    print("Заверешно")