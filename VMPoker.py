class TexasHoldemVM:
    def __init__(self):
        self.stacks = [1000] * 6  # 6 jugadores con 1000 fichas iniciales.
        self.pila_apuestas = []  # Pila de apuestas que almacenará las apuestas de los jugadores.
        self.bote = 0  # El bote empieza en 0.
        self.ciega_grande = 20  # Ciega grande inicial (20 fichas).
        self.ciega_pequena = 10  # Ciega pequeña inicial (10 fichas).
        self.turno = 0  # El primer jugador que empieza la ronda.
        self.jugadores = {0: "P1", 1: "P2", 2: "P3", 3: "P4", 4: "P5", 5: "P6"}  # Diccionario para identificar a los jugadores.
        self.ronda = 0  # Ronda actual (0: Preflop, 1: Flop, 2: Turn, 3: River).
        self.ronda_completada = False  # Bandera para saber si la ronda actual ha terminado.

    # Método para establecer la cantidad de fichas de un jugador.
    def set_stack(self, jugador, cantidad):
        self.stacks[jugador] = cantidad
        print(f"Jugador {self.jugadores[jugador]} tiene {cantidad} fichas.")

    # Método para que un jugador haga una apuesta.
    def apostar(self, jugador, cantidad):
        if self.stacks[jugador] >= cantidad:  # Comprobar si el jugador tiene suficientes fichas.
            self.stacks[jugador] -= cantidad  # Restar la apuesta del stack del jugador.
            self.pila_apuestas.append((jugador, cantidad))  # Registrar la apuesta en la pila de apuestas.
            print(f"Jugador {self.jugadores[jugador]} apuesta {cantidad} fichas.")
        else:
            print(f"El jugador {self.jugadores[jugador]} no tiene suficientes fichas para apostar.")

    # Método para hacer check.
    def chequear(self, jugador):
        print(f"Jugador {self.jugadores[jugador]} hace check.")

    # Método para hacer fold (retirarse de la ronda).
    def foldear(self, jugador):
        print(f"Jugador {self.jugadores[jugador]} se retira.")

    # Método para finalizar una ronda y mover las apuestas al bote.
    def finalizar_ronda(self):
        total_apostado = sum(apuesta[1] for apuesta in self.pila_apuestas)  # Sumar todas las apuestas.
        self.bote += total_apostado  # Agregar las apuestas al bote.
        print(f"Fin de la ronda. Total apostado en esta ronda: {total_apostado}. Bote acumulado: {self.bote}.")
        self.pila_apuestas = []  # Vaciar la pila de apuestas para la próxima ronda.
        self.ronda_completada = True  # Marcar la ronda como completada.

    # Método para pasar a la siguiente ronda.
    def siguiente_ronda(self):
        if self.ronda == 3:  # Si es el River, el juego termina.
            print(f"Fin del juego. El bote final es de {self.bote} fichas.")
            return

        # Cambios de ronda.
        if self.ronda == 0:
            print("Pasando del Preflop al Flop.")
        elif self.ronda == 1:
            print("Pasando del Flop al Turn.")
        elif self.ronda == 2:
            print("Pasando del Turn al River.")

        self.ronda += 1  # Avanzar a la siguiente ronda.
        self.ronda_completada = False  # Reiniciar el estado de la ronda.
        self.turno = (self.turno + 1) % 6  # Cambiar el jugador que comienza la nueva ronda.
        print(f"Comienza la ronda {self.ronda}. El primer jugador en hablar es {self.jugadores[self.turno]}.")

    # Método para leer instrucciones de un archivo.
    def leer_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()  # Eliminar espacios en blanco alrededor.
                if linea == "" or linea.startswith("#"):  # Saltar comentarios y líneas vacías.
                    continue
                
                instruccion = linea.split()  # Dividir la línea en una lista de palabras.

                if instruccion[0] == "SET":  # Establecer stacks o ciegas.
                    if instruccion[1].startswith("R"):  # Cambiar el stack de un jugador.
                        jugador = int(instruccion[1][1])  # Obtener el número del jugador.
                        cantidad = int(instruccion[2])
                        self.set_stack(jugador, cantidad)
                    elif instruccion[1] == "SB":  # Cambiar la ciega pequeña.
                        self.ciega_pequena = int(instruccion[2])
                        print(f"La ciega pequeña ahora es de {self.ciega_pequena} fichas.")
                    elif instruccion[1] == "BB":  # Cambiar la ciega grande.
                        self.ciega_grande = int(instruccion[2])
                        print(f"La ciega grande ahora es de {self.ciega_grande} fichas.")

                # Comandos de apuestas y acciones.
                elif instruccion[0] == "BET":
                    jugador = int(instruccion[1][1])  # Obtener el número del jugador.
                    cantidad = int(instruccion[2])
                    self.apostar(jugador, cantidad)

                elif instruccion[0] == "CHECK":
                    jugador = int(instruccion[1][1])
                    self.chequear(jugador)

                elif instruccion[0] == "FOLD":
                    jugador = int(instruccion[1][1])
                    self.foldear(jugador)

                # Finalizar la ronda.
                elif instruccion[0] == "ENDROUND":
                    self.finalizar_ronda()

                # Pasar a la siguiente ronda.
                elif instruccion[0] == "NEXTROUND":
                    if self.ronda_completada:
                        self.siguiente_ronda()
                    else:
                        print("La ronda actual no se ha completado.")
# Ejemplo de uso:
vm = TexasHoldemVM()
vm.leer_archivo("ronda.txt")
