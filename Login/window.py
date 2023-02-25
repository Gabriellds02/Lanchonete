from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("430x549")
window.configure(bg = "#202122")
canvas = Canvas(
    window,
    bg = "#202122",
    height = 549,
    width = 430,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    241.5, 399.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 129, y = 381,
    width = 225,
    height = 34)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    241.5, 337.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 129, y = 319,
    width = 225,
    height = 34)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    206.0, 193.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 163, y = 470,
    width = 158,
    height = 57)

window.resizable(False, False)
window.mainloop()
