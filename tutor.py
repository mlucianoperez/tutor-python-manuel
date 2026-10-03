class TutorPython:
    def __init__(self):
        self.historial = []
        self.temas = {
            "variable": {
                "explicacion": "Una variable es un nombre que apunta a un valor guardado en memoria.",
                "pregunta": "¿Qué elemento permite guardar o referenciar un valor en Python?",
                "respuesta": "variable",
                "tipo": "texto",
            },
            "lista": {
                "explicacion": "Una lista es una coleccion ordenada de elementos, escrita entre corchetes.",
                "pregunta": "¿En qué posición se encuentra el primer elemento de una lista?",
                "respuesta": "0",
                "tipo": "numero",
            },
        }
        self.temas_dominados = {}

    def explicar_concepto(self, mensaje_normalizado):
        for tema, contenido in self.temas.items():
            if tema in mensaje_normalizado:
                return contenido["explicacion"]

        temas_disponibles = ", ".join(self.temas.keys())
        return f"Ese tema no está disponible. Puedo explicar: {temas_disponibles}."

    def hacer_pregunta(self, mensaje_normalizado):
        for tema, contenido in self.temas.items():
            if tema in mensaje_normalizado:
                respuesta_estudiante = input(contenido["pregunta"] + " ")

                if contenido["tipo"] == "numero":
                    try:
                        respuesta_numero = int(respuesta_estudiante)
                    except ValueError:
                        return "Necesito que respondas con un número. Intenta de nuevo más tarde."

                    correcta = respuesta_numero == int(contenido["respuesta"])
                else:
                    correcta = (
                        respuesta_estudiante.strip().lower()
                        == contenido["respuesta"].strip().lower()
                    )

                self.temas_dominados[tema] = correcta

                if correcta:
                    return "¡Respuesta correcta!"

                return "Respuesta incorrecta."

        temas_disponibles = ", ".join(self.temas.keys())
        return f"No encontré ese tema. Puedo hacer preguntas sobre: {temas_disponibles}."

    def mostrar_progreso(self):
        preguntas_intentadas = len(self.temas_dominados)

        if preguntas_intentadas == 0:
            return "Todavía no has intentado ninguna pregunta."

        respuestas_correctas = sum(self.temas_dominados.values())

        return (
            f"Has respondido correctamente {respuestas_correctas} de "
            f"{preguntas_intentadas} preguntas intentadas."
        )

    def responder(self, mensaje):
        self.historial.append(("estudiante", mensaje))
        mensaje_normalizado = mensaje.lower()

        if "adios" in mensaje_normalizado or "salir" in mensaje_normalizado:
            respuesta = "Hasta luego! Sigue practicando."

        elif "hola" in mensaje_normalizado or "buenas" in mensaje_normalizado:
            respuesta = "Hola! Soy tu tutor de Python."

        elif "explica" in mensaje_normalizado or "explicame" in mensaje_normalizado:
            respuesta = self.explicar_concepto(mensaje_normalizado)

        elif "pregunta" in mensaje_normalizado or "quiz" in mensaje_normalizado:
            respuesta = self.hacer_pregunta(mensaje_normalizado)

        elif "progreso" in mensaje_normalizado:
            respuesta = self.mostrar_progreso()

        else:
            respuesta = "Todavia no se responder eso."

        self.historial.append(("tutor", respuesta))
        return respuesta

    def mostrar_historial(self):
        for quien, texto in self.historial:
            print(f"{quien}: {texto}")


if __name__ == "__main__":
    tutor_prueba = TutorPython()
    print("Corriendo tutor.py directamente - autoprueba:")
    print(tutor_prueba.responder("hola"))