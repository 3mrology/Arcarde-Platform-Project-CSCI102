from tkinter import *
import subprocess
def btn_clicked():
    print("Button Clicked")
def pong():
    subprocess.run("pong.exe")
def Mine():
    subprocess.run("test2.exe")
def snake():
    subprocess.run("snake.exe")


window = Tk()

window.geometry("1068x691")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 691,
    width = 1068,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    564.0, 345.5,
    image=background_img)


img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = pong,
    relief = "flat")

b1.place(
    x = 331, y = 484,
    width = 102,
    height = 102)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = Mine,
    relief = "flat")

b2.place(
    x = 465, y = 478,
    width = 120,
    height = 107)

img3 = PhotoImage(file = f"snake2.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = snake,
    relief = "flat")

b3.place(
    x = 616, y = 476,
    width = 113,
    height = 102)


window.resizable(False, False)
window.mainloop()
