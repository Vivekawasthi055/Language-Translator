from tkinter import *
import tkinter as tk
from tkinter import ttk
import pyttsx3
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0, END)
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

def clear():
    sor_txt.delete(1.0, END)
    dest_txt.delete(1.0, END)

def speaknow():
    text = dest_txt.get(1.0, END)
    engine.say(text)
    engine.runAndWait()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160)

root = tk.Tk()
root.title('Language Translator')
root.geometry('600x370')

frame = Frame(root, width=600, height=370, relief=RIDGE, borderwidth=5, bg='#F7DC6F')
frame.place(x=0, y=0)

lab_txt = Label(root, text=" Language Translator ", font=("Helvetica", 20, "bold"), relief=RIDGE, borderwidth=5, fg='black', bg='#FFC125')
lab_txt.place(x=150, y=30, height=50, width=300)

sor_txt = Text(frame, font=("verdana", 15, "bold"), fg='black', bg='white', wrap=WORD)
sor_txt.place(x=10, y=130, width=280, height=150)

dest_txt = Text(frame, font=("verdana", 15, "bold"), fg='black', bg='white', wrap=WORD)
dest_txt.place(x=300, y=130, width=280, height=150)

button_change = Button(frame, text="Translate", bg='#248aa2', relief=RAISED, command=data)
button_change.place(x=120, y=300, width=100, height=30)

button_clear = Button(frame, text="Clear", bg='#248aa2', relief=RAISED, command=clear)
button_clear.place(x=380, y=300, width=100, height=30)

button_speak = Button(frame, text="Speak", bg='#248aa2', relief=RAISED, command=speaknow)
button_speak.place(x=250, y=300, width=100, height=30)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, value=list_text)
comb_sor.place(x=70, y=90, width=150, height=20)
comb_sor.set("English")

comb_dest = ttk.Combobox(frame, value=list_text)
comb_dest.place(x=360, y=90, width=150, height=20)
comb_dest.set("Hindi")

root.mainloop()