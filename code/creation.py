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

    def copy():
        pypc.copy(password)
        status_label.configure(text='Password copied!', text_color='green')
    copy_button = ctk.CTkButton(pass_frame, text='Copy', command=copy, font=('Open Sans', 16), width=30)
    copy_button.grid(row=0, column=1, padx=10)

def submit_phrase():
    global password
    status_label.configure(text='', text_color='red')
    if not length_phrase:
        status_label.configure(text='Error: Please select a length for your password.')
    password = generate_phrase(length_phrase, options_groups)
    pass_label_II.configure(text=f'{password}', font=('Consolas', 30), wraplength=800, justify='center')
    if len(password) >= 30:
        pass_label_II.configure(font=('Consolas', 24))
    def copy():
        pypc.copy(password)
        status_label.configure(text='Password copied!', text_color='green')
    copy_button = ctk.CTkButton(pass_frame, text='Copy', command=copy, font=('Open Sans', 16), width=30)
    copy_button.grid(row=0, column=1, padx=10)

def creation_main(container):
    for child in container.winfo_children():
        child.destroy()
    
    global length_selection, characters, pass_label_II, status_label, pass_frame
    global length_phrase, options_groups
    length_selection = ''
    characters = []

    font_small = ctk.CTkFont(family='Open Sans', size=14)
    font_reg = ctk.CTkFont(family='Open Sans', size=16)
    font_big = ctk.CTkFont('Open Sans', 20, 'bold')
    font_xbig = ctk.CTkFont('Open Sans', 24, 'bold')

    frame = ctk.CTkFrame(container, fg_color='transparent')
    frame.place(x=0, y=0, relwidth=1, relheight=1)
    frame.lift()

    main_label = ctk.CTkLabel(frame, text='Creation', font=('Open Sans', 36, 'bold'))
    main_label.place(relx=0.5, y=40, anchor='center')

    word_lbl = ctk.CTkLabel(frame, text='Random Letters', font=('Open Sans', 24, 'bold'))
    word_lbl.place(relx=0.5, y=90, anchor='center')

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

    line = ctk.CTkFrame(frame, width=800, height=2, fg_color='white')
    line.place(relx=0.5, y=285, anchor='center')

    phrase_lbl = ctk.CTkLabel(frame, text='Random Words', font=('Open Sans', 24, 'bold'))
    phrase_lbl.place(relx=0.5, y=320, anchor='center')

    length_frame_II = ctk.CTkFrame(frame, width=835, height=50)
    length_frame_II.place(relx=0.5, y=360, anchor='center')
    length_frame_II.pack_propagate(False)
    length_frame_II.grid_propagate(False)
    len_lbl_phrase = ctk.CTkLabel(length_frame_II, text='Length:', font=font_small)
    len_lbl_phrase.grid(row=0, column=0, padx=(10,5), pady=10)

    def length_phrase_event():
        global length_phrase
        if radiovar_phrase.get() == 1:
            length_phrase = 2
            checkbox4.configure(state=ctk.NORMAL)
            checkbox5.configure(state=ctk.NORMAL)
            checkbox6.configure(state=ctk.NORMAL)
            checkbox7.configure(state=ctk.NORMAL)
        if radiovar_phrase.get() == 2:
            length_phrase = 3
            checkbox4.configure(state=ctk.NORMAL)
            checkbox5.configure(state=ctk.NORMAL)
            checkbox6.configure(state=ctk.NORMAL)
            checkbox7.configure(state=ctk.NORMAL)
        if radiovar_phrase.get() == 3:
            length_phrase = 4
            checkbox4.configure(state=ctk.NORMAL)
            checkbox5.configure(state=ctk.NORMAL)
            checkbox6.configure(state=ctk.NORMAL)
            checkbox7.configure(state=ctk.NORMAL)
        if radiovar_phrase.get() == 4:
            length_phrase = 6
            checkbox4.configure(state=ctk.NORMAL)
            checkbox5.configure(state=ctk.NORMAL)
            checkbox6.configure(state=ctk.NORMAL)
            checkbox7.configure(state=ctk.NORMAL)
        if radiovar_phrase.get() == 5:
            length_phrase = 8
            checkbox4.configure(state=ctk.NORMAL)
            checkbox5.configure(state=ctk.NORMAL)
            checkbox6.configure(state=ctk.NORMAL)
            checkbox7.configure(state=ctk.NORMAL)
        else: 
            pass

    radiovar_phrase = ctk.IntVar(value=0)
    radiobutton_7 = ctk.CTkRadioButton(length_frame_II, text='2 Words', command=length_phrase_event, variable=radiovar_phrase, value=1)
    radiobutton_7.grid(row=0, column=1, padx=10, pady=10)
    radiobutton_8 = ctk.CTkRadioButton(length_frame_II, text='3 Words', command=length_phrase_event, variable=radiovar_phrase, value=2)
    radiobutton_8.grid(row=0, column=2, padx=10, pady=10)
    radiobutton_9 = ctk.CTkRadioButton(length_frame_II, text='4 Words', command=length_phrase_event, variable=radiovar_phrase, value=3)
    radiobutton_9.grid(row=0, column=3, padx=10, pady=10)
    radiobutton_10 = ctk.CTkRadioButton(length_frame_II, text='6 Words', command=length_phrase_event, variable=radiovar_phrase, value=4)
    radiobutton_10.grid(row=0, column=4, padx=10, pady=10)
    radiobutton_11 = ctk.CTkRadioButton(length_frame_II, text='8 Words', command=length_phrase_event, variable=radiovar_phrase, value=5)
    radiobutton_11.grid(row=0, column=5, padx=10, pady=10)

    options_frame = ctk.CTkFrame(frame, width=835, height=50)
    options_frame.place(relx=0.493, y=410, anchor='center')
    options_frame.pack_propagate(False)
    options_frame.grid_propagate(False)

    def options_phrase_event():
        global options_groups
        options_groups = []
        if checkbox4_var.get():
            options_groups.append('hyphens')
        if checkbox5_var.get():
            options_groups.append('numbers')
        if checkbox6_var.get():
            options_groups.append('punctuation')
        if checkbox7_var.get():
            options_groups.append('capitals')

    checkbox4_var = ctk.IntVar(value=0)
    checkbox5_var = ctk.IntVar(value=0)
    checkbox6_var = ctk.IntVar(value=0)
    checkbox7_var = ctk.IntVar(value=0)
    options_lbl = ctk.CTkLabel(options_frame, text='Options:', font=font_small)
    options_lbl.grid(row=0, column=0, padx=(10, 5), pady=10)
    checkbox4 = ctk.CTkCheckBox(options_frame, text='Include Hyphens', command=options_phrase_event, variable=checkbox4_var, state=ctk.DISABLED)
    checkbox4.grid(row=0, column=1, padx=10, pady=10)
    checkbox5 = ctk.CTkCheckBox(options_frame, text='Include Numbers', command=options_phrase_event, variable=checkbox5_var, state=ctk.DISABLED)
    checkbox5.grid(row=0, column=2, padx=10, pady=10)
    checkbox6 = ctk.CTkCheckBox(options_frame, text='Include Punctuation', command=options_phrase_event, variable=checkbox6_var, state=ctk.DISABLED)
    checkbox6.grid(row=0, column=3, padx=10, pady=10)
    checkbox7 = ctk.CTkCheckBox(options_frame, text='Include Capitals', command=options_phrase_event, variable=checkbox7_var, state=ctk.DISABLED)
    checkbox7.grid(row=0, column=4, padx=10, pady=10)

    submit_II = ctk.CTkButton(frame, text='Submit', command=submit_phrase, font=('Open Sans', 24))
    submit_II.place(relx=0.5, y=470, anchor='center')
    
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

def generate_phrase(length_phrase, options_groups):
    words_path = os.path.abspath('words.txt')

    try:
        with open (words_path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Error: File not found")
        return None

    pieces = [secrets.choice(words) for _ in range(length_phrase)]
    if 'capitals' in options_groups:
        pieces = [value.title() for value in pieces]
    if 'numbers' in options_groups:
        pieces = [value + secrets.choice(string.digits) for value in pieces]
    if 'punctuation' in options_groups:
        pieces = [value + secrets.choice(string.punctuation) for value in pieces]
    if 'hyphens' in options_groups:
        phrase = '-'.join(pieces)
    if 'hyphens' not in options_groups:
        phrase = ' '.join(pieces)
    return phrase