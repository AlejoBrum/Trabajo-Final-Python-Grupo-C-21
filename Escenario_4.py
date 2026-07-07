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

    while intentos_restantes > 0:
        dni = input("Ingrese su DNI (Usuario): ").strip()
        pin = input("Ingrese su clave PIN de 4 dígitos: ").strip()

        if dni in usuarios and usuarios[dni]["pin"] == pin:
            usuario_autenticado = dni
            print(f"\n¡Ingreso exitoso! Bienvenido/a {usuarios[dni]['nombre']}.")
            return True
        else:
            intentos_restantes -= 1
            print(f"[ERROR] Usuario o PIN incorrectos.")
            print(f"Intentos restantes: {intentos_restantes}\n")

    print("\n[ALERTA] Tarjeta retenida por seguridad. Comuniqúese con el banco.")
    return False
    
