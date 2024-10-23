class TexasHoldemVM:
    def _init_(self):
        # Inicializa los atributos de la clase.
        self.stacks = [1000] * 6  # 6 jugadores con 1000 fichas iniciales.
        self.pila_apuestas = []  # Pila de apuestas.
        self.bote = 0  # El bote comienza en 0.
        self.ciega_grande = 20  # Valor inicial de la ciega grande.
        self.ciega_pequena = 10  # Valor inicial de la ciega pequeña.
        self.turno = 0  # Índice del jugador que tiene el turno.
        self.jugadores = {0: "P1", 1: "P2", 2: "P3", 3: "P4", 4: "P5", 5: "P6"}  # Diccionario de jugadores.
        self.ronda = 0  # Ronda actual (0: Preflop, 1: Flop, 2: Turn, 3: River).
        self.ronda_completada = False  # Indica si la ronda actual ha sido completada.

    def set_stack(self, jugador, cantidad):
        # Establece la cantidad de fichas de un jugador específico.
        self.stacks[jugador] = cantidad
        print(f"Jugador {self.jugadores[jugador]} tiene {cantidad} fichas.")

    def apostar(self, jugador, cantidad):
        # Permite a un jugador realizar una apuesta si tiene suficientes fichas.
        if self.stacks[jugador] >= cantidad:
            self.stacks[jugador] -= cantidad
            self.pila_apuestas.append((jugador, cantidad))
            print(f"Jugador {self.jugadores[jugador]} apuesta {cantidad} fichas.")
        else:
            print(f"El jugador {self.jugadores[jugador]} no tiene suficientes fichas para apostar.")

    def chequear(self, jugador):
        # Permite a un jugador pasar su turno sin apostar.
        print(f"Jugador {self.jugadores[jugador]} hace check.")

    def foldear(self, jugador):
        # Permite a un jugador retirarse de la ronda.
        print(f"Jugador {self.jugadores[jugador]} se retira.")

    def finalizar_ronda(self):
        # Finaliza la ronda actual sumando las apuestas realizadas al bote.
        total_apostado = sum(apuesta[1] for apuesta in self.pila_apuestas)
        self.bote += total_apostado
        print(f"Fin de la ronda. Total apostado en esta ronda: {total_apostado}. Bote acumulado: {self.bote}.")
        self.pila_apuestas = []
        self.ronda_completada = True

    def siguiente_ronda(self):
        # Avanza a la siguiente ronda del juego.
        if self.ronda == 3:  # Si es la ronda River, el juego termina.
            print(f"Fin del juego. El bote final es de {self.bote} fichas.")
            return

        # Mensajes de transición entre rondas.
        if self.ronda == 0:
            print("Pasando del Preflop al Flop.")
        elif self.ronda == 1:
            print("Pasando del Flop al Turn.")
        elif self.ronda == 2:
            print("Pasando del Turn al River.")

        # Avanza a la siguiente ronda.
        self.ronda += 1
        self.ronda_completada = False
        self.turno = (self.turno + 1) % 6  # Cambia el primer jugador en la siguiente ronda.
        print(f"Comienza la ronda {self.ronda}. El primer jugador en hablar es {self.jugadores[self.turno]}.")

    def leer_archivo(self, nombre_archivo):
        # Lee un archivo de texto con instrucciones y ejecuta las acciones correspondientes.
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "" or linea.startswith("#"):
                    continue  # Saltar comentarios y líneas vacías.
                
                instruccion = linea.split()

                # Procesa las instrucciones SET.
                if instruccion[0] == "SET":
                    if instruccion[1].startswith("R"):  # Ajustar stack de un jugador.
                        jugador = int(instruccion[1][1])  # Extraer número del jugador.
                        cantidad = int(instruccion[2])
                        self.set_stack(jugador, cantidad)
                    elif instruccion[1] == "SB":
                        self.ciega_pequena = int(instruccion[2])
                        print(f"La ciega pequeña ahora es de {self.ciega_pequena} fichas.")
                    elif instruccion[1] == "BB":
                        self.ciega_grande = int(instruccion[2])
                        print(f"La ciega grande ahora es de {self.ciega_grande} fichas.")

                # Procesa las instrucciones BET.
                elif instruccion[0] == "BET":
                    jugador = int(instruccion[1][1])  # Extraer número del jugador.
                    cantidad = int(instruccion[2])
                    self.apostar(jugador, cantidad)

                # Procesa las instrucciones CHECK.
                elif instruccion[0] == "CHECK":
                    jugador = int(instruccion[1][1])
                    self.chequear(jugador)

                # Procesa las instrucciones FOLD.
                elif instruccion[0] == "FOLD":
                    jugador = int(instruccion[1][1])
                    self.foldear(jugador)

                # Procesa las instrucciones ENDROUND.
                elif instruccion[0] == "ENDROUND":
                    self.finalizar_ronda()

                # Procesa las instrucciones NEXTROUND.
                elif instruccion[0] == "NEXTROUND":
                    if self.ronda_completada:
                        self.siguiente_ronda()
                    else:
                        print("La ronda actual no se ha completado.")
    def __init__(self):
        self.stacks = [1000] * 6  # 6 jugadores con 1000 fichas iniciales
        self.pila_apuestas = []  # Pila de apuestas
        self.bote = 0  # El bote comienza en 0
        self.ciega_grande = 20
        self.ciega_pequena = 10
        self.turno = 0
        self.jugadores = {0: "P1", 1: "P2", 2: "P3", 3: "P4", 4: "P5", 5: "P6"}
        self.ronda = 0  # Ronda actual (0: Preflop, 1: Flop, 2: Turn, 3: River)
        self.ronda_completada = False

    def set_stack(self, jugador, cantidad):
        self.stacks[jugador] = cantidad
        print(f"Jugador {self.jugadores[jugador]} tiene {cantidad} fichas.")

    def apostar(self, jugador, cantidad):
        if self.stacks[jugador] >= cantidad:
            self.stacks[jugador] -= cantidad
            self.pila_apuestas.append((jugador, cantidad))
            print(f"Jugador {self.jugadores[jugador]} apuesta {cantidad} fichas.")
        else:
            print(f"El jugador {self.jugadores[jugador]} no tiene suficientes fichas para apostar.")

    def chequear(self, jugador):
        print(f"Jugador {self.jugadores[jugador]} hace check.")

    def foldear(self, jugador):
        print(f"Jugador {self.jugadores[jugador]} se retira.")

    def finalizar_ronda(self):
        total_apostado = sum(apuesta[1] for apuesta in self.pila_apuestas)
        self.bote += total_apostado
        print(f"Fin de la ronda. Total apostado en esta ronda: {total_apostado}. Bote acumulado: {self.bote}.")
        self.pila_apuestas = []
        self.ronda_completada = True

    def siguiente_ronda(self):
        if self.ronda == 3:  # River
            print(f"Fin del juego. El bote final es de {self.bote} fichas.")
            return

        if self.ronda == 0:
            print("Pasando del Preflop al Flop.")
        elif self.ronda == 1:
            print("Pasando del Flop al Turn.")
        elif self.ronda == 2:
            print("Pasando del Turn al River.")

        self.ronda += 1
        self.ronda_completada = False
        self.turno = (self.turno + 1) % 6  # Cambiar el primer jugador en la siguiente ronda
        print(f"Comienza la ronda {self.ronda}. El primer jugador en hablar es {self.jugadores[self.turno]}.")

    def leer_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "" or linea.startswith("#"):
                    continue  # Saltar comentarios y líneas vacías
                
                instruccion = linea.split()

                if instruccion[0] == "SET":
                    if instruccion[1].startswith("R"):  # Stack de jugador
                        jugador = int(instruccion[1][1])  # Extraer número del jugador
                        cantidad = int(instruccion[2])
                        self.set_stack(jugador, cantidad)
                    elif instruccion[1] == "SB":
                        self.ciega_pequena = int(instruccion[2])
                        print(f"La ciega pequeña ahora es de {self.ciega_pequena} fichas.")
                    elif instruccion[1] == "BB":
                        self.ciega_grande = int(instruccion[2])
                        print(f"La ciega grande ahora es de {self.ciega_grande} fichas.")

                elif instruccion[0] == "BET":
                    jugador = int(instruccion[1][1])  # Extraer número del jugador
                    cantidad = int(instruccion[2])
                    self.apostar(jugador, cantidad)

                elif instruccion[0] == "CHECK":
                    jugador = int(instruccion[1][1])
                    self.chequear(jugador)

                elif instruccion[0] == "FOLD":
                    jugador = int(instruccion[1][1])
                    self.foldear(jugador)

                elif instruccion[0] == "ENDROUND":
                    self.finalizar_ronda()

                elif instruccion[0] == "NEXTROUND":
                    if self.ronda_completada:
                        self.siguiente_ronda()
                    else:
                        print("La ronda actual no se ha completado.")
# Ejemplo de uso:
vm = TexasHoldemVM()
vm.leer_archivo("ronda.txt")
