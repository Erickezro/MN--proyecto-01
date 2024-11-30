import numpy as np
from tkinter import messagebox

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from solver import calcular_trayectoria

# Actualización de mostrar_resultados
def mostrar_resultados(v, ha, hc, alpha, d, L):
    """
    Grafica la trayectoria de la bomba y verifica el impacto.
    """
    x, y, impacto = calcular_trayectoria(v, ha, hc, alpha, d, L)
    
    # Convert the angle to radians
    alpha_rad = np.radians(alpha)
    inclinacion = np.tan(np.radians(alpha)) * hc  # Proyección horizontal del ángulo

    # Calculate the larger base
    base_mayor = L + 2 * hc * np.tan(alpha_rad)
    d2 = d + (base_mayor / 2) - 50
    
    # Coordenadas del trapecio isósceles invertido
    x_trapecio = [d2, d2 + L, d2 + L + hc * np.tan(alpha_rad), d2 - hc * np.tan(alpha_rad)]
    y_trapecio = [-hc, -hc, 0, 0]
    
    # Configurar la figura
    fig, ax = plt.subplots()
    ax.set_xlim(0, max(x) + 20)
    ax.set_ylim(min(y) - 20, ha + 20)
    ax.axhline(0, color="black", linestyle="-", label="Suelo")
    ax.set_title("Trayectoria de la bomba")
    ax.set_xlabel("Distancia (m)")
    ax.set_ylabel("Altura (m)")

    # Dibujar la trayectoria
    linea, = ax.plot([], [], lw=2, label="Trayectoria")
    ax.fill(x_trapecio, y_trapecio, color='brown', alpha=0.7, label="Cañón")
    
    # Actualizar la animación
    def actualizar(i):
        """
        Actualiza la línea de la trayectoria en cada frame de la animación.

        Parameters:
        i (int): El índice del frame actual de la animación.

        Returns:
        tuple: Una tupla que contiene la línea actualizada.
        """
        linea.set_data(x[:i], y[:i])
        return linea,

    # Crear la animación con repeat=False
    anim = FuncAnimation(fig, actualizar, frames=len(x), interval=20, blit=True, repeat=False)
    ax.legend()
    plt.show()

    # Mostrar mensaje de impacto después de la animación
    if impacto[0]:
        if impacto[2] == 0:
            messagebox.showinfo("Resultado", f"La bomba impactó en el suelo en x = {impacto[1]:.2f} m.")
        else:
            messagebox.showinfo("Resultado", f"La bomba impactó dentro del cañón en x = {impacto[1]:.2f} m, y = {impacto[2]:.2f} m.")
    else:
        messagebox.showinfo("Resultado", "La bomba no impactó el cañón ni el suelo.")
