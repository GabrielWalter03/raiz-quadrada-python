import tkinter as tk
from tkinter import messagebox
import math

def calcular_raizes():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        # Calcula o discriminante
        delta = b**2 - 4*a*c
        
        if delta > 0:
            # Duas raízes reais distintas
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            resultado = f"Duas raízes reais:\nX1 = {raiz1:.2f}\nX2 = {raiz2:.2f}"
        elif delta == 0:
            # Uma raiz real
            raiz = -b / (2 * a)
            resultado = f"Uma raiz real:\nX = {raiz:.2f}"
        else:
            # Raízes complexas
            real = -b / (2 * a)
            imag = math.sqrt(-delta) / (2 * a)
            resultado = f"Raízes complexas:\nX1 = {real:.2f} + {imag:.2f}i\nX2 = {real:.2f} - {imag:.2f}i"
        
        messagebox.showinfo("Resultado", resultado)
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "O coeficiente 'a' não pode ser zero.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora de Raízes de Equação do 2° Grau")

# Labels e campos de entrada para os coeficientes
tk.Label(root, text="Coeficiente a:").grid(row=0, column=0, padx=10, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Coeficiente b:").grid(row=1, column=0, padx=10, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Coeficiente c:").grid(row=2, column=0, padx=10, pady=5)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1, padx=10, pady=5)

# Botão para calcular as raízes
button_calcular = tk.Button(root, text="Calcular Raízes", command=calcular_raizes)
button_calcular.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
