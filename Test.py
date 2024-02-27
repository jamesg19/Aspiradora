import threading
import time

# Función que representa el segundo hilo
def hilo2(nombre_evento, continuar_evento):
    while True:
        nombre_evento.wait()  # Espera a que se reciba el nombre
        nombre = nombre_evento.nombre
        print(f"Hilo 2: Hola, {nombre}!")
        continuar_evento.set()  # Indica al hilo 1 que puede continuar preguntando
        nombre_evento.clear()  # Resetea el evento de nombre para futuras iteraciones

# Función que representa el primer hilo
def hilo1(nombre_evento, continuar_evento):
    print("Hilo 1: Empezando...")
    while True:
        continuar_evento.clear()  # Indica al hilo 2 que debe detenerse
        nombre = input("Hilo 1: ¿Cómo te llamas? ('salir' para terminar): ")
        if nombre.lower() == "salir":
            break
        nombre_evento.nombre = nombre
        nombre_evento.set()  # Establece el nombre para que el hilo 2 lo procese
        continuar_evento.wait()  # Espera a que el hilo 2 pueda continuar

# Crear instancias de Event para sincronización
nombre_evento = threading.Event()
continuar_evento = threading.Event()

# Crear instancias de los hilos
hilo_1 = threading.Thread(target=hilo1, args=(nombre_evento, continuar_evento))
hilo_2 = threading.Thread(target=hilo2, args=(nombre_evento, continuar_evento))

# Iniciar los hilos
hilo_2.start()
hilo_1.start()

# Esperar a que ambos hilos terminen
hilo_2.join()
hilo_1.join()

print("Programa finalizado.")
