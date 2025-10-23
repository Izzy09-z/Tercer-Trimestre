import tkinter as tk

# Lista de productos: cada producto es una tupla (nombre, precio, cantidad)
productos = [
    ("Manzanas", 10.50, 20),
    ("Naranjas", 8.75, 15),
    ("Plátanos", 6.30, 30),
    ("Leche", 12.00, 10)
]

def mostrar_productos():
    # Limpiar el texto antes de mostrar la lista
    texto.delete("1.0", tk.END)
    for nombre, precio, cantidad in productos:
        texto.insert(tk.END, f"Producto: {nombre}\nPrecio: ${precio:.2f}\nCantidad: {cantidad}\n\n")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Visualizador de Productos")
titulo = tk.Label(ventana, text="Lista de Productos" , font= ("Arial" , 14 , "bold"))
titulo. pack (pady=10)

# Crear un botón para mostrar productos
boton_mostrar = tk.Button(ventana, text="Mostrar productos", command=mostrar_productos)
boton_mostrar.pack(pady=10)

# Crear un widget Text para mostrar la lista de productos
texto = tk.Text(ventana, width=40, height=15)
texto.pack(padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()