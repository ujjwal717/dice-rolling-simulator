import random
import tkinter as tk
def roll_d4():
    a = random.randint(1, 4)
    result = str(a)
    result_label.config(text="Result: " + result)
def roll_d6():
    a = random.randint(1, 6)
    result = str(a)
    result_label.config(text="Result: " + result)
def roll_d8():
    a = random.randint(1, 8)
    result = str(a)
    result_label.config(text="Result: " + result)
def roll_d10():
    a = random.randint(1, 10)
    result = str(a)
    result_label.config(text="Result: " + result)
def roll_d12():
    a = random.randint(1, 12)
    result = str(a)
    result_label.config(text="Result: " + result)
def roll_d20():
    a = random.randint(1, 20)
    result = str(a)
    result_label.config(text="Result: " + result)
def roll_d30():
    a = random.randint(1, 30)
    result = str(a)
    result_label.config(text="Result: " + result)
def roll_d50():
    a = random.randint(1, 50)
    result = str(a)
    result_label.config(text="Result: " + result)
def roll_d100():
    a = random.randint(1, 100)
    result = str(a)
    result_label.config(text="Result: " + result)


window = tk.Tk()
window.title("DICE ROLLING SIMULATOR ")

label = tk.Label(window, text="D4 means dice having digits 1 to 4 and so on. ")
label.pack()

roll_d4_button = tk.Button(window, text=" ROLL D4 ", command=roll_d4)
roll_d4_button.pack()

roll_d6_button = tk.Button(window, text=" ROLL D6 ", command=roll_d6)
roll_d6_button.pack()

roll_d8_button = tk.Button(window, text=" ROLL D8 ", command=roll_d8)
roll_d8_button.pack()

roll_d10_button = tk.Button(window, text=" ROLL D10 ", command=roll_d10)
roll_d10_button.pack()

roll_d12_button = tk.Button(window, text=" ROLL D12 ", command=roll_d12)
roll_d12_button.pack()

roll_d20_button = tk.Button(window, text=" ROLL D20 ", command=roll_d20)
roll_d20_button.pack()

roll_d30_button = tk.Button(window, text=" ROLL D30 ", command=roll_d30)
roll_d30_button.pack()

roll_d50_button = tk.Button(window, text=" ROLL D50 ", command=roll_d50)
roll_d50_button.pack()

roll_d100_button = tk.Button(window, text=" ROLL D100 ", command=roll_d100)
roll_d100_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
