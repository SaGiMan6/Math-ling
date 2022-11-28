import tkinter as tk


root = tk.Tk()

root.geometry("200x150+100+100")

root.title("Calc")


ch1 = tk.Entry(root, width=29).place(x=10, y=5)
ch2 = tk.Entry(root, width=29).place(x=10, y=30)

otv = tk.Label(width=24, height=1, text="")

def b_pl():
    otv["text"] = ""
    try:
        otv["text"] = str("Ответ: " + f"{int(ch1.tk.get()) + int(ch2.tk.get())}")
    except:
        otv["text"] = ("Ошибка")
    otv.place(x=10, y=125)

def b_mn():
    otv["text"] = ""
    try:
        otv["text"] = str("Ответ: " + f"{int(ch1.tk.get()) - int(ch2.tk.get())}")
    except:
        otv["text"] = ("Ошибка")
    otv.place(x=10, y=125)

def b_mlt():
    otv["text"] = ""
    try:
        otv["text"] = str("Ответ: " + f"{int(ch1.tk.get()) * int(ch2.tk.get())}")
    except:
        otv["text"] = ("Ошибка")
    otv.place(x=10, y=125)

def b_dvd():
    otv["text"] = ""
    try:
        otv["text"] = str("Ответ: " + f"{int(ch1.tk.get()) / int(ch2.tk.get())}")
    except:
        otv["text"] = ("Ошибка")



pl = tk.Button(root, text="+", justify="center", height=2, width=5, command=b_pl())
mn = tk.Button(root, text="-", justify="center", height=2, width=5, command=b_mn())
mlt =tk.Button(root, text="*", justify="center", height=2, width=5, command=b_mlt())
dvd =tk.Button(root, text="/", justify="center", height=2, width=5, command=b_dvd())




pl.place(x=10, y=57)
mn.place(x=55, y=57)
mlt.place(x=100, y=57)
dvd.place(x=145, y=57)


root.mainloop()
