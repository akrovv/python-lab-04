from tkinter import *
from math import acos, sqrt, pi

array_coords = []


def paint(event):
    global array_coords

    x1, y1, x2, y2 = (event.x - 3), (event.y - 3), (event.x + 3), (event.y + 3)

    colour = "#000fff000"

    canvas.create_oval(x1, y1, x2, y2, fill=colour)

    array_coords.append([event.x, event.y])



def show_dot(x, y):
    x1, y1, x2, y2 = (x - 3), (y - 3), (x + 3), (y + 3)

    colour = "#000fff000"

    canvas.create_oval(x1, y1, x2, y2, fill=colour)


def clean_table():
    entry_x.delete(0, END)
    entry_y.delete(0, END)


def erase():
    global array_coords
    canvas.delete("all")
    array_coords.clear()
    result.config(stat=NORMAL)
    result.delete(0, END)
    result.config(stat=DISABLED)


def calculate_angle():
    min_angle = 0
    for i in range(len(array_coords) - 2):
        ab = sqrt(
            (array_coords[i + 1][0] - array_coords[i][0]) ** 2 + (array_coords[i + 1][1] - array_coords[i][1]) ** 2)
        ac = sqrt(
            (array_coords[i + 2][0] - array_coords[i][0]) ** 2 + (array_coords[i + 2][1] - array_coords[i][1]) ** 2)
        bc = sqrt((array_coords[i + 2][0] - array_coords[i + 1][0]) ** 2 + (
                array_coords[i + 2][1] - array_coords[i + 1][1]) ** 2)

        angle_ab = acos((bc ** 2 + ac ** 2 - ab ** 2) / (2 * bc * ac))
        angle_ac = acos((ab ** 2 + ac ** 2 - bc ** 2) / (2 * ab * ac))
        angle_bc = acos((ab ** 2 + bc ** 2 - ac ** 2) / (2 * ab * bc))

        min_angle = max(angle_ab, angle_ac, angle_bc, min_angle)

    return min_angle * 180 / pi


def show_result(res):
    result.config(stat=NORMAL)
    result.delete(0, END)
    result.insert(0, res)
    result.config(stat=DISABLED)


def on_button(key):
    if key == 1:
        x = entry_x.get()
        y = entry_y.get()

        if x.isdigit() and y.isdigit():
            show_dot(int(x), int(y))
            clean_table()
        else:
            return 1
    elif key == 2:
        res = calculate_angle()
        if res == 0:
            return 1
        show_result("{:.6f}".format(res) + "°")
    else:
        erase()


planimetric = Tk()
planimetric.title('Планиметрические задачи')

# Поле для рисования
canvas = Canvas(planimetric, width=600, height=920, bg='white')
canvas.bind("<Button-1>", paint)

# Кнопки
clear = Button(planimetric, text="Стереть", width=100, command=lambda: on_button(3))
calculate = Button(planimetric, text="Посчитать", width=100, command=lambda: on_button(2))
point = Button(planimetric, text="Поставить точку", command=lambda: on_button(1))

# Текст
label_x = Label(text="x:")
label_y = Label(text="y:")

# Поле ввода
entry_x = Entry()
entry_y = Entry()
result = Entry(width=100)

# Размещение
canvas.pack(side=LEFT)
label_x.pack(anchor=N)
entry_x.pack(anchor=N)
label_y.pack(anchor=N)
entry_y.pack(anchor=N)
point.pack(anchor=N)
clear.pack(side=BOTTOM)
calculate.pack(side=BOTTOM)
result.pack(side=RIGHT)

# Настройка
planimetric.resizable(0, 0)
planimetric.geometry('920x700')
result.config(stat=DISABLED)

planimetric.mainloop()
