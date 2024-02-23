class Aspiradora:

    def __init__(self,board,type):

        self.board=board
        self.initial_position_vac()


    def initial_position_vac(self):
        if self.board[0][0] == "█x█x█x█x█x█":
            #print("MATCH!!!!")
            self.board[0][0] = "██x█VAC█x██"

        else:
            self.board[0][0] = "████VAC████"


    def clean_wuadrant(self, board, x):
        board[0][x] = "███████████"


    def move_dumb(self, board):
        if board[0][0] == "████VAC████" or board[0][0] == "██x█VAC█x██":
            self.board[0][1] = "████VAC████"
            self.board[0][0] = "███████████"
        elif board[0][1] == "████VAC████" or board[0][1] == "██x█VAC█x██":
            self.board[0][0] = "████VAC████"
            self.board[0][1] = "███████████"


    def move_smart(self, board):
        #if (board[0][0] == "█x█x█x█x█x█" and board[0][1] == "██x█VAC█x██") or (board[0][0] == "█x█x█x█x█x█" and board[0][1] == "████VAC████" or board[0][0] == "██x█VAC█x██"):
            #self.board[0][0] = "████VAC████"
            #self.board[0][1] = "███████████"
        #elif (board[0][1] == "█x█x█x█x█x█" and board[0][0] == "██x█VAC█x██") or (board[0][1] == "█x█x█x█x█x█" and board[0][0] == "████VAC████") or board[0][1] == "██x█VAC█x██":
            #self.board[0][1] = "████VAC████"
            #self.board[0][0] = "███████████"
        if ( board[0][0] == "██x█VAC█x██"):
             self.board[0][0] = "████VAC████"

        elif (board[0][1] == "██x█VAC█x██"):
             self.board[0][1] = "████VAC████"










