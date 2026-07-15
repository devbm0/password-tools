import customtkinter as ctk
from PIL import Image, ImageTk
import os, platform
import home, creation, analysis, learn

def test():
    print("Hello, world!")

def quit_if():
    os_name = platform.system()
    if os_name == 'Windows':
        quit_win(icon)
    if os_name == 'Linux':
        quit_linux(icon)

def quit_win(icon):
    if hasattr(root, 'quit_root') and root.quit_root.winfo_exists():
        root.quit_root.lift()
        root.quit_root.focus_force()
        return
    quit_root = ctk.CTkToplevel(root)
    quit_root.wm_iconphoto(False, icon)
    quit_root.title("Are you sure you want to quit?")
    quit_root.grab_set()
    quit_root.lift()
    quit_root.focus_force()
    y = ctk.CTkButton(quit_root, text='Yes', command=root.destroy, width=20, fg_color='blue')
    y.grid(row=0, column=0, padx=10, pady=5)
    n = ctk.CTkButton(quit_root, text='No', command=quit_root.destroy, width=20, fg_color='blue')
    n.grid(row=0, column=2, padx=10, pady=5)
    confirm = ctk.CTkLabel(quit_root, text='''Are you sure you want to quit?
All unsaved data will be destroyed.''', font=('Open Sans', 16))
    confirm.grid(row=0, column=1, padx=15, pady=15)

def quit_linux(icon):
    quit_root = ctk.CTkToplevel(root)
    quit_root.title("Are you sure you want to quit?")
    quit_root.wm_iconphoto(False, icon)
    quit_root.resizable(False, False)
    y = ctk.CTkButton(quit_root, text='Yes', command=root.destroy, width=20, fg_color='blue')
    y.grid(row=0, column=0, padx=10, pady=5)
    n = ctk.CTkButton(quit_root, text='No', command=quit_root.destroy, width=20, fg_color='blue')
    n.grid(row=0, column=2, padx=10, pady=5)
    confirm = ctk.CTkLabel(quit_root, text='''Are you sure you want to quit?
All unsaved data will be destroyed.''', font=('Open Sans', 16))
    confirm.grid(row=0, column=1, padx=15, pady=15)

def settings_main():
    global theme_var
    settings_root = ctk.CTkToplevel(root)
    settings_root.title("Settings - Password Tools")
    settings_root.wm_iconphoto(False, icon)
    settings_root.resizable(False, False)
    settings_root.geometry("450x350")
    
    main_label = ctk.CTkLabel(settings_root, text="Settings", font=("Open Sans", 36, "bold"))
    main_label.place(relx=0.5, y=30, anchor='center')
    theme_frame = ctk.CTkFrame(settings_root, width=400, height=90)
    theme_frame.place(relx=0.5, y=110, anchor='center')
    theme_label = ctk.CTkLabel(theme_frame, text="Theme", font=("open Sans", 24, "bold"))
    theme_label.place(relx=0.5, y=20, anchor='center')
    theme_options_frame = ctk.CTkFrame(theme_frame, width=400, height=25, fg_color='transparent')
    theme_options_frame.place(relx=0.5, y=60, anchor='center')
    theme_var = ctk.IntVar(value=0)
    light = ctk.CTkRadioButton(theme_options_frame, text="Light", font=("Open Sans", 18), command=theme_event, value=1, variable=theme_var)
    light.grid(row=0, column=0, padx=5, pady=5)
    dark = ctk.CTkRadioButton(theme_options_frame, text="Dark", font=("Open Sans", 18), command=theme_event,  value=2, variable=theme_var)
    dark.grid(row=0, column=1, padx=5, pady=5)
    system = ctk.CTkRadioButton(theme_options_frame, text="System", font=("Open Sans", 18), command=theme_event,  value=3, variable=theme_var)
    system.grid(row=0, column=2, padx=5, pady=5)

def theme_event():
    if theme_var.get() == 1: ctk.set_appearance_mode("light")
    if theme_var.get() == 2: ctk.set_appearance_mode("dark")
    if theme_var.get() == 3: ctk.set_appearance_mode("system")

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
app_label = ctk.CTkLabel(header, text='Password Tools', font=font_big, text_color='white')
app_label.place(x=10, y=13)

nav = ctk.CTkFrame(root, width=450, height=40, fg_color='dark blue', bg_color='blue')
nav.place(x=483, y=9)
home_btn = ctk.CTkButton(nav, text='Home', command=lambda: home.home_main(container), fg_color='dark blue', bg_color='dark blue', width=70, height=40, font=font_small)
home_btn.place(x=2, y=0)
creation_btn = ctk.CTkButton(nav, text='Creation', command=lambda: creation.creation_main(container), fg_color='dark blue', bg_color='dark blue', width=70, height=40, font=font_small)
creation_btn.place(x=71, y=0)
analysis_btn = ctk.CTkButton(nav, text='Analysis', command=lambda: analysis.analysis_main(container), fg_color='dark blue', bg_color='dark blue', width=70, height=40, font=font_small)
analysis_btn.place(x=140, y=0)
learn_btn = ctk.CTkButton(nav, text='Learn', command=test, fg_color='dark blue', bg_color='dark blue', width=70, height=40, font=font_small)
learn_btn.place(x=209, y=0)
settings_btn = ctk.CTkButton(nav, text='Settings', command=lambda: settings_main(), fg_color='dark blue', bg_color='dark blue', width=70, height=40, font=font_small)
settings_btn.place(x=278, y=0)
quit_btn = ctk.CTkButton(nav, text='Quit', command=quit_if, fg_color='dark blue', bg_color='dark blue', width=70, height=40, font=font_small)
quit_btn.place(x=347, y=0)

home.home_main(container)
root.mainloop()