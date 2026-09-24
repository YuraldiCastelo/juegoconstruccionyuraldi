import random

def jugar():
    print("========================================")
    print("   ¡PIEDRA, PAPEL O TIJERA!            ")
    print("========================================")
    
    opciones = ["piedra", "papel", "tijera"]
    
    while True:
        usuario = input("\nElige (piedra, papel, tijera) o 'salir': ").lower()
        
        if usuario == "salir":
            print("¡Gracias por jugar! Hasta luego.")
            break
            
        if usuario not in opciones:
            print("❌ Opción no válida. Intenta de nuevo.")
            continue
            
        computadora = random.choice(opciones)
        print(f"🤖 La computadora eligió: {computadora}")
        
        if usuario == computadora:
            print("🤝 ¡Empate!")
        elif (usuario == "piedra" and computadora == "tijera") or \
             (usuario == "papel" and computadora == "piedra") or \
             (usuario == "tijera" and computadora == "papel"):
            print("🎉 ¡Ganaste esta ronda!")
        else:
            print("💻 ¡Gana la computadora!")

if __name__ == "__main__":
    jugar()

    