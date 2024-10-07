from novaktais import Raza
import tkinter as tk   
from tkinter import ttk, END

#raza
visi_raza = []

#ekrāns
root = tk.Tk()
root.title("Dārza pieraksti")
root.geometry("500x500")

frame = ttk.Frame(root)
frame.grid(padx=10, pady=10)

#field options
options = {'padx':5, 'pady':5}

# label
novakta_label = ttk.Label(frame, text="Ievadi info par novakto")
novakta_label.grid(column=0, row=0, sticky="w", **options)

# nomainit sarakstu

def nomainit_sarakstu():
    listbox.delete(0,END)
    for raza in visi_raza:
        listbox.insert("end","{},{},{}".format(raza.name, raza.weight, raza.fruitorvegetable))

# nosaukums entry
nosaukums = tk.StringVar()

nosaukums_entry = ttk.Entry(frame, textvariable=nosaukums)
nosaukums_entry.grid(column=1, row=0, **options)
nosaukums_entry.focus()

# daudzums entry

daudzums = tk.IntVar()

daudzums_entry = ttk.Entry(frame, textvariable=daudzums)
daudzums_entry.grid(column=1, row=1, **options)


# aVAId entry

aVAId = tk.StringVar()

aVAId_entry = ttk.Entry(frame, textvariable=aVAId)
aVAId_entry.grid(column=1, row=2, **options)


# jaunais nosaukums

jaunais_nosaukums = tk.StringVar()

jaunais_nosaukums_entry = ttk.Entry(frame, textvariable=jaunais_nosaukums)
jaunais_nosaukums_entry.grid(column=6, row=3, **options)

#jaunais nosaukums button

def jaunais_nosaukums_button_clicked():
    jaunaisVards = jaunais_nosaukums.get()  # Retrieve the new name first
    if not jaunaisVards:
        result_label.config(text="Lūdzu, ievadiet jauno vārdu.")
        return

    for izveletais in listbox.curselection():
        visi_raza[izveletais].jaunais_nosaukums(jaunaisVards)
    
    result_label.config(text="Vārds mainīts veiksmīgi.")
    nomainit_sarakstu()

jaunais_nosaukums_button = ttk.Button(frame, text='mainīt vārdu')
jaunais_nosaukums_button.grid(column=7, row=3, sticky='W',**options)
jaunais_nosaukums_button.configure(command=jaunais_nosaukums_button_clicked)

# jaunais avaid

jaunais_avaid = tk.StringVar()
jaunais_avaid_entry = ttk.Entry(frame, textvariable=jaunais_avaid)
jaunais_avaid_entry.grid(column=6, row=4, **options)

#jaunais avaid button

def jaunais_avaid_button_clicked():
    javaid = jaunais_avaid.get()  # Retrieve the new name first
    if not javaid:
        result_label.config(text="Lūdzu, ievadiet jauno a vai d.")
        return

    for izveletais in listbox.curselection():
        visi_raza[izveletais].jaunais_avaid(javaid)
    
    result_label.config(text="a vai d mainīts veiksmīgi.")
    nomainit_sarakstu()

jaunais_avaid_button = ttk.Button(frame, text='mainīt a vai d')
jaunais_avaid_button.grid(column=7, row=4, sticky='W',**options)
jaunais_avaid_button.configure(command=jaunais_avaid_button_clicked)
# aped entry

cik_aped = tk.IntVar()
cik_aped_entry = ttk.Entry(frame, textvariable= cik_aped)
cik_aped_entry.grid(column=6, row=5)

# aped

def aped_button_clicked(): 
    jaunais_teksts=""
    for izveletais in listbox.curselection():

        visi_raza[izveletais].aped()
        jaunais_teksts += visi_raza[izveletais].info() + "\n"

    result_label.config(text=jaunais_teksts)
    nomainit_sarakstu()

# aped button

aped_button = ttk.Button(frame, text='apēdu 1 kg')
aped_button.grid(column=7, row=5, sticky='W',**options)
aped_button.configure(command=aped_button_clicked)

#listbox button 
def novaktaisList_button_clicked():
    raza_nosuakums = nosaukums.get()
    raza_daudzums = daudzums.get()
    raza_aVAId = aVAId.get()

    visi_raza.append(Raza(raza_nosuakums, raza_daudzums, raza_aVAId))
    result_label.config(text=visi_raza[-1].info())
    nomainit_sarakstu()

#listbox

listSaturs = tk.Variable(value=tuple(visi_raza))

listbox = tk.Listbox(
    root,
    listvariable= listSaturs,
    height=8,
    selectmode=tk.EXTENDED
)
listbox.grid(columnspan = 3, row = 4, **options)


#poga ar kuru ievieto ražu

def novaktais_button_clicked():
    ievaditais = nosaukums.get(), daudzums.get(), aVAId.get()
    result_label.config(text=ievaditais)

novaktais_button = ttk.Button(frame, text='ievadīt novākto')
novaktais_button.grid(column=2, row=0, sticky='W',**options)
novaktais_button.configure(command=novaktaisList_button_clicked)


#result label

result_label = ttk.Label(frame)
result_label.grid(row=4, columnspan=3, **options)

#add padding to the frame un parādi to

frame.grid(padx=10, pady=10)

#atver aplikāciju

root.mainloop()

