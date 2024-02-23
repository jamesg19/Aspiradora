from Aspiradora import Aspiradora


class Logica:

    def __init__(self, board):
        self.board = board
        self.vaccum=None

    def start(self):
        self.select_scenario()

    def select_scenario(self):
        flag = True
        while flag:

            n = input("What scenario do you want to simulate?\n1) Dumb\n2) Smart\n3) Exit\n")
            try:
                if int(n) == 1:
                    self.start_dumb()

                elif int(n) == 2:
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
        self.dumb_move()
        flag = True
        while flag:
            self.dirty_board(self.board.board)
            self.dumb_move()
            flag=self.want_continue()


    def start_smart(self):
        self.print_board1()
        self.initial_positicion_vac()
        flag = True
        while flag:
            self.dirty_board(self.board.board)
            self.smart_move()
            flag = self.want_continue()

    def initial_positicion_vac(self):
        print("Vaccum Added..")
        self.vaccum = Aspiradora(self.board.board, "dumb")
        self.print_board1()

    def dirty_board(self, board):
        n = input("Do you want to dirty quadrant? \n1) A\n2) B\n3) None\n")
        try:
            if int(n) == 1:
                if board[0][0]=="████VAC████":
                    board[0][0]="██x█VAC█x██"

                elif board[0][0]=="██x█VAC█x██":
                    board[0][0] = "██x█VAC█x██"
                else:
                    board[0][0] = "█x█x█x█x█x█"

                self.print_board1()
            elif int(n) == 2:
                if board[0][1] == "████VAC████":
                    board[0][1] = "██x█VAC█x██"

                elif board[0][1] == "██x█VAC█x██":
                    board[0][1] = "██x█VAC█x██"
                else:
                    board[0][1] = "█x█x█x█x█x█"
                self.print_board1()
            elif int(n) == 3:
                pass
            else:
                print("Invalid option")
                pass
        except ValueError:
            print("Invalid option numbers only")

    def print_board1(self):
        self.board.print_board()

    def dumb_move(self):


       n = input("Do u want move ->   <-? YES(1) | NO(2)")
       try:
           if int(n) == 1:
               self.vaccum.move_dumb(self.board.board)

           elif int(n) == 2:
               pass

           else:
               print("Invalid option")

           self.print_board1()

       except ValueError:
           print("Invalid option numbers only")




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





    def smart_move(self):
        # verify if the quadrant is dirty
        self.vaccum.move_smart(self.board.board)
        self.print_board1()
