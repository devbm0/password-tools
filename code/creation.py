import customtkinter as ctk

def creation_main(root):
    frame = ctk.CTkFrame(root, fg_color='transparent')
    

    def checkbox_event():
        if checkbox1_var.get() == 0:
            pass
        elif checkbox1_var.get() == 1:
            print("Hello, world!")
        if checkbox2_var.get() == 0:
            pass
        elif checkbox2_var.get() == 0:
            pass
        if checkbox1_var.get() == 0:
            if checkbox2.get() == 0:
                print("Please choose a length for your password")

    checkbox1_var = ctk.IntVar(value=0)
    checkbox2_var = ctk.IntVar(value=0)
    checkbox1 = ctk.CTkCheckBox(frame, text="Option 1", command=checkbox_event, variable=checkbox1_var)
    checkbox1.place(x=20, y=20)
    checkbox2 = ctk.CTkCheckBox(frame, text="Option 2", command=checkbox_event, variable=checkbox2_var)
    checkbox2.place(x=20, y=40)

    return frame