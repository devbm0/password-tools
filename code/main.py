import customtkinter as ctk
from PIL import Image, ImageTk
import os
import home

ctk.set_default_color_theme('blue')
ctk.set_appearance_mode('system')

def test():
    print("Hello, world!")

def quit():
    def y_():
        root.destroy()
        quit_root.destroy()
    quit_root = ctk.CTk()
    y = ctk.CTkButton(quit_root, text='Yes', command=y_, width=20, fg_color='blue')
    y.grid(row=0, column=0, padx=5, pady=5)
    n = ctk.CTkButton(quit_root, text='No', command=quit_root.destroy, width=20, fg_color='blue')
    n.grid(row=0, column=2, padx=5, pady=5)
    confirm = ctk.CTkLabel(quit_root, text='Are you sure you want to quit?')
    confirm.grid(row=0, column=1, padx=5, pady=5)

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

nav = ctk.CTkFrame(root, width=450, height=40, fg_color='dark blue', bg_color='blue')
nav.place(x=483, y=9)
home_btn = ctk.CTkButton(nav, text='Home', command=lambda: home.home_main(root), fg_color='dark blue', bg_color='dark blue', width=70, height=40, border_color='white', border_width=1, font=font_small)
home_btn.place(x=2, y=0)
creation_btn = ctk.CTkButton(nav, text='Creation', command=test, fg_color='dark blue', bg_color='dark blue', width=70, height=40, border_color='white', border_width=1, font=font_small)
creation_btn.place(x=71, y=0)
analysis_btn = ctk.CTkButton(nav, text='Analysis', command=test, fg_color='dark blue', bg_color='dark blue', width=70, height=40, border_color='white', border_width=1, font=font_small)
analysis_btn.place(x=140, y=0)
settings_btn = ctk.CTkButton(nav, text='Settings', command=test, fg_color='dark blue', bg_color='dark blue', width=70, height=40, border_color='white', border_width=1, font=font_small)
settings_btn.place(x=209, y=0)
learn_btn = ctk.CTkButton(nav, text='Learn', command=test, fg_color='dark blue', bg_color='dark blue', width=70, height=40, border_color='white', border_width=1, font=font_small)
learn_btn.place(x=278, y=0)
quit_btn = ctk.CTkButton(nav, text='Quit', command=quit, fg_color='dark blue', bg_color='dark blue', width=70, height=40, border_color='white', border_width=1, font=font_small)
quit_btn.place(x=347, y=0)

root.mainloop()