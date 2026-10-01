class TutorPython:
	def __init__(self):
		self.historial = []
		self.temas = {
			"variable": {
				"explicacion": "Una variable es un nombre que apunta a un valor guardado en memoria."
			},
			"lista": {
				"explicacion": "Una lista es una coleccion ordenada de elementos, escrita entre corchetes."
			},
		}

	def explicar_concepto(self, mensaje_normalizado):
		for tema, contenido in self.temas.items():
			if tema in mensaje_normalizado:
				return contenido["explicacion"]

		temas_disponibles = ", ".join(self.temas.keys())
		return f"Ese tema no está disponible. Puedo explicar: {temas_disponibles}."

	def responder(self, mensaje):
		self.historial.append(("estudiante", mensaje))
		mensaje_normalizado = mensaje.lower()
		if "adios" in mensaje_normalizado or "salir" in mensaje_normalizado:
			respuesta = "Hasta luego! Sigue practicando."
		elif "hola" in mensaje_normalizado or "buenas" in mensaje_normalizado:
			respuesta = "Hola! Soy tu tutor de Python."
		elif "explica" in mensaje_normalizado or "explicame" in mensaje_normalizado:
			respuesta = self.explicar_concepto(mensaje_normalizado)
		else:
			respuesta = "Todavia no se responder eso."
		self.historial.append(("tutor", respuesta))
		return respuesta

tutor = TutorPython()

print(tutor.responder("explicame variable"))
print(tutor.responder("explicame algo que no existe"))