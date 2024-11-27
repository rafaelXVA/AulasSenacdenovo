import customtkinter as ctk

janela=ctk.CTk()
janela.geometry('500x500')

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

text=ctk.CTkLabel(janela, text="fortaleza > flamengo")
text.pack()
text.place(x=255,y=100)

janela.mainloop()

btn1=ctk.CTkButton(janela, text="")
btn1.pack()
btn1.place(x=300,y=100)
