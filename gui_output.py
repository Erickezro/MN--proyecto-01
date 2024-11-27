import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solver import calcular_trayectoria
import numpy as np

def mostrar_resultados(v, ha, hc, alpha, d, L):
    x, y = calcular_trayectoria(v, ha, hc, alpha, d, L)
    
    # Coordenadas del cañón
    h_canon = -hc  # Altura negativa para estar debajo del suelo
    inclinacion = np.tan(np.radians(alpha)) * hc  # Proyección horizontal del ángulo
    base_superior = d
    base_inferior = d + L
    
    # Coordenadas del trapecio isósceles invertido
    x_trapecio = [base_superior - inclinacion, base_inferior + inclinacion, base_inferior, base_superior]
    y_trapecio = [0, 0, h_canon, h_canon]
    
    # Determinar límites del gráfico para incluir todo el cañón
    x_min = min(min(x), base_superior - inclinacion) - 10
    x_max = max(max(x), base_inferior + inclinacion) + 10
    y_min = min(min(y), h_canon) - 10
    y_max = max(max(y), ha) + 10

    # Configurar la figura
    fig, ax = plt.subplots()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    
    ax.axhline(0, color="black", linestyle="-", label="suelo")
    ax.set_title("Trayectoria de la bomba")
    ax.set_xlabel("Distancia (m)")
    ax.set_ylabel("Altura (m)")

    # Línea para la trayectoria
    linea, = ax.plot([], [], label="Trayectoria", lw=2)

    # Dibujar el cañón como un trapecio
    ax.fill(x_trapecio, y_trapecio, color='brown', alpha=0.7, label="Cañón")

    # Función para animación
    def actualizar(i):
        linea.set_data(x[:i], y[:i])
        return linea,

    # Animación
    anim = FuncAnimation(fig, actualizar, frames=len(x), interval=20, blit=True)

    ax.legend()
    plt.show()
