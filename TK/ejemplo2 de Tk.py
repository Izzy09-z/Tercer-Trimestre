import tkinter as tk

# --------------------------- FUNCIONES ---------------------------------
def sumar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado.set(str(n1 + n2))          # Convertimos a cadena para mostrar
    except ValueError:
        resultado.set("Error")

# ------------------------- Ventana Principal ---------------------------
ventana = tk.Tk()                     # <-- Paréntesis
ventana.title("Calculadora Básica")
ventana.geometry("250x180")           # Tamaño

# ------------------------- Variables ---------------------------------
resultado = tk.StringVar()            # Después de crear la ventana

# -------------------------- Widgets ----------------------------------
tk.Label(ventana, text="Número 1: ").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Número 2: ").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Suma", command=sumar).pack(pady=5)

tk.Label(ventana, text="Resultado: ").pack()
tk.Label(ventana,
         textvariable=resultado,
         fg="blue",
         font=("Arial", 12)).pack(pady=5)

# -------------------- Loop Principal -------------------------------
ventana.mainloop()