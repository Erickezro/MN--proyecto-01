import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



# Actualización de calcular_trayectoria
def calcular_trayectoria(v, ha, hc, alpha, d, L, g=9.81):
    """
    Calcula la trayectoria de la bomba y verifica el impacto.
    
    Parámetros:
    v: Velocidad del avión (m/s).
    ha: Altura del avión al soltar la bomba (m).
    hc: Altura del cañón (m).
    alpha: Ángulo de inclinación del cañón (grados).
    d: Distancia horizontal inicial desde el borde del cañón (m).
    L: Longitud superior del cañón (m).
    g: Aceleración gravitacional (m/s^2).
    
    Retorna:
    x: Coordenadas horizontales de la trayectoria.
    y: Coordenadas verticales de la trayectoria.
    impacto: Tuple con (True/False, coordenada impacto)
    """
    # Convertir el ángulo del cañón a radianes
    alpha_rad = np.radians(alpha)
    
    # Tiempo inicial estimado con caída libre desde ha
    t_total = np.sqrt(2 * ha / g)
    
    # Crear un conjunto de tiempos con pasos más pequeños para mayor precisión
    t = np.linspace(0, t_total, 1000)
    
    # Trayectoria de la bomba
    x = v * t
    y = ha - 0.5 * g * t**2
    
    # Verificar si la bomba impacta el suelo
    suelo_idx = np.where(y <= 0)[0]
    if len(suelo_idx) > 0:
        impacto_idx = suelo_idx[0]
        x = x[:impacto_idx + 1]
        y = y[:impacto_idx + 1]
        return x, y, (True, x[-1], 0)  # Impacto en el suelo

    # Verificar impacto en el cañón
    x_canon = np.array([d, d + L])
    y_canon = np.array([-hc, -hc])
    for xi, yi in zip(x, y):
        if d <= xi <= d + L and yi <= 0:
            return x[:len(x)], y[:len(y)], (True, xi, yi)
    
    return x, y, (False, None, None)

