# This is a sample Python script.
from Logica import Logica
from Tablero import Tablero


def main():

    tab=Tablero()
    print("Starting quadrants...")
    tab.generate_board(2)
    tab.print_board()

    logica=Logica(tab)
    logica.start()



if __name__ == "__main__":
    main()
