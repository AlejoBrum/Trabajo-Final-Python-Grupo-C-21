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