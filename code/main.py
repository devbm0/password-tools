import customtkinter as ctk
from PIL import Image, ImageTk
import os, platform
import home, creation, analysis, learn, settings

ctk.set_default_color_theme('blue')
ctk.set_appearance_mode('system')

def test():
    print("Hello, world!")

def quit_if():
    os_name = platform.system()
    if os_name == 'Windows':
        quit_win()
    if os_name == 'Linux':
        quit_linux()

def quit_win():
    if hasattr(root, 'quit_root') and root.quit_root.winfo_exists():
        root.quit_root.lift()
        root.quit_root.focus_force()
        return
    quit_root = ctk.CTkToplevel(root)
    quit_root.title("Are you sure you want to quit?")
    quit_root.grab_set()
    quit_root.lift()
    quit_root.focus_force()
    y = ctk.CTkButton(quit_root, text='Yes', command=root.destroy, width=20, fg_color='blue')
    y.grid(row=0, column=0, padx=10, pady=5)
    n = ctk.CTkButton(quit_root, text='No', command=quit_root.destroy, width=20, fg_color='blue')
    n.grid(row=0, column=2, padx=10, pady=5)
    confirm = ctk.CTkLabel(quit_root, text='''Are you sure you want to quit?
All unsaved data will be deleted.''', font=('Open Sans', 16))
    confirm.grid(row=0, column=1, padx=15, pady=15)

def quit_linux():
    quit_root = ctk.CTkToplevel(root)
    quit_root.title("Are you sure you want to quit?")
    y = ctk.CTkButton(quit_root, text='Yes', command=root.destroy, width=20, fg_color='blue')
    y.grid(row=0, column=0, padx=10, pady=5)
    n = ctk.CTkButton(quit_root, text='No', command=quit_root.destroy, width=20, fg_color='blue')
    n.grid(row=0, column=2, padx=10, pady=5)
    confirm = ctk.CTkLabel(quit_root, text='''Are you sure you want to quit?
All unsaved data will be deleted.''', font=('Open Sans', 16))
    confirm.grid(row=0, column=1, padx=15, pady=15)

root = ctk.CTk()
root.geometry("900x700")
root.title("Password Tools 1.0.0")
root.resizable(False, False)

container = ctk.CTkFrame(root, width=900, height=650)
container.place(x=0, y=50)
container.pack_propagate(False)
container.grid_propagate(False)

font_small = ctk.CTkFont(family='Open Sans', size=14)
font_reg = ctk.CTkFont(family='Open Sans', size=16)
font_big = ctk.CTkFont('Open Sans', 20, 'bold')

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
home_btn = ctk.CTkButton(nav, text='Home', command=lambda: home.home_main(container), fg_color='dark blue', bg_color='dark blue', width=70, height=40, border_color='white', border_width=1, font=font_small)
home_btn.place(x=2, y=0)
creation_btn = ctk.CTkButton(nav, text='Creation', command=lambda: creation.creation_main(container), fg_color='dark blue', bg_color='dark blue', width=70, height=40, border_color='white', border_width=1, font=font_small)
creation_btn.place(x=71, y=0)
analysis_btn = ctk.CTkButton(nav, text='Analysis', command=lambda: analysis.analysis_main(container), fg_color='dark blue', bg_color='dark blue', width=70, height=40, border_color='white', border_width=1, font=font_small)
analysis_btn.place(x=140, y=0)
learn_btn = ctk.CTkButton(nav, text='Learn', command=test, fg_color='dark blue', bg_color='dark blue', width=70, height=40, border_color='white', border_width=1, font=font_small)
learn_btn.place(x=209, y=0)
settings_btn = ctk.CTkButton(nav, text='Settings', command=test, fg_color='dark blue', bg_color='dark blue', width=70, height=40, border_color='white', border_width=1, font=font_small)
settings_btn.place(x=278, y=0)
quit_btn = ctk.CTkButton(nav, text='Quit', command=quit_if, fg_color='dark blue', bg_color='dark blue', width=70, height=40, border_color='white', border_width=1, font=font_small)
quit_btn.place(x=347, y=0)

home.home_main(container)
root.mainloop()