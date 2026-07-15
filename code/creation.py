import customtkinter as ctk
import string
import secrets
import pyperclip as pypc
import os

char_groups = {
    'letters':{
        'pool':string.ascii_letters,
        'required':[string.ascii_uppercase, string.ascii_lowercase],
        'label':'letters'
    },

    'digits':{
        'pool':string.digits,
        'required':[string.digits],
        'label':'numbers'
    },

    'punctuation':{
        'pool':string.punctuation,
        'required':[string.punctuation],
        'label':'punctuation'
    }
}


password_list = []
def submit_word():
    global password
    status_label.configure(text='', text_color='red')
    if not length_selection:
        status_label.configure(text='Error: Please select a length for your password')
        return
    if not characters:
        status_label.configure(text='Error: Please select at least one character type option.')
    password = generate(length_word, selected_groups)
    pass_label_II.configure(text=f'{password}', font=('Consolas', 36))
    password_list.append(password)
    print(password_list)
 
    def copy():
        pypc.copy(password)
        status_label.configure(text='Password copied!', text_color='green')
    copy_button = ctk.CTkButton(pass_frame, text='Copy', command=copy, font=('Open Sans', 16), width=30)
    copy_button.grid(row=0, column=1, padx=10)

    def save():
        save_window = ctk.CTkToplevel(frame, width=450, height=300)
        lbl = ctk.CTkLabel(save_window, text="Are you sure?", font=('Open Sans', 32, 'bold'))
        lbl.place(relx=0.5, y=30, anchor='center')
        textbox = ctk.CTkTextbox(save_window, fg_color='transparent', width=400, height=300, wrap='word', font=("Open Sans", 16))
        textbox.place(relx=0.5, y=200, anchor='center')
        warning_text = '''If you continue, all passwords generated in this session will be saved to your computer. Once you press 'save' below, they will be forgotten by this program and you will not be able to recover them. To ensure the passwords are not lost, be sure to securely save them in a password manager or another secure place.'''
        textbox.insert('0.0', warning_text, 'center')
        textbox.tag_config('center', justify='center')
        textbox.configure(state='disabled')

        def defsave():
            with open("passwords.txt", 'w') as file:
                for item in password_list:
                    file.write(item + '\n')
            password_list.clear()
            save_window.destroy()    
            status_label.configure(text='File saved successfully!', text_color='green')
        button_frame = ctk.CTkFrame(save_window, height=25)
        button_frame.place(relx=0.5, y=260, anchor='center')
        defsave_btn = ctk.CTkButton(button_frame, text="Save", command=defsave)
        defsave_btn.grid(row=0, column=0)
        cancel_btn = ctk.CTkButton(button_frame, text="Cancel", command=save_window.destroy)
        cancel_btn.grid(row=0, column=1)

    save_button = ctk.CTkButton(pass_frame, text='Save', command=save, font=("Open Sans", 16), width=30)
    save_button.grid(row=0, column=2, padx=10)

def creation_main(container):
    for child in container.winfo_children():
        child.destroy()
    
    global length_selection, characters, pass_label_II, status_label, pass_frame, frame
    global length_phrase, options_groups
    length_selection = ''
    characters = []

    font_small = ctk.CTkFont(family='Open Sans', size=14)
    font_reg = ctk.CTkFont(family='Open Sans', size=16)
    font_big = ctk.CTkFont('Open Sans', 20, 'bold')
    font_xbig = ctk.CTkFont('Open Sans', 24, 'bold')

    frame = ctk.CTkFrame(container, fg_color='transparent', width=900, height=650)
    frame.place(x=0, y=0)
    frame.lift()

    main_label = ctk.CTkLabel(frame, text='Creation', font=('Open Sans', 36, 'bold'))
    main_label.place(relx=0.5, y=40, anchor='center')

    sub_lbl = ctk.CTkLabel(frame, text='Create a random and secure password!', font=('Open Sans', 24, 'bold', 'italic'))
    sub_lbl.place(relx=0.5, y=90, anchor='center')

    length_frame = ctk.CTkFrame(frame, width=835, height=50)
    length_frame.place(relx=0.5, y=135, anchor='center')
    length_frame.pack_propagate(False)
    length_frame.grid_propagate(False)
    len_lbl_word = ctk.CTkLabel(length_frame, text="Length:", font=font_small)
    len_lbl_word.grid(row=0, column=0, padx=10, pady=10)
    def length_word_event():
        global length_word, length_selection
        status_label.configure(text='')
        if radiovar_word.get() ==  1:
            length_word = 4
            length_selection = '4'
            checkbox1.configure(state=ctk.NORMAL)
            checkbox2.configure(state=ctk.NORMAL)
            checkbox3.configure(state=ctk.NORMAL)
        if radiovar_word.get() == 2:
            length_word = 6
            length_selection = '6'
            checkbox1.configure(state=ctk.NORMAL)
            checkbox2.configure(state=ctk.NORMAL)
            checkbox3.configure(state=ctk.NORMAL)
        if radiovar_word.get() == 3:
            length_word = 8
            length_selection = '8'
            checkbox1.configure(state=ctk.NORMAL)
            checkbox2.configure(state=ctk.NORMAL)
            checkbox3.configure(state=ctk.NORMAL)
        if radiovar_word.get() == 4:
            length_word = 12
            length_selection = '12'
            checkbox1.configure(state=ctk.NORMAL)
            checkbox2.configure(state=ctk.NORMAL)
            checkbox3.configure(state=ctk.NORMAL)
        if radiovar_word.get() == 5:
            length_word = 16
            length_selection = '16'
            checkbox1.configure(state=ctk.NORMAL)
            checkbox2.configure(state=ctk.NORMAL)
            checkbox3.configure(state=ctk.NORMAL)
        if radiovar_word.get() == 6:
            length_word = 32
            length_selection = '32'
            checkbox1.configure(state=ctk.NORMAL)
            checkbox2.configure(state=ctk.NORMAL)
            checkbox3.configure(state=ctk.NORMAL)
            
    radiovar_word = ctk.IntVar(value=0)
    radiobutton_1 = ctk.CTkRadioButton(length_frame, text='4-Character', command=length_word_event, variable=radiovar_word, value=1)
    radiobutton_1.grid(row=0, column=1, padx=10, pady=10)
    radiobutton_2 = ctk.CTkRadioButton(length_frame, text='6-Character', command=length_word_event, variable=radiovar_word, value=2)
    radiobutton_2.grid(row=0, column=2, padx=10, pady=10)
    radiobutton_3 = ctk.CTkRadioButton(length_frame, text='8-Character', command=length_word_event, variable=radiovar_word, value=3)
    radiobutton_3.grid(row=0, column=3, padx=10, pady=10)
    radiobutton_4 = ctk.CTkRadioButton(length_frame, text='12-Character', command=length_word_event, variable=radiovar_word, value=4)
    radiobutton_4.grid(row=0, column=4, padx=10, pady=10)
    radiobutton_5 = ctk.CTkRadioButton(length_frame, text='16-Character', command=length_word_event, variable=radiovar_word, value=5)
    radiobutton_5.grid(row=0, column=5, padx=10, pady=10)
    radiobutton_6 = ctk.CTkRadioButton(length_frame, text='32-Character', command=length_word_event, variable=radiovar_word, value=6)
    radiobutton_6.grid(row=0, column=6, padx=10, pady=10)

    char_frame = ctk.CTkFrame(frame, width=850, height=50)
    char_frame.place(relx=0.5, y=185, anchor='center')
    char_frame.pack_propagate(False)
    char_frame.grid_propagate(False)
    char_lbl = ctk.CTkLabel(char_frame, text='Characters:', font=font_small)
    char_lbl.grid(row=0, column=0)
    
    def variables_event():
        global characters, selected_groups
        selected_groups = []
        if checkbox1_var.get():
            selected_groups.append('letters')
        if checkbox2_var.get():
            selected_groups.append('digits')
        if checkbox3_var.get():
            selected_groups.append('punctuation')
        if not selected_groups:
            return
        status_label.configure(text='')
        characters = [char_groups[g]['label'] for g in selected_groups]

    checkbox1_var = ctk.IntVar(value=0)
    checkbox2_var = ctk.IntVar(value=0)
    checkbox3_var = ctk.IntVar(value=0)
    checkbox1 = ctk.CTkCheckBox(char_frame, text="Letters", command=variables_event, variable=checkbox1_var, state=ctk.DISABLED)
    checkbox1.grid(row=0, column=1, padx=10, pady=10)
    checkbox2 = ctk.CTkCheckBox(char_frame, text="Numbers", command=variables_event, variable=checkbox2_var, state=ctk.DISABLED)
    checkbox2.grid(row=0, column=2, padx=10, pady=10)
    checkbox3 = ctk.CTkCheckBox(char_frame, text="Punctuation", command=variables_event, variable=checkbox3_var, state=ctk.DISABLED)
    checkbox3.grid(row=0, column=3, padx=10, pady=10)
    sec_label = ctk.CTkLabel(char_frame, text='Choose all these for the most secure option', font=('Open Sans', 16, 'italic'))
    sec_label.grid(row=0, column=4, padx=10, pady=10)

    submit = ctk.CTkButton(frame, text='Submit', command=submit_word, font=('Open Sans', 24))
    submit.place(relx=0.5, y=240, anchor='center')
    
    pass_label = ctk.CTkLabel(frame, text='Your new password:', font=('Open sans', 20))
    pass_label.place(relx=0.5, y = 550, anchor='center')

    pass_frame = ctk.CTkFrame(frame, width=900, height=50)
    pass_frame.place(relx=0.5, y=590, anchor='center')
    
    pass_label_II = ctk.CTkLabel(pass_frame, text='...Press submit after picking some options...', font=('Consolas', 16))
    pass_label_II.grid(row=0, column=0)
    
    status_label = ctk.CTkLabel(frame, text='', font=('Open Sans', 14), text_color='red')
    status_label.place(relx=0.5, y=630, anchor='center')

def generate(length_word, selected_groups):
    rng = secrets.SystemRandom()
    password_chars = []
    counts = {}

    for group in selected_groups:
        char = rng.choice(char_groups[group]['pool'])
        password_chars.append(char)
        counts[group] = 1
    
    remaining = length_word - len(password_chars)

    while remaining > 0:
        group = rng.choice(selected_groups)

        max_allowed = (length_word // len(selected_groups)) + 1
        if counts[group] < max_allowed:
            password_chars.append(rng.choice(char_groups[group]['pool']))
            counts[group] += 1
            remaining -= 1

    rng.shuffle(password_chars)
    return ''.join(password_chars)