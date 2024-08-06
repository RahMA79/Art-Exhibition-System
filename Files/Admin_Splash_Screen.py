import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")


app=ctk.CTk()
app.title("Admin Page")
width=1100
height=600

app.geometry(f'{width}x{height}+0+0')
app.resizable(False,False)
    

    # components 
admin_frame= ctk.CTkFrame(app,height=height,width=width)
admin_frame.place(relx=0.5,rely=0.5, anchor='center')


    # Load and display background image
image = Image.open('images/admin_background.webp')
img = image.resize((1370,745))
img_tk = ImageTk.PhotoImage(img)
background_label = Label(admin_frame, image=img_tk)
background_label.place(x=0, y=0)


upload_button = ctk.CTkButton(admin_frame,
                                text="Continue → ",
                                font=('Arial Rounded MT Bold',40,'bold'),
                                fg_color= "#4A4046",
                                hover_color='#B08968',
                                corner_radius=0,
                                width=20,
                                height=20)
upload_button.place(x=100, y=500)
app.mainloop()
