import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solver import calcular_trayectoria
import numpy as np

def mostrar_resultados(v, ha, hc, alpha, d, L):
    x, y = calcular_trayectoria(v, ha, hc, alpha, d, L)

    # Configurar la figura
    fig, ax = plt.subplots()
    ax.set_xlim(0, max(x) + 10)
    #ax.set_ylim(0, max(ha, hc) + 10)
    ax.set_ylim(-hc - 10, max(ha, hc) + 10)
    plt.axhline(0, color="black", linestyle="-", label="suelo")
    ax.set_title("Trayectoria de la bomba")
    ax.set_xlabel("Distancia (m)")
    ax.set_ylabel("Altura (m)")

    # Línea para la trayectoria
    linea, = ax.plot([], [], label="Trayectoria", lw=2)
    ax.legend()
    
    # Calcular las coordenadas del cañón
    h_canon = -hc  # Por debajo del eje y = 0
    base_superior = d
    base_inferior = d + L
    inclinacion = np.tan(np.radians(alpha)) * hc #horizontal por altura y el angulo
    
    # Coordenadas del trapecio isósceles invertido
    x_trapecio = [d - inclinacion, d + L + inclinacion, d + L, d]
    y_trapecio = [0, 0, h_canon, h_canon]

    # Dibujar el cañón como un trapecio
    ax.fill(x_trapecio, y_trapecio, color='brown', alpha=0.7, label="Cañón")

    # Función para animación
    def actualizar(i):
        linea.set_data(x[:i], y[:i])
        return linea,

    # Animación
    anim = FuncAnimation(fig, actualizar, frames=len(x), interval=20, blit=True)

    plt.legend()
    plt.show()
