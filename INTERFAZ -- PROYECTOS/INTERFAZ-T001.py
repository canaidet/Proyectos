import tkinter as tk
from tkinter import Tk, Label, Button, Entry
vent = Tk()
vent.title("INTERFAZ-T001")
vent.geometry("250x500")
def contra():
  contra = imput_contraseña.get()
  print(contra)
  label2 = tk.Label(text=f"La contraseña es: {contra}")
  label2.pack()
  
label1 = tk.Label(text="Code")
label1.pack()

imput_contraseña = tk.Entry(vent)
imput_contraseña.config(width=15)
imput_contraseña.pack()

Botton = tk.Button(text="Generar", command=contra)
imput_contraseña.config()
Botton.pack()

vent.mainloop()
