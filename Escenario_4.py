# Trabajo final: Simulador de cajero automático

usuarios = {
    "20444555": {
        "pin": "1234",
        "nombre": "Alejo Brum",
        "saldo": 45000.0,
        "limite_extraccion": 20000.0
    },
    "30111222": {
        "pin": "4321",
        "nombre": "Juan Pérez",
        "saldo": 120000.0,
        "limite_extraccion": 50000.0
    }
}

usuario_autenticado = None  
intentos_restantes = 3
# Sección de autenticación

def iniciar_sesion():
    global usuario_autenticado, intentos_restantes

    print("\n--- BIENVENIDO AL BANCO DIGITAL ---")

    # Un bucle 'while' (Mientras) que se repite mientras queden intentos
    while intentos_restantes > 0:
        dni = input("Ingrese su DNI (Usuario): ").strip()
        pin = input("Ingrese su clave PIN de 4 dígitos: ").strip()

        # Verificamos si el DNI existe en el diccionario y si el PIN coincide
        if dni in usuarios and usuarios[dni]["pin"] == pin:
            usuario_autenticado = dni
            print(f"\n¡Ingreso exitoso! Bienvenido/a {usuarios[dni]['nombre']}.")
            return True  # Corta la función y devuelve "Verdadero" (logueado)
        else:
            intentos_restantes -= 1
            print(f"[ERROR] Usuario o PIN incorrectos.")
            print(f"Intentos restantes: {intentos_restantes}\n")

    # Si el bucle termina y llega acá, es porque se quedó sin intentos
    print("\n[ALERTA] Tarjeta retenida por seguridad. Comuniqúese con el banco.")
    return False
 # Menú principal del sistema
def menu_principal():
    """Muestra el menú de operaciones y gestiona la selección del usuario."""
    
    opciones_validas = {"1", "2", "3", "4", "5"}
    
    # El bucle mantiene al usuario dentro del menú hasta que decida salir
    while True:
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Consultar Saldo")
        print("2. Extracción de Efectivo")
        print("3. Depósito")
        print("4. Transferencia")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion not in opciones_validas:
            print("\n[ERROR] Opción no válida. Intente nuevamente.")
            continue

        if opcion == "1":
            pass  # Temporal: Aca va la consulta de saldo
        elif opcion == "2":
            pass  # Temporal: Aca va la extracción
        elif opcion == "3":
            pass  # Temporal: Aca va el depósito
        elif opcion == "4":
            pass  # Temporal: Aca va la transferencia
        elif opcion == "5":
            print("\nGracias por utilizar nuestros servicios. ¡Hasta luego!")
            break  # Rompe el bucle y cierra el menú   
