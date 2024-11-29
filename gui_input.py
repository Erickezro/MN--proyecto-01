import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Para manejar imágenes
from gui_output import mostrar_resultados
      
# Modificar estilo y disposición
def bienvenida():
    ventana = tk.Tk()
    ventana.title("Información del Proyecto")
    ventana.geometry("600x700")
    ventana.resizable(False, False)

    # color de fondo
    ventana.configure(bg="#e6f7ff")

    # Estilo
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Blue.TLabel", background="#e6f7ff", foreground="#003366", font=("Arial", 16, "bold"))
    style.configure("Normal.TLabel", background="#e6f7ff", foreground="#003366", font=("Arial", 12))
    style.configure("Blue.TButton", background="#003366", foreground="white", font=("Arial", 14, "bold"))
    style.map("Blue.TButton", background=[("active", "#00509e")])

    # Contenedor principal
    frame = ttk.Frame(ventana, style="Blue.TLabel")
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Universidad al principio
    info = "Escuela Politécnica Nacional"
    ttk.Label(frame, text=f"Universidad: {info}", style="Blue.TLabel").pack(pady=(20, 10))

    # Tema después de la universidad
    tema = "Simulación de la caída de una bomba"
    ttk.Label(frame, text=f"Tema: {tema}", style="Blue.TLabel", wraplength=500, justify="center").pack(pady=(10, 20))

    # Imagen al centro
    try:
        img = Image.open("imagenAvion.jpg")  # Cambia "logo.png" por tu imagen
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)

        img_label = tk.Label(frame, image=img_tk, bg="#e6f7ff")
        img_label.image = img_tk
        img_label.pack(pady=(10, 20))
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

    # Integrantes al final
    integrantes = ["Alexis Bautista", "David Egas", "Aubertin Ochoa", "Erick Romero"]
    tema = "Simulación de la caída de una bomba"

    # Etiquetas centradas
    label_uni = ttk.Label(frame, text=f"Universidad: {info}", style="Blue.TLabel")
    label_uni.pack(pady=20)

    for integrante in integrantes:
        label_integrante = ttk.Label(frame, text=f"Integrante: {integrante}", style="Blue.TLabel")
        label_integrante.pack(pady=10)

    label_tema = ttk.Label(frame, text=f"Tema: {tema}", style="Blue.TLabel", wraplength=500, justify="center")
    label_tema.pack(pady=20)

    # Botón llamativo
    btn_ingreso = ttk.Button(frame, text="Ir a ingreso de datos", style="Blue.TButton", command=lambda: [ventana.destroy(), abrir_interfaz()])
    btn_ingreso.pack(pady=20)

    ventana.mainloop()
    ##linea de prueba para la subida sin realizar cambios en el codigo (solo para probar el funcionamiento de la subida)

        
        
        
def abrir_interfaz():
    root = tk.Tk()
    root.configure(bg="#f0f4f8")
    root.title("Simulación de Trayectoria de la Bomba")

    # Configurar el tamaño de la ventana
    root.geometry("600x650")
    root.resizable(False, False)

    # Estilo
    style = ttk.Style()
    style.theme_use("default") 
    style.configure("Blue.TLabel", background="#f0f4f8", foreground="#003366", font=("Arial", 10))
    style.configure("Blue.TButton", background="#003366", foreground="white", font=("Arial", 10, "bold"))
    style.map("Blue.TButton", background=[("active", "#00509e")])  # Color al hacer clic
    style.configure("Blue.TFrame", background="#f0f4f8")

    # Título
    titulo = tk.Label(
        root,
        text="Simulación de la trayectoria de la bomba",
        font=("Arial", 16, "bold"),
        bg="#f0f4f8",
        fg="#003366"
    )
    titulo.pack(pady=6)

    # Cargar la imagen
    try:
        img = Image.open("imagen.png")
        img = img.resize((600, 300))  # Redimensionar la imagen si es necesario
        img_tk = ImageTk.PhotoImage(img)

        # Mostrar la imagen en la interfaz
        img_label = tk.Label(root, image=img_tk, bg="#f0f4f8")
        img_label.image = img_tk  # Mantener referencia para evitar recolección de basura
        img_label.pack(pady=(5, 5))
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

    texto_datos = tk.Label(
        root,
        text="Por favor, ingrese los datos requeridos:",
        font=("Arial", 14, "bold"),
        bg="#f0f4f8",
        fg="#003366"
    )
    texto_datos.pack(pady=(5, 10))

    # Variables
    velocidad = tk.StringVar()
    altura_avion = tk.StringVar()
    altura_canon = tk.StringVar()
    angulo = tk.StringVar()
    distancia = tk.StringVar()
    longitud = tk.StringVar()

    # Frame para entradas
    frame = ttk.Frame(root, style="Blue.TFrame")
    frame.pack(pady=3)

    # Etiquetas y campos de entrada
    entradas = [
        ("Velocidad del avión (m/s):", velocidad),
        ("Altura del avión (m):", altura_avion),
        ("Altura del cañón (m):", altura_canon),
        ("Ángulo del cañón (°):", angulo),
        ("Distancia al cañón (m):", distancia),
        ("Longitud del cañón (m):", longitud),
    ]

    for i, (etiqueta, variable) in enumerate(entradas):
        ttk.Label(frame, text=etiqueta, style="Blue.TLabel").grid(
            row=i, column=0, padx=5, pady=3, sticky="w"
        )
        tk.Entry(frame, textvariable=variable, bg="white", fg="#003366", insertbackground="#003366").grid(
            row=i, column=1, padx=5, pady=3
        )

    # Función para procesar los datos
    def procesar_datos():
        try:
            v = float(velocidad.get())
            ha = float(altura_avion.get())
            hc = float(altura_canon.get())
            alpha = float(angulo.get())
            d = float(distancia.get())
            L = float(longitud.get())

            # if v <= 0 or ha <= 0 or hc <= 0 or L <= 0 or d < 0:
            #     raise ValueError("Todos los valores deben ser positivos.")
              
            #Validaciones
            if v <= 0:
                    raise ValueError("La velocidad debe ser mayor que 0.")
            if ha <= 0:
                    raise ValueError("La altura del avión debe ser mayor que 0.")
            if hc <= 0:
                    raise ValueError("La altura del cañón debe ser mayor que 0.")
            if not (0 < alpha < 90):
                    raise ValueError("El ángulo debe estar entre 0° y 90°.")
            if d < 0:
                    raise ValueError("La distancia al cañón no puede ser negativa.") #Dado que se supone que va en una direccion, y eso no se puede alterar
            if L <= 0:
                    raise ValueError("La longitud del cañón debe ser mayor que 0.")

            root.withdraw()
            # Llamar a la siguiente ventana
            mostrar_resultados(v, ha, hc, alpha, d, L)

        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")
    # Botón
    ttk.Button(root, text="Siguiente", command=procesar_datos, style="Blue.TButton").pack(pady=20)

    # Iniciar aplicación
    root.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
# CODIGO ANTIGUO  
# import tkinter as tk
# from tkinter import ttk, messagebox
# from PIL import Image, ImageTk  # Para manejar imágenes
# from gui_output import mostrar_resultados

# def bienvenida():
#     ventana = tk.Tk()
#     ventana.title("Información del Proyecto")
#     ventana.geometry("600x650")  # Tamaño fijo
#     ventana.resizable(False, False)

#     # Estilo de la ventana
#     style = ttk.Style()
#     style.theme_use("default")
#     style.configure("Blue.TLabel", background="#f0f4f8", foreground="#003366", font=("Arial", 14))
#     style.configure("Blue.TButton", background="#003366", foreground="white", font=("Arial", 12, "bold"))
#     style.map("Blue.TButton", background=[("active", "#00509e")])  # Color al hacer clic
#     style.configure("Blue.TFrame", background="#f0f4f8")

#     # Contenedor principal
#     frame = ttk.Frame(ventana, style="Blue.TFrame")
#     frame.pack(fill="both", expand=True, padx=20, pady=20)


#     # Cargar la imagen
#     try:
#         img = Image.open("imagenAvion.jpg")  # Reemplaza "logo.png" con la ruta de tu imagen
#         img = img.resize((150, 150))  # Redimensionar si es necesario
#         img_tk = ImageTk.PhotoImage(img)

#         # Mostrar la imagen en un Label
#         img_label = tk.Label(frame, image=img_tk, bg="#f0f4f8")
#         img_label.image = img_tk  # Mantener referencia para evitar que el recolector de basura la elimine
#         img_label.pack(pady=(10, 20))  # Añade espacio entre la imagen y el texto
#     except Exception as e:
#         messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

#     # Información requerida
#     info = "Escuela Politécnica Nacional"
#     integrantes = ["Alexis Bautista", "David Egas", "Aubertin Ochoa", "Erick Romero"]
#     tema = "Simulación de la caída de una bomba"

#     # Etiquetas centradas
#     label_uni = ttk.Label(frame, text=f"Universidad: {info}", style="Blue.TLabel")
#     label_uni.pack(pady=20)

#     for integrante in integrantes:
#         label_integrante = ttk.Label(frame, text=f"Integrante: {integrante}", style="Blue.TLabel")
#         label_integrante.pack(pady=10)

#     label_tema = ttk.Label(frame, text=f"Tema: {tema}", style="Blue.TLabel", wraplength=500, justify="center")
#     label_tema.pack(pady=20)

#     # Botón al final
#     btn_ingreso = ttk.Button(frame, text="Ir a ingreso de datos", style="Blue.TButton",command=lambda: [ventana.destroy(), abrir_interfaz()])
#     btn_ingreso.pack(pady=20)

#     ventana.mainloop()
        
# def abrir_interfaz():
#     root = tk.Tk()
#     root.configure(bg="#f0f4f8")
#     root.title("Simulación de Trayectoria de la Bomba")

#     # Configurar el tamaño de la ventana
#     root.geometry("600x650")
#     root.resizable(False, False)

#     # Estilo
#     style = ttk.Style()
#     style.theme_use("default") 
#     style.configure("Blue.TLabel", background="#f0f4f8", foreground="#003366", font=("Arial", 10))
#     style.configure("Blue.TButton", background="#003366", foreground="white", font=("Arial", 10, "bold"))
#     style.map("Blue.TButton", background=[("active", "#00509e")])  # Color al hacer clic
#     style.configure("Blue.TFrame", background="#f0f4f8")

#     # Título
#     titulo = tk.Label(
#         root,
#         text="Simulación de la trayectoria de la bomba",
#         font=("Arial", 16, "bold"),
#         bg="#f0f4f8",
#         fg="#003366"
#     )
#     titulo.pack(pady=6)

#     # Cargar la imagen
#     try:
#         img = Image.open("imagen.png")
#         img = img.resize((600, 300))  # Redimensionar la imagen si es necesario
#         img_tk = ImageTk.PhotoImage(img)

#         # Mostrar la imagen en la interfaz
#         img_label = tk.Label(root, image=img_tk, bg="#f0f4f8")
#         img_label.image = img_tk  # Mantener referencia para evitar recolección de basura
#         img_label.pack(pady=(5, 5))
#     except Exception as e:
#         messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

#     texto_datos = tk.Label(
#         root,
#         text="Por favor, ingrese los datos requeridos:",
#         font=("Arial", 14, "bold"),
#         bg="#f0f4f8",
#         fg="#003366"
#     )
#     texto_datos.pack(pady=(5, 10))

#     # Variables
#     velocidad = tk.StringVar()
#     altura_avion = tk.StringVar()
#     altura_canon = tk.StringVar()
#     angulo = tk.StringVar()
#     distancia = tk.StringVar()
#     longitud = tk.StringVar()

#     # Frame para entradas
#     frame = ttk.Frame(root, style="Blue.TFrame")
#     frame.pack(pady=3)

#     # Etiquetas y campos de entrada
#     entradas = [
#         ("Velocidad del avión (m/s):", velocidad),
#         ("Altura del avión (m):", altura_avion),
#         ("Altura del cañón (m):", altura_canon),
#         ("Ángulo del cañón (°):", angulo),
#         ("Distancia al cañón (m):", distancia),
#         ("Longitud del cañón (m):", longitud),
#     ]

#     for i, (etiqueta, variable) in enumerate(entradas):
#         ttk.Label(frame, text=etiqueta, style="Blue.TLabel").grid(
#             row=i, column=0, padx=5, pady=3, sticky="w"
#         )
#         tk.Entry(frame, textvariable=variable, bg="white", fg="#003366", insertbackground="#003366").grid(
#             row=i, column=1, padx=5, pady=3
#         )

#     # Función para procesar los datos
#     def procesar_datos():
#         try:
#             v = float(velocidad.get())
#             ha = float(altura_avion.get())
#             hc = float(altura_canon.get())
#             alpha = float(angulo.get())
#             d = float(distancia.get())
#             L = float(longitud.get())

#             # if v <= 0 or ha <= 0 or hc <= 0 or L <= 0 or d < 0:
#             #     raise ValueError("Todos los valores deben ser positivos.")
              
#             #Validaciones
#             if v <= 0:
#                     raise ValueError("La velocidad debe ser mayor que 0.")
#             if ha <= 0:
#                     raise ValueError("La altura del avión debe ser mayor que 0.")
#             if hc <= 0:
#                     raise ValueError("La altura del cañón debe ser mayor que 0.")
#             if not (0 < alpha < 90):
#                     raise ValueError("El ángulo debe estar entre 0° y 90°.")
#             if d < 0:
#                     raise ValueError("La distancia al cañón no puede ser negativa.") #Dado que se supone que va en una direccion, y eso no se puede alterar
#             if L <= 0:
#                     raise ValueError("La longitud del cañón debe ser mayor que 0.")

#             root.withdraw()
#             # Llamar a la siguiente ventana
#             mostrar_resultados(v, ha, hc, alpha, d, L)

#         except ValueError as e:
#             messagebox.showerror("Error", f"Entrada inválida: {e}")
#     # Botón
#     ttk.Button(root, text="Siguiente", command=procesar_datos, style="Blue.TButton").pack(pady=20)

#     # Iniciar aplicación
#     root.mainloop()