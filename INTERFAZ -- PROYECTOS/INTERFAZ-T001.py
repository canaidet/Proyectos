import tkinter as tk
from tkinter import Tk, Label, Button, Entry
vent = Tk()
vent.title("INTERFAZ-T001")
vent.geometry("250x500")
""" 
Button_1 = Button(vent, text = "Generador de contraseña", fg = "White", bg= "Black")
Button_1.place(x=10, y=10, width=200, height=30)

Texto_1 = Label(vent, text = "Generador de contraseña \n de todo tipo", fg = "Black")
Texto_1.place(x=10, y=40, width=200, height=30)

Button_2 = Button(vent, text = "Descargador de imagen", fg = "White", bg= "Black")
Button_2.place(x=10, y=100, width=200, height=30) """

# def Carculo():
#   Valor1 = float(num1.get())
#   Valor2 = float(num2.get())
#   resultado = Valor1 + Valor2
#   labelresultado.config(text=f"Resultado: {resultado}")

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



# hello = tk.Label(text="Ingrece Valor")
# hello.pack()

# num1 = tk.Entry(window)
# num1.config(font="Arial 20", width=10)
# num1.pack()

# Label = tk.Label(text="Ingrece Cantidad")
# Label.pack()

# num2 = tk.Entry(window)
# num2.config(font="Arial 20", width=10)
# num2.pack()


# button = tk.Button(text="Click me!")
# button.pack()

# labelresultado = tk.Label(text="Resultado: ")
# labelresultado.pack()


vent.mainloop()