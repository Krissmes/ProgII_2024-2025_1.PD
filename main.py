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

#field options
options = {'padx':5, 'padx':5}

# label
novakta_label = ttk.Label(frame, text="Ievadi info par novakto")
novakta_label.grid(column=0, row=0, sitcky="w", **options)

# nosaukums entry
nosaukums = tk.StringVar()

nosaukums_entry = ttk.Entry(frame, textvariable=nosaukums)
nosaukums_entry.grid(column=1, row=0, **options)
nosaukums_entry.focus()

# daudzums entry

daudzums = tk.IntVar()

daudzums_entry = ttk.Entry(frame, textvariable=daudzums)
daudzums_entry.grid(column=1, row=1, **options)
daudzums_entry.focus()

# aVAId entry

aVAId = tk.StringVar()

aVAId_entry = ttk.Entry(frame, textvariable=aVAId)
aVAId_entry.grid(column=1, row=2, **options)
aVAId_entry.focus()

def novaktais_button_clicked():
     