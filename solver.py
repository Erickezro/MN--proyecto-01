import numpy as np

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
    #calcular la inclinacion lateral del trapecio
    alpha_rad = np.radians(alpha)  # Convertir ángulo a radianes
    inclinacion = np.tan(alpha_rad)
    
    t_total = np.sqrt(2 * (ha + hc) / g)  # Tiempo de vuelo (considerando caída libre)
    x_impacto = d + L / 2  #Posicion del impacto (centro canon)
    
    # Determinar la posición inicial del avión
    x0 = x_impacto - v * t_total  # Posición horizontal inicial del avión
    
    t = np.linspace(0, t_total, 500)  # Tiempo dividido en puntos
    x = x0 +v * t  # Posición horizontal
    y = ha - 0.5 * g * t**2  # Posición vertical
    
    # Verificar si la bomba impacta el cañón
    impacto_x = x[(x >= d) & (x <= d + L)]
    impacto_y = y[(x >= d) & (x <= d + L)]
    if any((impacto_y <= 0) & (impacto_y >= -hc)):
        print("¡Impacto exitoso en el cañón!")
    else:
        print("La bomba no impacta en el cañón.")
        
    return x, y
