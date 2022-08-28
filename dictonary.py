from tkinter import *
from PyDictionary import PyDictionary
dictionary = PyDictionary()
win =Tk()
win.geometry("700x400")

win.title("Python Dictionary")

def dict():
   meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
Label(win, text="Dictionary", font=("Times New Roman" ,20)).pack(pady=20)
frame = Frame(win)
Label(frame, text="Type any Word ", font=("Poppins bold", 15)).pack(side=LEFT)
word = Entry(frame, font=("Times New Roman", 15))
word.pack()
frame.pack(pady=10)
frame1 = Frame(win)
Label(frame1, text="Meaning:", font=("Aerial", 18)).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Poppins",15), width= 30)
meaning.pack()
frame1.pack(pady=10)

Button(win, text="Find", font=("Poppins bold",15), command=dict).pack()

win.mainloop()