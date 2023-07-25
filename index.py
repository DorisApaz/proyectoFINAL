import tkinter as tk
from tkinter import ttk
from app import logica 

def calcular_ruta_optima():
    try:    
        origen = origen_var.get()
        destino = destino_var.get()
        if(origen == "" or destino == "") : return
        # Aquí puedes agregar la lógica para calcular la ruta óptima utilizando los valores seleccionados
        strRoute = logica(origen, destino)
        mensaje_texto.configure(text="Ruta óptima calculada: " + str(strRoute), foreground="black")
    except:
        mensaje_texto.configure(text="Ruta óptima calculada: " + "No existe ruta para llegar al destino", foreground="red")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ciudad ILO")

# Crear estilo
style = ttk.Style()
style.theme_use("clam")  # Puedes elegir otros temas según tus preferencias

# Crear el título centrado
titulo = ttk.Label(ventana, text="Calculadora de Ruta Óptima", font=("Helvetica", 16, "bold"), padding=20)
titulo.pack()

# Crear los select de ciudad origen y destino
origen_label = ttk.Label(ventana, text="Seleccionar punto origen:")
origen_label.pack()
origen_var = tk.StringVar()
origen_select = ttk.Combobox(ventana, textvariable=origen_var)
tupla_v = tuple(f'v{i}' for i in range(1, 50))

origen_select["values"] = tupla_v  # Agrega aquí las opciones de ciudades disponibles
origen_select.pack()

destino_label = ttk.Label(ventana, text="Seleccionar punto destino:")
destino_label.pack()
destino_var = tk.StringVar()
destino_select = ttk.Combobox(ventana, textvariable=destino_var)
destino_select["values"] = tupla_v  # Agrega aquí las opciones de ciudades disponibles
destino_select.pack()

# Crear el botón de calcular ruta óptima
calcular_btn = ttk.Button(ventana, text="Calcular Ruta Óptima", command=calcular_ruta_optima)
calcular_btn.pack(pady=20)

# Crear el panel de mensajes de texto
mensaje_texto = ttk.Label(ventana, text="")
mensaje_texto.pack()

# Ejecutar la interfaz
ventana.mainloop()
