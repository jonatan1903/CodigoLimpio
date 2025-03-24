
from model.juego import ComienzaElJuego
from model.sistemaUsuario import SistemaJugador
from model.puntuaciones import Puntuaciones


def main():
    sistema = SistemaJugador()
    sistema.puntuaciones = Puntuaciones()  # Asegurar que puntuaciones esté inicializado
    
    print("=== BIENVENIDO A BATALLA NAVAL ===")
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Probar juego sin registro")
        print("4. Mostrar puntuaciones")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese un nombre de usuario: ")
            contraseña = input("Ingrese una contraseña: ")
            sistema.registrar_jugador(nombre, contraseña)
        
        elif opcion == "2":
            nombre = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            jugador = sistema.iniciar_sesion(nombre, contraseña)
            if jugador:
                jugar(jugador, sistema)
        
        elif opcion == "3":
            jugar_sin_registro()
        
        elif opcion == "4":
            print("\nTABLA DE PUNTUACIONES:")
            sistema.puntuaciones.mostrar_puntuaciones()
        
        elif opcion == "5":
            print("¡Gracias por jugar!")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")

def jugar(jugador, sistema):
    print(f"Bienvenido, {jugador.nombre_usuario}.")
    iniciar_juego(sistema, jugador.nombre_usuario)

def jugar_sin_registro():
    print("Iniciando juego de prueba sin registro...")
    iniciar_juego()

def iniciar_juego(sistema=None, nombre_usuario=None):
    ancho = int(input("Ingrese el ancho del tablero: "))
    alto = int(input("Ingrese el alto del tablero: "))
    num_naves = int(input("Ingrese el número de naves: "))
    
    juego = ComienzaElJuego(alto, ancho, num_naves)
    juego.campo.MostrarCampo()
    
    while not juego.verificar_ganador():
        try:
            x = int(input("Ingrese la fila del disparo: "))
            y = int(input("Ingrese la columna del disparo: "))
            juego.realizar_disparo(x, y)
            juego.campo.MostrarCampo()  # ACTUALIZAR EL MAPA DESPUÉS DE CADA DISPARO
        except ValueError:
            print("Entrada inválida, ingrese números enteros.")
    
    print("¡Felicidades! Has ganado la partida.")
    
    if sistema and nombre_usuario:
        sistema.actualizar_puntaje(nombre_usuario, 10)
        print("Tu puntaje ha sido actualizado.")
    
    opcion = input("¿Quieres jugar otra partida? (s/n): ")
    if opcion.lower() == "s":
        iniciar_juego(sistema, nombre_usuario)
    else:
        print("Regresando al menú principal...")

if __name__ == "__main__":
    main()