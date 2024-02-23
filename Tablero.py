class Tablero:

    def __init__(self):
        self.board=None


    def print_board(self):
        print("A:            B:")
        for fila in self.board:
            print("   ".join(fila))

        print("\n")

    def generate_board(self,n):
        #columns and rows
        self.board = [["███████████" for _ in range(n)] for _ in range(1)]
        #return board

    def get_simbol(self,tablero,x):
        print(tablero[0][x])


    def ensuciar_cuadrante(self,tablero, x):
        tablero[0][x] = "█x█x█x█x█x█"
        return tablero






