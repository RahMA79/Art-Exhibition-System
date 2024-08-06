from tkinter import *
import customtkinter
import sqlite3

def artDiscription(artID):
    hovColor="#B08968"

    artpiece = Tk()

    artpiece.geometry('1100x600')
    artpiece.resizable(False,False)
    artpiece.config(bg='#EDE0D4')

#  ---  x is a parameter passed to that page contains the id of the art piece chosen ---  
    conn = sqlite3.connect('ArtGalary.db')
    cur = conn.cursor()
    cur.execute(f'SELECT title FROM ArtWork where ArtWork_ID = {artID}')
    artpieceTitle = cur.fetchall()

    cur.execute(f'SELECT Img_URL FROM ArtWork where ArtWork_ID = {artID}')
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

#------------------BackButton------------------#
    def back():
        artpiece.destroy()
        import categoryArts

    arrow = PhotoImage(file = 'images/arrow.png')
    artpieceBackBtn = customtkinter.CTkButton(
                       artpieceTitle,
                       text='',
                       image=arrow,
                       width=20,
                       height=20,
                       bg_color="transparent",
                       fg_color='transparent',
                       hover_color=hovColor,
                       command=back,
                     )



    artpieceFrame = customtkinter.CTkScrollableFrame(artpiece,
                                                    border_color='#EDE0D4',
                                                    fg_color='#EDE0D4',
                                                    scrollbar_button_color='#7F5539',
                                                    scrollbar_button_hover_color='#B08968',
                                                    width=100,
                                                    )
#-----------------------ArtImage------------------#
    img = PhotoImage(file = artpieceImg[0])
    img = img.subsample(x=1,y=1)
    artpieceImg = Label(artpieceFrame,
                    anchor='center',
                    image= img,
                    font=("Arial Rounded MT Bold", 60, "bold")
               )

    cur = conn.cursor()
    cur.execute(f'SELECT Artist_ID FROM ArtWork where ArtWork_ID = {artID}')
    artist_id = cur.fetchall()
    cur.execute(f'SELECT Category, description, Date_of_creation FROM ArtWork where ArtWork_ID = {artID}')
    data = cur.fetchall()

    cur.execute(f'SELECT first_name, last_name FROM Artist where Artist_ID = {artist_id[0][0]}')
    artistData = cur.fetchall()


    conn.close()

#---------------------Art Description-------------------#
    ls = data[0][1].split()

    des = ""
    sm = 0
    for word in ls: 
        if sm + len(word) < 90:
            des = des + word + " "
            sm += len(word) + 1
        else : 
            sm = len(word)
            des = des + "\n" + word


    descriptionText = f"""
Artist : {artistData[0][0]} {artistData[0][1]}
Art Category : {data[0][0]}
date of creation : {data[0][2]}
Description : 
{des}
"""

    description = Label(artpieceFrame,
                       anchor='center',
                       text= descriptionText,
                       font=("Times new roman", 18, "bold"),
                       bg= '#EDE0D4',
                       justify=CENTER
                    )



    artpieceTitle.pack(side='top')
    artpieceBackBtn.place(x=0.3)
    artpieceImg.pack()
    description.pack()

    artpieceFrame.pack(fill=BOTH, expand=1)

    artpiece.mainloop()

#artDiscription()