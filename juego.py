import tkinter as tk
from tkinter import messagebox
import random

class JuegoAhorcado:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Juego del Ahorcado")
        self.ventana.geometry("600x500")
        self.ventana.configure(bg="#2c3e50")
        
        self.palabras = ["python", "programacion", "ahorcado", "computadora", "interfaz", 
                        "juego", "desarrollo", "codigo", "ventana", "boton"]
        self.palabra_secreta = random.choice(self.palabras).upper()
        self.letras_adivinadas = set()
        self.intentos_restantes = 6
        self.letras_incorrectas = set()
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Título
        titulo = tk.Label(self.ventana, text="🎮 JUEGO DEL AHORCADO 🎮", 
                         font=("Arial", 20, "bold"), bg="#2c3e50", fg="#ecf0f1")
        titulo.pack(pady=10)
        
        # Frame para mostrar la palabra
        frame_palabra = tk.Frame(self.ventana, bg="#2c3e50")
        frame_palabra.pack(pady=10)
        
        tk.Label(frame_palabra, text="Palabra:", font=("Arial", 12, "bold"), 
                bg="#2c3e50", fg="#ecf0f1").pack(side=tk.LEFT, padx=5)
        
        self.label_palabra = tk.Label(frame_palabra, text=self.obtener_palabra_visible(), 
                                     font=("Arial", 16, "bold"), bg="#3498db", fg="white", 
                                     padx=10, pady=5)
        self.label_palabra.pack(side=tk.LEFT, padx=5)
        
        # Frame para intentos y letras incorrectas
        frame_info = tk.Frame(self.ventana, bg="#2c3e50")
        frame_info.pack(pady=10)
        
        self.label_intentos = tk.Label(frame_info, text=f"Intentos: {self.intentos_restantes}", 
                                       font=("Arial", 11, "bold"), bg="#e74c3c", fg="white", padx=10, pady=5)
        self.label_intentos.pack(side=tk.LEFT, padx=10)
        
        self.label_incorrectas = tk.Label(frame_info, text="Incorrectas: ", 
                                         font=("Arial", 11, "bold"), bg="#95a5a6", fg="white", padx=10, pady=5)
        self.label_incorrectas.pack(side=tk.LEFT, padx=10)
        
        # Frame para entrada
        frame_entrada = tk.Frame(self.ventana, bg="#2c3e50")
        frame_entrada.pack(pady=10)
        
        tk.Label(frame_entrada, text="Ingresa una letra:", font=("Arial", 11, "bold"), 
                bg="#2c3e50", fg="#ecf0f1").pack(side=tk.LEFT, padx=5)
        
        self.entrada_letra = tk.Entry(frame_entrada, font=("Arial", 12), width=3, 
                                      justify=tk.CENTER)
        self.entrada_letra.pack(side=tk.LEFT, padx=5)
        self.entrada_letra.bind("<Return>", lambda e: self.adivinar())
        
        # Frame para botones
        frame_botones = tk.Frame(self.ventana, bg="#2c3e50")
        frame_botones.pack(pady=10)
        
        btn_adivinar = tk.Button(frame_botones, text="Adivinar", command=self.adivinar, 
                                font=("Arial", 11, "bold"), bg="#27ae60", fg="white", padx=15, pady=5)
        btn_adivinar.pack(side=tk.LEFT, padx=5)
        
        btn_nuevo = tk.Button(frame_botones, text="Nuevo Juego", command=self.nuevo_juego, 
                             font=("Arial", 11, "bold"), bg="#3498db", fg="white", padx=15, pady=5)
        btn_nuevo.pack(side=tk.LEFT, padx=5)
        
        btn_salir = tk.Button(frame_botones, text="Salir", command=self.ventana.quit, 
                             font=("Arial", 11, "bold"), bg="#c0392b", fg="white", padx=15, pady=5)
        btn_salir.pack(side=tk.LEFT, padx=5)
        
        # Area de dibujo del ahorcado
        self.canvas = tk.Canvas(self.ventana, width=200, height=250, bg="#34495e")
        self.canvas.pack(pady=10)
        
        self.label_estado = tk.Label(self.ventana, text="", font=("Arial", 12, "bold"), 
                                    bg="#2c3e50", fg="#ecf0f1")
        self.label_estado.pack(pady=5)
        
        self.dibujar_ahorcado()
        
    def obtener_palabra_visible(self):
        return " ".join([letra if letra in self.letras_adivinadas else "_" 
                        for letra in self.palabra_secreta])
    
    def adivinar(self):
        letra = self.entrada_letra.get().upper()
        self.entrada_letra.delete(0, tk.END)
        
        if not letra or len(letra) != 1 or not letra.isalpha():
            messagebox.showwarning("Error", "Ingresa una única letra válida")
            return
        
        if letra in self.letras_adivinadas or letra in self.letras_incorrectas:
            messagebox.showinfo("Información", f"Ya ingresaste la letra {letra}")
            return
        
        self.letras_adivinadas.add(letra)
        
        if letra not in self.palabra_secreta:
            self.letras_incorrectas.add(letra)
            self.intentos_restantes -= 1
        
        self.actualizar_interfaz()
        self.verificar_estado()
        
    def actualizar_interfaz(self):
        self.label_palabra.config(text=self.obtener_palabra_visible())
        self.label_intentos.config(text=f"Intentos: {self.intentos_restantes}")
        self.label_incorrectas.config(text=f"Incorrectas: {', '.join(sorted(self.letras_incorrectas))}")
        self.dibujar_ahorcado()
        
    def dibujar_ahorcado(self):
        self.canvas.delete("all")
        
        # Poste
        self.canvas.create_line(10, 240, 10, 10, width=3, fill="black")
        self.canvas.create_line(10, 10, 100, 10, width=3, fill="black")
        self.canvas.create_line(100, 10, 100, 40, width=2, fill="black")
        
        errores = 6 - self.intentos_restantes
        
        if errores >= 1:  # Cabeza
            self.canvas.create_oval(85, 40, 115, 70, outline="black", width=2, fill="#f39c12")
        if errores >= 2:  # Cuerpo
            self.canvas.create_line(100, 70, 100, 130, width=2, fill="black")
        if errores >= 3:  # Brazo izquierdo
            self.canvas.create_line(100, 90, 70, 110, width=2, fill="black")
        if errores >= 4:  # Brazo derecho
            self.canvas.create_line(100, 90, 130, 110, width=2, fill="black")
        if errores >= 5:  # Pierna izquierda
            self.canvas.create_line(100, 130, 70, 170, width=2, fill="black")
        if errores >= 6:  # Pierna derecha
            self.canvas.create_line(100, 130, 130, 170, width=2, fill="black")
    
    def verificar_estado(self):
        palabra_visible = self.obtener_palabra_visible()
        palabra_sin_espacios = palabra_visible.replace(" ", "")
        
        if palabra_sin_espacios == self.palabra_secreta:
            self.label_estado.config(text="¡¡¡ GANASTE !!!", fg="#27ae60")
            messagebox.showinfo("¡Ganaste!", f"La palabra era: {self.palabra_secreta}")
            self.nuevo_juego()
        elif self.intentos_restantes == 0:
            self.label_estado.config(text="GAME OVER", fg="#c0392b")
            messagebox.showinfo("Perdiste", f"La palabra era: {self.palabra_secreta}")
            self.nuevo_juego()
    
    def nuevo_juego(self):
        self.palabra_secreta = random.choice(self.palabras).upper()
        self.letras_adivinadas = set()
        self.intentos_restantes = 6
        self.letras_incorrectas = set()
        self.label_estado.config(text="")
        self.actualizar_interfaz()
        self.entrada_letra.focus()

# Crear ventana principal
ventana = tk.Tk()
juego = JuegoAhorcado(ventana)
ventana.mainloop()
