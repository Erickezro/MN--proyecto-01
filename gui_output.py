import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solver import calcular_trayectoria
import numpy as np
from tkinter import messagebox

# Actualización de mostrar_resultados
def mostrar_resultados(v, ha, hc, alpha, d, L):
    """
    Grafica la trayectoria de la bomba y verifica el impacto.
    """
    x, y, impacto = calcular_trayectoria(v, ha, hc, alpha, d, L)
    
    # Coordenadas del cañón
    h_canon = -hc  # Altura negativa para estar debajo del suelo
    inclinacion = np.tan(np.radians(alpha)) * hc  # Proyección horizontal del ángulo
    base_superior = d
    base_inferior = d + L
    
    # Coordenadas del trapecio isósceles invertido
    x_trapecio = [base_superior - inclinacion, base_inferior + inclinacion, base_inferior, base_superior]
    y_trapecio = [0, 0, h_canon, h_canon]
    
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
        linea.set_data(x[:i], y[:i])
        return linea,

    anim = FuncAnimation(fig, actualizar, frames=len(x), interval=20, blit=True)
    ax.legend()
    plt.show()

    # Mostrar mensaje de impacto
    if impacto[0]:
        if impacto[2] == 0:
            messagebox.showinfo("Resultado", f"La bomba impactó en el suelo en x = {impacto[1]:.2f} m.")
        else:
            messagebox.showinfo("Resultado", f"La bomba impactó dentro del cañón en x = {impacto[1]:.2f} m, y = {impacto[2]:.2f} m.")
    else:
        messagebox.showinfo("Resultado", "La bomba no impactó el cañón ni el suelo.")