import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solver import calcular_trayectoria

def mostrar_resultados(v, ha, hc, alpha, d, L):
    x, y = calcular_trayectoria(v, ha, hc, alpha, d, L)

    # Configurar la figura
    fig, ax = plt.subplots()
    ax.set_xlim(0, max(x) + 10)
    ax.set_ylim(0, max(ha, hc) + 10)
    ax.set_title("Trayectoria de la bomba")
    ax.set_xlabel("Distancia (m)")
    ax.set_ylabel("Altura (m)")

    # Línea para la trayectoria
    linea, = ax.plot([], [], label="Trayectoria", lw=2)
    ax.legend()

    # Función para animación
    def actualizar(i):
        linea.set_data(x[:i], y[:i])
        return linea,

    # Animación
    anim = FuncAnimation(fig, actualizar, frames=len(x), interval=20, blit=True)

    # Mostrar cañón
    ax.plot([d, d + L], [hc, hc], 'r-', label="Cañón")

    plt.show()
