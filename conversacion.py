def iniciar_conversacion(tutor):
	print("Tutor de Python - escribe 'salir' para terminar\n")
	while True:
		mensaje = input("Tu: ")
		respuesta = tutor.responder(mensaje)
		print(f"Tutor: {respuesta}\n")
		if "adios" in mensaje.lower() or "salir" in mensaje.lower():
			break

	print("--- Historial de la conversacion ---")
	tutor.mostrar_historial()