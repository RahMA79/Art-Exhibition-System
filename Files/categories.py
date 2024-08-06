from tkinter import *
from PIL import Image, ImageTk
import customtkinter as CTK

primaryColor = "#EDE0D4"
secondaryColor="#E6CCB2"
thirdColor="#DDB892"
btnColor="#9C6644"
hovColor="#B08968"

# Create the main window
Categories = CTK.CTk()
Categories.title("Art Gallery")
Categories.geometry("1100x600")
Categories.resizable(False, False)
# Set the background color of the root window
Categories.config(bg='#EDE0D4')

def new_window():
    window = CTK.CTkToplevel(Categories)
    window.title('Art Gallery')
    window.geometry('1100x600')
    window.configure(bg='#EDE0D4')
    window.resizable(False, False)
def navigationBar():
    nav_frame = CTK.CTkFrame(Categories,width=150,height=600,fg_color="#7F5539",bg_color="#7F5539")
    nav_frame.grid(row=0,column=0,sticky="nw") 
    
    artist_img = Image.open("images/painter.png")
    artist_img = artist_img.resize((100,100))
    artist_img_tk = ImageTk.PhotoImage(artist_img)
    artist_lbl = CTK.CTkLabel(nav_frame,text="",image=artist_img_tk)
    artist_lbl.grid(row=0,column=0,pady=(30,0))

    icons_frame = CTK.CTkFrame(nav_frame,width=150,height=600,fg_color="#7F5539",bg_color="#7F5539")
    icons_frame.grid(row=1,column=0,pady=(80,250))

    categoryIcon = Image.open("images/choice.png")
    categoryIcon = categoryIcon.resize((45,45))
    profileIcon_tk = ImageTk.PhotoImage(categoryIcon)    
    profile_btn = CTK.CTkButton(icons_frame,
                                image=profileIcon_tk,
                                text="Arts",
                                bg_color="transparent",
                                fg_color="transparent",
                                hover_color=hovColor)
    profile_btn.grid(pady=(0,40))

    def events():
        Categories.destroy()
        import events

    eventIcon = Image.open("images/event.png")
    eventIcon = eventIcon.resize((50,50))
    postIcon_tk = ImageTk.PhotoImage(eventIcon)    
    post_btn = CTK.CTkButton(icons_frame,image=postIcon_tk,text="Events",
                             bg_color="transparent",fg_color="transparent",
                             hover_color=hovColor,
                             command=events)
    post_btn.grid(pady=(0,40))

    def logout():
        Categories.destroy()
        import Registeration

    logoutIcon = Image.open("images/logout .png")
    logoutIcon = logoutIcon.resize((50,50))
    logoutIcon_tk = ImageTk.PhotoImage(logoutIcon)    
    logout_btn = CTK.CTkButton(icons_frame,image=logoutIcon_tk,
                               text="Logout",bg_color="transparent",
                               fg_color="transparent",
                               hover_color=hovColor,
                               command=logout)
    logout_btn.grid()


navigationBar()

# Create a label for the first line of text
label1 = CTK.CTkLabel(Categories, text="Welcome to our Art Gallery!", 
                        font=("Arial", 30, 'bold'),
                        bg_color='#EDE0D4',
                        text_color='black')
label1.place(x=380, y=20)

# Create a label for the second line of text
label2 = CTK.CTkLabel(Categories, text="Select your Category",
                        font=("Arial", 26, 'bold'),
                        bg_color='#EDE0D4',
                        text_color='black')
label2.place(x=450, y=80)

image1 = Image.open('images/painting art.jpeg')
image1 = image1.resize((250, 200))
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open('images/Expressionism arts.jpeg')
image2 = image2.resize((250, 200))
photo2 = ImageTk.PhotoImage(image2)

image3 = Image.open('images/Figuratve art.jpeg')
image3 = image3.resize((250, 200))
photo3 = ImageTk.PhotoImage(image3)

image4 = Image.open('images/Abstrct art.jpeg')
image4 = image4.resize((250, 200))
photo4 = ImageTk.PhotoImage(image4)

image5 = Image.open('images/Sculpture arts.jpeg')
image5 = image5.resize((250, 200))
photo5 = ImageTk.PhotoImage(image5)

image6 = Image.open('images/Visual arts.jpeg')
image6 = image6.resize((250, 200))
photo6 = ImageTk.PhotoImage(image6)

# Create the buttons
btn1 = CTK.CTkButton(Categories, text='Abstrct arts', image=photo1, font=("Arial", 12, 'bold'), command=new_window, fg_color=btnColor,bg_color=btnColor, compound='top',hover_color=hovColor)
btn2 = CTK.CTkButton(Categories, text='Expressionism arts', image=photo2, font=("Arial", 12, 'bold'), command=new_window, fg_color=btnColor,bg_color=btnColor,compound='top', hover_color=hovColor)
btn3 = CTK.CTkButton(Categories, text='Figuratve arts', image=photo3, font=("Arial", 12, 'bold'), command=new_window, fg_color=btnColor,bg_color=btnColor,compound='top',hover_color=hovColor)
btn4 = CTK.CTkButton(Categories, text='Sculpture arts', image=photo4, font=("Arial", 12, 'bold'), command=new_window, fg_color=btnColor,bg_color=btnColor,compound='top',hover_color=hovColor)
btn5 = CTK.CTkButton(Categories, text='Painting arts', image=photo5, font=("Arial", 12, 'bold'), command=new_window, fg_color=btnColor,bg_color=btnColor,compound='top', hover_color=hovColor)
btn6 = CTK.CTkButton(Categories, text='Visual arts', image=photo6, font=("Arial", 12, 'bold'), command=new_window, fg_color=btnColor,bg_color=btnColor,compound='top', hover_color=hovColor)

# Arrange the buttons in a grid
btn1.place(x=270, y=140)
btn2.place(x=540, y=140)
btn3.place(x=800, y=140)
btn4.place(x=270, y=370)
btn5.place(x=540, y=370)
btn6.place(x=800, y=370)

Categories.mainloop()