# Trabajo final: Simulador de cajero automático

# Simulación de base de datos de usuarios

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

usuario_autenticado = None  # Almacena el DNI del usuario que inició sesión
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
    # El bucle mantiene al usuario dentro del menú hasta que decida salir
    while True:
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Consultar Saldo")
        print("2. Extracción de Efectivo")
        print("3. Depósito")
        print("4. Transferencia")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            pass # Temporal: Aca va la consulta de saldo
        elif opcion == "2":
            extraer_dinero() # <-- Cambiamos el pass por la función real
        elif opcion == "3":
            depositar_dinero() # <-- Cambiamos el pass por la función real
        elif opcion == "4":
            pass # Temporal: Aca va la transferencia
        elif opcion == "5":
            print("\nGracias por utilizar nuestros servicios. ¡Hasta luego!")
            break  # Rompe el bucle y cierra el menú
        else:
            print("\n[ERROR] Opción no válida. Intente nuevamente.")

# función para extraer dinero

def extraer_dinero():
    datos_usuario = usuarios[usuario_autenticado]
    print("\n--- EXTRACCIÓN DE EFECTIVO ---")
    print(f"Su límite de extracción diaria es: ${datos_usuario['limite_extraccion']}")
    
    # Validamos que lo ingresado sea un número
    entrada = input("Ingrese el monto a extraer: ").strip()
    if not entrada.isdigit():
        print("\n[ERROR] Debe ingresar un monto numérico válido.")
        return

    monto = float(entrada)
    
    # CONTROLES REQUERIDOS POR EL ESCENARIO
    if monto <= 0:
        print("\n[ERROR] El monto debe ser mayor a cero.")
    elif monto > datos_usuario["saldo"]:
        print("\n[ERROR] Saldo insuficiente.")
    elif monto > datos_usuario["limite_extraccion"]:
        print("\n[ERROR] La operación supera su límite de extracción diaria.")
    else:
        # Si pasa los controles, descontamos el dinero
        datos_usuario["saldo"] -= monto
        print(f"\n¡Extracción exitosa! Retire su dinero.")
        print(f"Saldo restante: ${datos_usuario['saldo']}")

# Función para depositar dinero

def depositar_dinero():
    datos_usuario = usuarios[usuario_autenticado]
    print("\n--- DEPÓSITO DE EFECTIVO ---")
    
    entrada = input("Ingrese el monto a depositar: ").strip()
    if not entrada.isdigit():
        print("\n[ERROR] Debe ingresar un monto numérico válido.")
        return

    monto = float(entrada)
    
    # Validamos que no metan un monto negativo o cero
    if monto <= 0:
        print("\n[ERROR] El monto a depositar debe ser mayor a cero.")
    else:
        # Sumamos la plata al saldo del usuario
        datos_usuario["saldo"] += monto
        print(f"\n¡Depósito exitoso! Se han acreditado ${monto} en su cuenta.")
        print(f"Nuevo saldo disponible: ${datos_usuario['saldo']}")