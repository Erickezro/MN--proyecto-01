import numpy as np
from scipy.interpolate import interp1d

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
    """
    # Convertir el ángulo del cañón a radianes
    alpha_rad = np.radians(alpha)
    
    # Calcular el tiempo total de vuelo basado en la altura del avión
    t_total = np.sqrt(2 * ha / g)
    
    # Calcular posición horizontal inicial del avión
    x0 = v * t_total  # Avión se encuentra antes del origen aqui la velocidad es negativa 
    
    # Crear una división de tiempo más detallada para la trayectoria
    t = np.linspace(0, t_total, 500)
    x = x0 + v * t  # Posición horizontal
    y = ha - 0.5 * g * t**2  # Posición vertical

    # Verificar si la bomba impacta dentro del área del cañón
    if np.any((x >= d) & (x <= d + L)):
        # Identificar los puntos de intersección relevantes
        indices = np.where((x >= d) & (x <= d + L))[0]
        x_relevante = x[indices]
        y_relevante = y[indices]
        
        # Interpolación lineal para encontrar el punto exacto de impacto
        interpolador = interp1d(x_relevante, y_relevante, kind="linear", fill_value="extrapolate")
        y_impacto = interpolador(d)  # Altura en la posición del cañón
        
        if -hc <= y_impacto <= 0:
            print(f"¡Impacto exitoso en el cañón! Punto de impacto: x = {d:.2f}, y = {y_impacto:.2f}")
        else:
            print("La bomba pasa por encima o debajo del cañón.")
    else:
        print("La bomba no impacta en el cañón.")
    
    return x, y


