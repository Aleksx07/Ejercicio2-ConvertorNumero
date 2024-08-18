import tkinter as tk
from num2words import num2words

def convertir_numero():
    numero = entry.get()
    try:
        numero_en_palabras = num2words(int(numero), lang='es').upper()
        resultado_label.config(text=numero_en_palabras)
    except ValueError:
        resultado_label.config(text="Por favor, ingresa un número válido.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Convertor de Números a Palabras")
ventana.geometry("400x230")

# Entrada del número
label = tk.Label(ventana, text="Ingresa un número:")
label.pack(pady=10)
entry = tk.Entry(ventana)
entry.pack(pady=5)

# Botón para convertir
boton = tk.Button(ventana, text="Convertir", command=convertir_numero)
boton.pack(pady=10)

# Etiqueta para el título de la representación en palabras
titulo_label = tk.Label(ventana, text="Representación del número en palabras en Español:")
titulo_label.pack(pady=7)  # Empaquetar la etiqueta del título

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack(pady=10)

# Iniciar el loop principal de la ventana
ventana.mainloop()