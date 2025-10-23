import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Presupuesto con Tkinter")
ventana.geometry("300x300")

# Etiquetas y entradas
tk.Label(ventana, text="Decoración:").pack()
decoracion = tk.Entry(ventana)
decoracion.pack()

tk.Label(ventana, text="Comida:").pack()
comida = tk.Entry(ventana)
comida.pack()

tk.Label(ventana, text="Música:").pack()
musica = tk.Entry(ventana)
musica.pack()

tk.Label(ventana, text="Transporte:").pack()
transporte = tk.Entry(ventana)
transporte.pack()

# Función para calcular el total
def calcular():
    d = float(decoracion.get() or 0)
    c = float(comida.get() or 0)
    m = float(musica.get() or 0)
    t = float(transporte.get() or 0)
    total = d + c + m + t
    resultado.config(text="Total: $" + str(total))


# Botón y resultado
tk.Button(ventana, text="Calcular total", command=calcular).pack()
resultado = tk.Label(ventana, text="Total: $0")
resultado.pack()

ventana.mainloop()