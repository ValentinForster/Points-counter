from tkinter import *

background_color = '#212121'
button_color = "#189404"
active_button_color = '#168504'
active_button_text = '#d4d2d2'

def is_integer(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True

root = Tk()
root.title("Punktezähler")
root.configure(background=background_color)

# Creating a label widget
valis_label_punkte = 0
#valis_label = Label(root, text=valis_label_punkte) # brauch ich die zeilen überhaupt???
andis_label_punkte = 0
andis_label = Label(root, text=andis_label_punkte)
gregors_label_punkte = 0
gregors_label = Label(root, text=gregors_label_punkte)
ellis_label_punkte = 0
ellis_label = Label(root, text=ellis_label_punkte)
tobis_label_punkte = 0
tobis_label = Label(root, text=tobis_label_punkte)

angezeigte_punkte_v = 0
angezeigte_punkte_a = 0
angezeigte_punkte_g = 0
angezeigte_punkte_e = 0
angezeigte_punkte_t = 0

# Creating entry fields
eingabe_vali = Entry(root, width=20, borderwidth=1, justify=CENTER, font=("default", 12))
eingabe_andi = Entry(root, width=20, borderwidth=1, justify=CENTER, font=("default", 12))
eingabe_gregor = Entry(root, width=20, borderwidth=1, justify=CENTER, font=("default", 12))
eingabe_elli = Entry(root, width=20, borderwidth=1, justify=CENTER, font=("default", 12))
eingabe_tobi = Entry(root, width=20, borderwidth=1, justify=CENTER, font=("default", 12))

# Creating submit buttons
first_time_v = True
previous_entry_v = "0"
first_time_a = True
previous_entry_a = "0"
first_time_g = True
previous_entry_g = "0"
first_time_e = True
previous_entry_e = "0"
first_time_t = True
previous_entry_t = "0"

def v_click():
    global valis_label_punkte
    global valis_label
    global previous_entry_v
    global first_time_v

    if is_integer(eingabe_vali.get()):
        previous_entry_v = previous_entry_v + f" + {eingabe_vali.get()}"
        valis_label_punkte = int(eingabe_vali.get()) + valis_label_punkte
        if first_time_v:
            valis_label_punkte_string = f"{str(valis_label_punkte)}"
            first_time_v = False
        else:
            valis_label_punkte_string = f"{previous_entry_v[3:]} = {str(valis_label_punkte)}"
        valis_label = Label(root, text=valis_label_punkte_string, bg=background_color, fg='white')
        valis_label.grid(row=6, column=0)
        eingabe_vali.delete(0, END)
    else:
        pass

def a_click():
    global andis_label_punkte
    global andis_label
    global previous_entry_a
    global first_time_a

    if is_integer(eingabe_andi.get()):
        previous_entry_a = previous_entry_a + f" + {eingabe_andi.get()}"
        andis_label_punkte = int(eingabe_andi.get()) + andis_label_punkte
        if first_time_a:
            andis_label_punkte_string = f"{str(andis_label_punkte)}"
            first_time_a = False
        else:
            andis_label_punkte_string = f"{previous_entry_a[3:]} = {str(andis_label_punkte)}"
        andis_label = Label(root, text=andis_label_punkte_string, bg=background_color, fg='white')
        andis_label.grid(row=9, column=0)
        eingabe_andi.delete(0, END)
    else:
        pass

def g_click():
    global gregors_label_punkte
    global gregors_label
    global previous_entry_g
    global first_time_g

    if is_integer(eingabe_gregor.get()):
        previous_entry_g = previous_entry_g + f" + {eingabe_gregor.get()}"
        gregors_label_punkte = int(eingabe_gregor.get()) + gregors_label_punkte
        if first_time_g:
            gregors_label_punkte_string = f"{str(gregors_label_punkte)}"
            first_time_g = False
        else:
            gregors_label_punkte_string = f"{previous_entry_g[3:]} = {str(gregors_label_punkte)}"
        gregors_label = Label(root, text=gregors_label_punkte_string, bg=background_color, fg='white')
        gregors_label.grid(row=12, column=0)
        eingabe_gregor.delete(0, END)
    else:
        pass

def e_click():
    global ellis_label_punkte
    global ellis_label
    global previous_entry_e
    global first_time_e

    if is_integer(eingabe_elli.get()):
        previous_entry_e = previous_entry_e + f" + {eingabe_elli.get()}"
        ellis_label_punkte = int(eingabe_elli.get()) + ellis_label_punkte
        if first_time_e:
            ellis_label_punkte_string = f"{str(ellis_label_punkte)}"
            first_time_e = False
        else:
            ellis_label_punkte_string = f"{previous_entry_e[3:]} = {str(ellis_label_punkte)}"
        ellis_label = Label(root, text=ellis_label_punkte_string, bg=background_color, fg='white')
        ellis_label.grid(row=15, column=0)
        eingabe_elli.delete(0, END)
    else:
        pass

def t_click():
    global tobis_label_punkte
    global tobis_label
    global previous_entry_t
    global first_time_t

    if is_integer(eingabe_tobi.get()):
        previous_entry_t = previous_entry_t + f" + {eingabe_tobi.get()}"
        tobis_label_punkte = int(eingabe_tobi.get()) + tobis_label_punkte
        if first_time_t:
            tobis_label_punkte_string = f"{str(tobis_label_punkte)}"
            first_time_t = False
        else:
            tobis_label_punkte_string = f"{previous_entry_t[3:]} = {str(tobis_label_punkte)}"
        tobis_label = Label(root, text=tobis_label_punkte_string, bg=background_color, fg='white')
        tobis_label.grid(row=18, column=0)
        eingabe_tobi.delete(0, END)
    else:
        pass

valis_button = Button(root, text="Vali", command=v_click, fg='white', bg=button_color,
                      height= 1, width=6, activebackground=active_button_color, activeforeground=active_button_text)
andis_button = Button(root, text="Andi", command=a_click, fg='white', bg=button_color,
                      height= 1, width=6, activebackground=active_button_color, activeforeground=active_button_text)
gregors_button = Button(root, text="Gregor", command=g_click, fg='white', bg=button_color,
                        height= 1, width=6, activebackground=active_button_color, activeforeground=active_button_text)
ellis_button = Button(root, text="Elli", command=e_click, fg='white', bg=button_color,
                      height= 1, width=6, activebackground=active_button_color, activeforeground=active_button_text)
tobis_button = Button(root, text="Tobi", command=t_click, fg='white', bg=button_color,
                      height= 1, width=6, activebackground=active_button_color, activeforeground=active_button_text)

# Putting it onto the screen
eingabe_vali.grid(row=5, column=0, padx=10, pady=10)
eingabe_andi.grid(row=8, column=0, padx=10, pady=10)
eingabe_gregor.grid(row=11, column=0, padx=10, pady=10)
eingabe_elli.grid(row=14, column=0, padx=10, pady=10)
eingabe_tobi.grid(row=17, column=0, padx=10, pady=10)

l0 = Label(root, text=' ', bg=background_color)
l0.grid(column=0, row=0)
l1 = Label(root, text='Punktezähler', bg=background_color, fg='white', font = "Verdana 14 bold")
l1.grid(column=0, row=1)
l0 = Label(root, text=' ', bg=background_color)
l0.grid(column=0, row=2)
#l2 = Label(root, text='\n', bg=background_color)
#l2.grid(column=0, row=2)
#l3 = Label(root, text='\n', bg=background_color)
#l3.grid(column=0, row=3)
#l4 = Label(root, text='\n', bg=background_color)
#l4.grid(column=0, row=4)
l7 = Label(root, text=' ', bg=background_color)
l7.grid(column=0, row=7)
l10 = Label(root, text=' ', bg=background_color)
l10.grid(column=0, row=10)
l13 = Label(root, text=' ', bg=background_color)
l13.grid(column=0, row=13)
l16 = Label(root, text=' ', bg=background_color)
l16.grid(column=0, row=16)

valis_button.grid(row=5, column=2, padx=10, pady=10)
andis_button.grid(row=8, column=2, padx=10, pady=10)
gregors_button.grid(row=11, column=2, padx=10, pady=10)
ellis_button.grid(row=14, column=2, padx=10, pady=10)
tobis_button.grid(row=17, column=2, padx=10, pady=10)

root.mainloop()