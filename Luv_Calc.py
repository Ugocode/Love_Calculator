from tkinter import *
from tkinter import ttk
from random import randint
from tkinter.messagebox import showinfo


win = Tk()
win.title('Love Calculator')
win.configure(bg = 'black')
win.geometry('490x670+0+0')
win.iconbitmap('lovei.ico')

# Place a photo
photo1 = PhotoImage(file = 'love.png')
Label(win, image = photo1, bg = 'black').grid(row=0, column=0)

# Write a Heading
Label(win, text = 'Calculate You Love Percentage', bg = 'black', font = ('Arial 14 bold'), fg = 'red').grid(row = 1, column = 0)

# Lets make our calculating function
def calculate():
    number = randint(50, 100)
    showinfo('Love Percentage', f'Your Love Percentage is :  {number} %')


# Where to fill in the information
Label(win, text = '', bg = 'black').grid(row = 2, column = 0)

Label(win, text = 'Enter your lovers name: ', bg = 'black', fg = 'white', font = ('arial 12')).grid(row = 3, column = 0, sticky = W)

# Create and Entry box for the name
entry1 = Entry(win, bg = 'white', font = ('arial 10 bold')). grid(row = 3, column =0, padx = 15)

# Creating a space inbetween
Label(win, text = '', bg = 'black').grid(row = 4, column = 0)

#
Label(win, text = 'Enter your name :', bg = 'black', fg = 'white', font = ('arial 12')).grid(row = 5, column = 0, sticky = W)

# Create and Entry box for the name
entry1 = Entry(win, width = 26, bg = 'white', font = ('arial 10 bold')). grid(row = 5, column =0, padx = 1)

# CCreate space
Label(win, text = '', bg = 'black').grid(row = 6, column = 0)


# Create a button
btn1 = Button(win, text = 'Calculate', fg= 'purple', command = calculate, font = ('arial 9 bold')).grid(row= 7, column = 0)


Label(win, text = '\n\n Made by @Ugocode', bg = 'black', fg = 'white').grid(row = 9, column = 0)

win.mainloop()
