from Aspiradora import Aspiradora
import threading
import time
import random

from Tablero import Tablero


class Logica:

    def __init__(self, board):
        self.board = board
        self.vacuum = None
        self.thread1=None
        self.thread2=None
        self.pause_event_1 = threading.Event()
        self.pause_event_2 = threading.Event()

    def start(self):
        self.select_scenario()

    def select_scenario(self):
        flag = True
        while flag:

            n = input("What scenario do you want to simulate?\n1) Dumb\n2) Smart\n3) Exit\n")
            try:
                if int(n) == 1:
                    tab = Tablero()
                    tab.generate_board(2)
                    self.board = tab
                    self.start_dumb()

                elif int(n) == 2:
                    tab = Tablero()
                    tab.generate_board(2)
                    self.board = tab
                    self.start_smart()
                elif int(n) == 3:
                    flag = False
                    break
                else:
                    print("Invalid option")
                    pass
            except ValueError:
                print("Invalid option numbers only")

    def start_dumb(self):
        self.print_board1()
        self.initial_positicion_vac()

        # Crear instancias de Event para sincronización
        nombre_evento = threading.Event()
        continuar_evento = threading.Event()

        self.thread1 = threading.Thread(target=self.dirty_board, args=(nombre_evento, continuar_evento))
        self.thread2 = threading.Thread(target=self.dumb_move, args=(nombre_evento, continuar_evento))
        self.thread1.start()
        self.thread2.start()

        self.thread1.join()
        self.thread2.join()

    def dirty_board(self,nombre_evento, continuar_evento):
        while True:
            continuar_evento.clear()  # Indica al hilo 2 que debe detenerse
            board = self.board.board

            n = input("Do you want to dirty quadrant? \n1) A\n2) B\n3) None\n4) Exit")
            #time.sleep(9)
            try:
                if int(n) == 1:
                    if board[0][0] == "████VAC████":
                        board[0][0] = "██x█VAC█x██"
                    elif board[0][0] == "██x█VAC█x██":
                        board[0][0] = "██x█VAC█x██"
                    else:
                        board[0][0] = "█x█x█x█x█x█"
                    self.print_board1()
                    nombre_evento.nombre = n
                    nombre_evento.set()  # Establece el nombre para que el hilo 2 lo procese
                    continuar_evento.wait()  # Espera a que el hilo 2 pueda continuar

                elif int(n) == 2:
                    if board[0][1] == "████VAC████":
                        board[0][1] = "██x█VAC█x██"
                    elif board[0][1] == "██x█VAC█x██":
                        board[0][1] = "██x█VAC█x██"
                    else:
                        board[0][1] = "█x█x█x█x█x█"
                    self.print_board1()
                    nombre_evento.nombre = n
                    nombre_evento.exit = False
                    nombre_evento.set()  # Establece el nombre para que el hilo 2 lo procese
                    continuar_evento.wait()  # Espera a que el hilo 2 pueda continuar

                elif int(n) == 3:
                    nombre_evento.nombre = n
                    nombre_evento.exit = False
                    nombre_evento.set()  # Establece el nombre para que el hilo 2 lo procese
                    continuar_evento.wait()  # Espera a que el hilo 2 pueda continuar

                elif int(n) == 4:
                    nombre_evento.exit = True
                    nombre_evento.set()  # Establece el nombre para que el hilo 2 lo procese
                    break
                else:
                    print("Invalid option")
                    pass

            except ValueError:
                print("Invalid option numbers only")






    #Se mueve con aleatoriedad
    def dumb_move(self,nombre_evento, continuar_evento):
        while True :
            nombre_evento.wait()  # Espera a que se reciba el nombre

            n = random.randint(1, 2)
            #print(str(n))
            if int(n) == 1:
                print("The vacuum cleaner moves")
                self.vacuum.move_dumb(self.board.board)

            elif int(n) == 2:
                print("The vacuum cleaner does NOT move")
                pass

            else:
                print("Invalid option")

            self.print_board1()
            continuar_evento.set()  # Indica al hilo 1 que puede continuar preguntando
            nombre_evento.clear()  # Resetea el evento de nombre para futuras iteraciones

            if nombre_evento.exit!= False:
                break

    def start_smart(self):
        self.print_board1()
        self.initial_positicion_vac()

        nombre_evento = threading.Event()
        continuar_evento = threading.Event()

        self.thread1 = threading.Thread(target=self.dirty_board, args=(nombre_evento, continuar_evento))
        self.thread2 = threading.Thread(target=self.smart_move, args=(nombre_evento, continuar_evento))
        self.thread1.start()
        self.thread2.start()

        self.thread1.join()
        self.thread2.join()

    def initial_positicion_vac(self):
        print("Vacuum Added..")
        self.vacuum = Aspiradora(self.board.board, "dumb")
        self.print_board1()



    def print_board1(self):
        self.board.print_board()



    def want_continue(self):
        n = input("Do u want continue? YES(1) | NO(2)")
        try:
            if int(n) == 1:
                return True

            elif int(n) == 2:
                return False
            else:
                print("Invalid option")
                pass
        except ValueError:
            print("Invalid option numbers only")

    def smart_move(self,nombre_evento, continuar_evento):
        while True :
            nombre_evento.wait()  # Espera a que se reciba el nombre
            # verify if the quadrant is dirty
            self.vacuum.move_smart(self.board.board)
            self.print_board1()

            continuar_evento.set()  # Indica al hilo 1 que puede continuar preguntando
            nombre_evento.clear()  # Resetea el evento de nombre para futuras iteraciones

            if nombre_evento.exit != False:
                break

