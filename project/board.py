from piece import *

"""
PARAMETHER:
board -> Full empty board
legend -> The side text of the board when print
lets -> Letters for the cords
nums -> Numbers for the cords
FUNCTIONS:
print -> print the board on different states,
if sports is not None, it will print the spots 
highlighted by ( )
"""
class Board():
    def __init__(self):
        self.board = [
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"]
        ]
        self.legend = legend = [
        "| SYMBOLS:",
        "| W B",
        "| ♔ ♚ KINGS",
        "| ♕ ♛ QUEENS",
        "| ♖ ♜ ROOKS",
        "| ♘ ♞ KNIGHTS",
        "| ♗ ♝ BISHOPS",
        "| ♙ ♟ PAWNS",
        ]
        self.lets = ["(A)","(B)","(C)","(D)","(E)","(F)","(G)","(H)"]
        self.nums = ["(8)","(7)","(6)","(5)","(4)","(3)","(2)","(1)"]


    def print(self, spots):
        print("")

        #prints each row
        for i in range(0, 8):
            st = ""
            for j in range(0, 8):
              
                if (checkForPiece(i,j)):
                    piece = getPieceAtPosition(i, j)
                    if((spots != None) and ([i, j] in spots)): 
                        st += "(" + piece.chessman + ")"
                    else: 
                        st += " " + piece.chessman + " "
                else:
                    if((spots != None) and ([i, j] in spots)): 
                        st += "( )"
                    else: 
                        st += "[ ]"
            
        
            print(self.nums[i] + st + " " + self.legend[i])

        
        print("   ", end="")
        for i in self.lets:
            print(i, end="")
        print("")
        print("") 
