import customtkinter as ctk
from PIL import Image, ImageTk
import os

ctk.set_default_color_theme('blue')
ctk.set_appearance_mode('system')

root = ctk.CTk()
root.geometry("900x700")
root.title("Password Tools 1.0.0")
root.resizable(False, False)

font_small = ctk.CTkFont(family='Open Sans', size=14)
font_reg = ctk.CTkFont(family='Open Sans', size=16)
font_big = ctk.CTkFont('Open Sans', 20, 'bold')

#App icon
icon_path = os.path.abspath('password-tools.png')
img = Image.open(icon_path)
icon = ImageTk.PhotoImage(img)
root.wm_iconphoto(False, icon)

header = ctk.CTkFrame(root, width=900, height=53, fg_color='blue')
header.place(x=0, y=-3)
app_label = ctk.CTkLabel(header, text='Password Tools', font=font_big)
app_label.place(x=10, y=13)

nav = ctk.CTkFrame(root, width=377, height=40, fg_color='blue', bg_color='blue')
home_btn = ctk.CTkButton(nav, text="Home", command=lambda: home())
home_btn.place(x=0, y=0)

root.mainloop()