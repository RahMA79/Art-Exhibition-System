from tkinter import *
from PIL import Image,ImageTk
import sqlite3
root=Tk()
root.geometry('1100x600')
scl=  Scrollbar(root,orient=VERTICAL)
scl.pack(side=LEFT,fill=Y)
sc2=Scrollbar(root,orient=HORIZONTAL)
sc2.pack(side=BOTTOM,fill=X)

root.resizable(False,False)
root.title("Abstract Art")
root.config(bg='#EDE0D4')
l1 = Label(root,anchor='center', text = "About Abstrct Art",
                       foreground='#EDE0D4',
                       bg='#9C6644',
                       width='23',
                       font = ("Times New Roman",35,"bold")
                       )
l1.pack()
l2 = Label(root,anchor='center', text = "click and Read details",
                       foreground='#463F3A',
                       width='23',

                       font = ("Times New Roman",20,"bold")
                       )
l2.pack()
img1=Image.open(r"images/Overthinking1.jpg")
img1=img1.resize((450,220))
img_t=ImageTk.PhotoImage(img1)
img2=Image.open(r"images/interference1.jpg")
img2=img2.resize((450,220))
img_t2=ImageTk.PhotoImage(img2)
img3=Image.open(r"images/fairness1.jpg")
img3=img3.resize((450,200))
img_t3=ImageTk.PhotoImage(img3)
img4=Image.open(r"images/legibility1.jpg")
img4=img4.resize((450,200))
img_t4=ImageTk.PhotoImage(img4)
b1 = Button(root, text='Over thinking', compound='top', font=("Arial", 12, 'bold'), image=img_t, relief='flat')
b2 = Button(root, text='Interference', font=("Arial", 12, 'bold'), compound='top', image=img_t2, relief='flat')
b3 = Button(root, text='Fairness', compound='top', font=("Arial", 12, 'bold'), image=img_t3, relief='flat')
b4 = Button(root, text='Legibility', compound='top', font=("Arial", 12, 'bold') , image=img_t4, relief='flat')
# Arrange the buttons in a grid
b1.place(x=100, y=90)
b2.place(x=600, y=90)
b3.place(x=600, y=370)
b4.place(x=100, y=370)

root.mainloop()




