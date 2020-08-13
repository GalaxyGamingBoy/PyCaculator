from tkinter import *

# Selects the root
root = Tk()
root.title("Calculator")
root.iconbitmap('Calc.ico')
# Functions
def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


# Declares/Initializes Objects
e = Entry(root)
button_1 = Button(root, text="1", width=12, height=5, command=lambda: button_click(1))
button_2 = Button(root, text="2", width=12, height=5, command=lambda: button_click(2))
button_3 = Button(root, text="3", width=12, height=5, command=lambda: button_click(3))
button_4 = Button(root, text="4", width=12, height=5, command=lambda: button_click(4))
button_5 = Button(root, text="5", width=12, height=5, command=lambda: button_click(5))
button_6 = Button(root, text="6", width=12, height=5, command=lambda: button_click(6))
button_7 = Button(root, text="7", width=12, height=5, command=lambda: button_click(7))
button_8 = Button(root, text="8", width=12, height=5, command=lambda: button_click(8))
button_9 = Button(root, text="9", width=12, height=5, command=lambda: button_click(9))
button_0 = Button(root, text="0", width=12, height=5, command=lambda: button_click(0))
button_add = Button(root, text="+", width=12, height=5, command=button_add)
button_min = Button(root, text="-", width=12, height=5, command=button_subtract)
button_mul = Button(root, text="*", width=12, height=5, command=button_multiply)
button_dev = Button(root, text="/", width=12, height=5, command=button_divide)
button_equ = Button(root, text="=", width=12, height=5, command=button_equal)
button_clr = Button(root, text="Clear", width=12, height=5, command=button_clear)
# Displays to screen
# Row 4
button_clr.grid(column=0, row=4)
button_0.grid(column=1, row=4)
button_equ.grid(column=2, row=4)
button_add.grid(column=3, row=4)
# Row 3
button_1.grid(column=0, row=3)
button_2.grid(column=1, row=3)
button_3.grid(column=2, row=3)
button_min.grid(column=3, row=3)
# Row 2
button_4.grid(column=0, row=2)
button_5.grid(column=1, row=2)
button_6.grid(column=2, row=2)
button_mul.grid(column=3, row=2)
# Row 1
button_7.grid(column=0, row=1)
button_8.grid(column=1, row=1)
button_9.grid(column=2, row=1)
button_dev.grid(column=3, row=1)
# Row 0
e.grid(column=0, row=0, columnspan=4, padx=48, pady=5)
# Main Loop
root = mainloop()
