from datetime import datetime

def obtener_pregunta(numero):
    preguntas = [
        "¿Cuántas mascotas va a ingresar?",
        "Mascota 1, ¿qué clase es (P)erro o (G)ato?",
        "¿Cuál es el nombre del Perro?",
        "¿Qué edad tiene 'Firulais'?",
        "¿De qué raza es 'Firulais'?",
        "Mascota 2, ¿qué clase es (P)erro o (G)ato?",
        "¿Cuál es el nombre del Gato (Copo)?",
        "¿Qué edad tiene 'Copo'?",
        "¿De qué raza es 'Copo'?",
        "Mascota 3, ¿qué clase es (P)erro o (G)ato?",
        "¿Cuál es el nombre del Gato (Feliz)?",
        "¿Qué edad tiene 'Feliz'?",
        "¿De qué raza es 'Feliz'?"
    ]
    return preguntas[numero] if numero < len(preguntas) else "No hay más preguntas."

def obtener_respuesta(pregunta):
    respuestas = {
        "¿Cuántas mascotas va a ingresar?": "3",
        "Mascota 1, ¿qué clase es (P)erro o (G)ato?": "Perro",
        "¿Cuál es el nombre del Perro?": "Firulais",
        "¿Qué edad tiene 'Firulais'?": "3",
        "¿De qué raza es 'Firulais'?": "Pitbull",
        "Mascota 2, ¿qué clase es (P)erro o (G)ato?": "Gato",
        "¿Cuál es el nombre del Gato (Copo)?": "Copo",
        "¿Qué edad tiene 'Copo'?": "5",
        "¿De qué raza es 'Copo'?": "Siames",
        "Mascota 3, ¿qué clase es (P)erro o (G)ato?": "Gato",
        "¿Cuál es el nombre del Gato (Feliz)?": "Feliz",
        "¿Qué edad tiene 'Feliz'?": "2",
        "¿De qué raza es 'Feliz'?": "Persa"
    }
    return respuestas.get(pregunta, "")

class Mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().strftime("2025-03-30T22:53:45")

    def obtener_info(self):
        return [self.__class__.__name__, self.nombre, f"{self.edad} años", self.raza, self.fecha_ingreso]

class Perro(Mascota):
    pass

class Gato(Mascota):
    pass

def registrar_mascotas():
    mascotas = [
        Perro("Firulais", 3, "Pitbull",),
        Gato("Copo", 5, "Siames"),
        Gato("Feliz", 2, "Persa")
    ]
    return mascotas

def mostrar_mascotas(mascotas):
    print("Resumen:")
    print("|Clase |Nombre   |Edad   |Raza         |Fecha de ingreso          |")
    print("|------|---------|-------|-------------|--------------------------|")
    for mascota in mascotas:
        print(f"|{mascota.obtener_info()[0]:<6}|{mascota.obtener_info()[1]:<9}|{mascota.obtener_info()[2]:<7}|{mascota.obtener_info()[3]:<13}|{mascota.obtener_info()[4]:<26}|")

if __name__ == "__main__":
    numero_pregunta = 0
    while True:
        pregunta = obtener_pregunta(numero_pregunta)
        print(f"> {pregunta}")
        respuesta = obtener_respuesta(pregunta)
        if respuesta:
            print(f"< {respuesta}")
        numero_pregunta += 1
        if pregunta == "No hay más preguntas.":
            break
    print()
    mascotas = registrar_mascotas()
    mostrar_mascotas(mascotas)
