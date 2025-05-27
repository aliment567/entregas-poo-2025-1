# Importamos las herramientas necesarias de la librería Tkinter.
# Esta librería nos permite crear ventanas y elementos gráficos.
import tkinter as tk
from tkinter import messagebox


# La clase se encargará de construir la ventana y manejar lo que hace cada botón.
class AplicacionSaludo:
    def __init__(self):
        # Creamos la ventana principal de la aplicación
        self.ventana = tk.Tk()
        self.ventana.title("Aplicación de Saludo")  
        self.ventana.geometry("500x350")
        self.ventana.resizable(False, False)  

        # Etiqueta (Label) que le dice al usuario qué debe escribir
        self.label_nombre = tk.Label(self.ventana, text="porfaor ingrese su nombre:")
        self.label_nombre.pack(pady=10) 

        # Cuadro de texto donde el usuario va a escribir su nombre
        self.entrada_nombre = tk.Entry(self.ventana, width=30)
        self.entrada_nombre.pack()

        # Botón que cuando se hace clic, saluda al usuario
        self.boton_saludar = tk.Button(self.ventana, text="Saludar", command=self.saludar)
        self.boton_saludar.pack(pady=5)

        self.boton_salir = tk.Button(self.ventana, text="Salir", command=self.ventana.quit)
        self.boton_salir.pack()

    # Esta función se llama cuando el usuario hace clic en el botón "Saludar"
    def saludar(self):
        nombre = self.entrada_nombre.get()  
        if nombre.strip() == "":
            
            messagebox.showwarning("Advertencia", "Por favor ingrese un nombre.")
        else:
            
            messagebox.showinfo("Saludo", f"Hola {nombre}")

    # Esta función arranca la aplicación y mantiene la ventana abierta
    def ejecutar(self):
        self.ventana.mainloop()

# Esta parte del código se asegura de que la aplicación solo se ejecute si este archivo es el principal
if __name__ == "__main__":
    app = AplicacionSaludo()  
    app.ejecutar()  
