import customtkinter as ctk
def home_main(root):
    home_root = ctk.CTkFrame(root, width=900, height=650)
    home_root.place(x=0, y=50)

    main_label = ctk.CTkLabel(home_root, text="Welcome to Password Tools!", font=('Open Sans', 40, 'bold'))
    main_label.pack()