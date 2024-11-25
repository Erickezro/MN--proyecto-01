import numpy as np

def calcular_trayectoria(v, ha, hc, alpha, d, L, g=9.81):
    """
    Calcula la trayectoria de la bomba y verifica el impacto.
    """
    alpha_rad = np.radians(alpha)  # Convertir ángulo a radianes
    t_total = np.sqrt(2 * ha / g)  # Tiempo de vuelo (considerando caída libre)
    t = np.linspace(0, t_total, 500)  # Tiempo dividido en puntos
    x = v * t + d  # Posición horizontal
    y = ha - 0.5 * g * t**2  # Posición vertical
    return x, y
