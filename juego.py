import random

def jugar():
    print("========================================")
    print("   ¡BIENVENIDO A ADIVINA EL NÚMERO!    ")
    print("========================================")
    print("Estoy pensando en un número entre 1 y 100.")
    
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    while not adivinado:
        try:
            intento = int(input("\nIntroduce tu número: "))
            intentos += 1

            if intento < numero_secreto:
                print("↓ El número secreto es MAYOR.")
            elif intento > numero_secreto:
                print("↑ El número secreto es MENOR.")
            else:
                adivinado = True
                print(f"\n🎉 ¡FELICIDADES! Adivinaste el número en {intentos} intentos.")
        except ValueError:
            print("❌ Por favor, ingresa solo números enteros.")

if __name__ == "__main__":
    jugar()

    