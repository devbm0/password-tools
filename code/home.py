import customtkinter as ctk
from PIL import Image
import os


def home_main(root):
    frame = ctk.CTkFrame(root, fg_color='transparent', height=650, width=900)
    frame.place(x=0, y=0)

    main_label = ctk.CTkLabel(frame, text="Welcome to Password Tools!", font=('Open Sans', 40, 'bold'), fg_color='transparent')
    main_label.place(relx=0.5, rely=0.1, anchor='center')

    sub_text = ctk.CTkTextbox(frame, width=500, height=330, wrap='word', font=('Open Sans', 18), fg_color='transparent')
    sub_text.place(relx=0.5, rely=0.4, anchor='center')
    paragraph_text = '''Password tools was written to help the average person when it comes to the cast world of online threats. Now more than ever, strong passwords are very important to keeping you safe. This tool can help you create strong new passwords, analyze the security of current ones, and educate you about good password habits. Whether you're a cybersecurity expert or a typical user, this tool can help you save time and bring peace of mind to all!
    
    Written by Ben Munch (Github: devbm0)
    
    Version 1.0.0'''
    sub_text.insert('0.0', paragraph_text, 'center')
    sub_text.tag_config('center', justify="center")
    sub_text.configure(state='disabled')
    
    image_path = os.path.abspath('password-tools.png')
    image = Image.open(image_path)
    ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(200,200))
    image_label = ctk.CTkLabel(frame, image=ctk_image, text='', fg_color='transparent')
    image_label.place(relx=0.5, rely=0.7, anchor='center')