import requests
import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo
import datetime
import arrow
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates


# now = datetime.date.today()
# print(now)


# now = arrow.now()
# last_water = now.shift(hours=-3)
# last_water.humanize()
# print(f'The last time you watered your plant was {last_water.humanize()}')




# def question_answer():
#     question =e1.get()
#     answer = wikipedia.summary(question)
#     showinfo('answer', answer)

# root = Tk()
# root.geometry("300x400")
# question = StringVar()
# e1 = Entry(root, textvariable = question)
# e1.grid(row=1, column=1)

# b1 = Button(root, width = 12, command = question_answer)
# b1.grid(row = 3, column = 12)

# root.mainloop()