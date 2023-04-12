from tkinter import *

background_color = '#FFE3B3'
button_color = "#30A0E0"

root = Tk()
root.title("Punktezähler")
root.configure(background=background_color)

# Creating a label widget
valis_label_punkte = 0
valis_label = Label(root, text=valis_label_punkte) # brauch ich die zeilen überhaupt???
andis_label_punkte = 0
andis_label = Label(root, text=andis_label_punkte)
gregors_label_punkte = 0
gregors_label = Label(root, text=gregors_label_punkte)
ellis_label_punkte = 0
ellis_label = Label(root, text=ellis_label_punkte)

angezeigte_punkte_v = 0
angezeigte_punkte_a = 0
angezeigte_punkte_g = 0
angezeigte_punkte_e = 0

# Creating entry fields
eingabe_vali = Entry(root, width=30, borderwidth=3)
eingabe_andi = Entry(root, width=30, borderwidth=3)
eingabe_gregor = Entry(root, width=30, borderwidth=3)
eingabe_elli = Entry(root, width=30, borderwidth=3)

# Creating submit buttons
first_time_v = True
previous_entry_v = "0"
first_time_a = True
previous_entry_a = "0"
first_time_g = True
previous_entry_g = "0"
first_time_e = True
previous_entry_e = "0"


def v_click():
    global valis_label_punkte
    global valis_label
    global previous_entry_v
    global first_time_v
    previous_entry_v = previous_entry_v + f" + {eingabe_vali.get()}"
    valis_label_punkte = int(eingabe_vali.get()) + valis_label_punkte
    if first_time_v:
        valis_label_punkte_string = f"{str(valis_label_punkte)}"
        first_time_v = False
    else:
        valis_label_punkte_string = f"{previous_entry_v[3:]} = {str(valis_label_punkte)}"
    valis_label = Label(root, text=valis_label_punkte_string, bg=background_color)
    valis_label.grid(row=6, column=0)
    eingabe_vali.delete(0, END)

def a_click():
    global andis_label_punkte
    global andis_label
    global previous_entry_a
    global first_time_a
    previous_entry_a = previous_entry_a + f" + {eingabe_andi.get()}"
    andis_label_punkte = int(eingabe_andi.get()) + andis_label_punkte
    if first_time_a:
        andis_label_punkte_string = f"{str(andis_label_punkte)}"
        first_time_a = False
    else:
        andis_label_punkte_string = f"{previous_entry_a[3:]} = {str(andis_label_punkte)}"
    andis_label = Label(root, text=andis_label_punkte_string, bg=background_color)
    andis_label.grid(row=9, column=0)
    eingabe_andi.delete(0, END)

def g_click():
    global gregors_label_punkte
    global gregors_label
    global previous_entry_g
    global first_time_g
    previous_entry_g = previous_entry_g + f" + {eingabe_gregor.get()}"
    gregors_label_punkte = int(eingabe_gregor.get()) + gregors_label_punkte
    if first_time_g:
        gregors_label_punkte_string = f"{str(gregors_label_punkte)}"
        first_time_g = False
    else:
        gregors_label_punkte_string = f"{previous_entry_g[3:]} = {str(gregors_label_punkte)}"
    gregors_label = Label(root, text=gregors_label_punkte_string, bg=background_color)
    gregors_label.grid(row=12, column=0)
    eingabe_gregor.delete(0, END)

def e_click():
    global ellis_label_punkte
    global ellis_label
    global previous_entry_e
    global first_time_e
    previous_entry_e = previous_entry_e + f" + {eingabe_elli.get()}"
    ellis_label_punkte = int(eingabe_elli.get()) + ellis_label_punkte
    if first_time_e:
        ellis_label_punkte_string = f"{str(ellis_label_punkte)}"
        first_time_e = False
    else:
        ellis_label_punkte_string = f"{previous_entry_e[3:]} = {str(ellis_label_punkte)}"
    ellis_label = Label(root, text=ellis_label_punkte_string, bg=background_color)
    ellis_label.grid(row=15, column=0)
    eingabe_elli.delete(0, END)

valis_button = Button(root, text="Vali", command=v_click, fg='white', bg=button_color)
andis_button = Button(root, text="Andi", command=a_click, fg='white', bg=button_color)
gregors_button = Button(root, text="Gregor", command=g_click, fg='white', bg=button_color)
ellis_button = Button(root, text="Elli", command=e_click, fg='white', bg=button_color)

# Putting it onto the screen
eingabe_vali.grid(row=5, column=0, padx=10, pady=10)
eingabe_andi.grid(row=8, column=0, padx=10, pady=10)
eingabe_gregor.grid(row=11, column=0, padx=10, pady=10)
eingabe_elli.grid(row=14, column=0, padx=10, pady=10)

#valis_label.grid(row=1, column=0)
#andis_label.grid(row=3, column=0)
#gregors_label.grid(row=5, column=0)
#ellis_label.grid(row=7, column=0)

l0 = Label(root, text='\n', bg=background_color)
l0.grid(column=0, row=0)
l1 = Label(root, text='\n', bg=background_color)
l1.grid(column=0, row=1)
l2 = Label(root, text='\n', bg=background_color)
l2.grid(column=0, row=2)
l3 = Label(root, text='\n', bg=background_color)
l3.grid(column=0, row=3)
l4 = Label(root, text='\n', bg=background_color)
l4.grid(column=0, row=4)
l7 = Label(root, text='\n', bg=background_color)
l7.grid(column=0, row=7)
l10 = Label(root, text='\n', bg=background_color)
l10.grid(column=0, row=10)
l13 = Label(root, text='\n', bg=background_color)
l13.grid(column=0, row=13)
l16 = Label(root, text='\n', bg=background_color)
l16.grid(column=0, row=16)

valis_button.grid(row=5, column=2, padx=10, pady=10)
andis_button.grid(row=8, column=2, padx=10, pady=10)
gregors_button.grid(row=11, column=2, padx=10, pady=10)
ellis_button.grid(row=14, column=2, padx=10, pady=10)

root.mainloop()

#def click():