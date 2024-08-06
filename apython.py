from tkinter import *
import sqlite3
from PIL import Image , ImageTk
artpiece = Tk()

artpiece.geometry('1100x600')
artpiece.resizable(False,False)
artpiece.config(bg='#EDE0D4')


x = 15
#  ---  x is a parameter passed to that page contains the id of the art piece chosen ---  
conn = sqlite3.connect('ArtGalary.db')
cur = conn.cursor()
cur.execute(f'SELECT title FROM ArtWork where ArtWork_ID = {x}')
artpieceTitle = cur.fetchall()

cur.execute(f'SELECT Img_URL FROM ArtWork where ArtWork_ID = {x}')
artpieceImg = cur.fetchall()

artpiece.title(artpieceTitle[0])

artpieceTitle = Label(
                       artpiece,
                       anchor='center',
                       text=artpieceTitle[0], # art piece title can be put here
                       foreground='#EDE0D4',
                       bg='#9C6644',
                       width='23',
                       font=("Arial Rounded MT Bold", 60, "bold")
                     )

arrow = PhotoImage(file = 'images/arrow.png')
artpieceBackBtn = Button(
                       artpieceTitle,
                       text='Back',
                       image=arrow,
                       relief="sunken",
                       highlightthickness=0,
                       borderwidth=0
                     )

img = PhotoImage(file = artpieceImg[0])
img = img.subsample(x=1,y=2)
artpieceImg = Label(artpiece,
                    anchor='center',
                    image= img,
                    font=("Arial Rounded MT Bold", 60, "bold")
               )

cur = conn.cursor()
cur.execute(f'SELECT Artist_ID FROM ArtWork where ArtWork_ID = {x}')
artist_id = cur.fetchall()
cur.execute(f'SELECT Category, description, Date_of_creation FROM ArtWork where ArtWork_ID = {x}')
data = cur.fetchall()

cur.execute(f'SELECT first_name, last_name FROM Artist where Artist_ID = {artist_id[0][0]}')
artistData = cur.fetchall()


conn.close()

descriptionText = f"""
Artist : {artistData[0][0]} {artistData[0][1]}
Art Category : {data[0][0]}
date of creation : {data[0][2]}
description : {data[0][1]}
"""
description = Label(artpiece,
                       anchor='center',
                       text= descriptionText,
                       font=("Times new roman", 18, "bold"),
                       bg= '#EDE0D4'
                    )



artpieceTitle.pack(side='top')
artpieceBackBtn.place(width=85, height=88)
artpieceImg.pack()
description.pack()

artpiece.mainloop()