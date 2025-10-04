import tkinter as tk
#---------------------------FUNCIONES---------------------------------
def sumar():
    try:
        n1=float (entrada1.get())
        n2=float (entrada2.get())
        resultado.set(n1+n2)
    except ValueError:
        resultado.set("Error")

#-------------------------Ventada Principal----------------------------
ventana = tk.Tk
ventana.title("Calculadora Basica")
ventana.geometry ("250x180") #Tamaño

#-------------------------Variable-------------------------------
resultado=tk.StringVar()

#----------------------------------Widgets------------------------
tk.Label(ventana, tex="numero 1: "). pack(padu=5)
entrada=tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana,text="numero 2: "). pack (pady=5)
entrada2=tk.Entry(ventana)
entrada2.pack()

tk.Button (ventana, text="suma" , command=sumar). pack(pady=5)
tk.Label(ventana, text="Resultado: "). pack
tk.Label(ventana, textvariable=resultado, fg="blue" ,font=("Arial",12)). pack()

#--------------------Loop Principal------------------------
ventana.mainloop()