from piece import *
from board import Board
from player import Player

"""
RUNS BY CYCLES
>Each cycle is when both White and Black make a move.
>Stars the game by a White Move.
>Every move, checks if the game is finished, prints board, and
prints the last move of the game.
>For each move:
>1. Ask the position of the piece to move
>2. Shows all possible move for that piece
>3. User chose one move the his or her turn is over
>4. The same with the next player
"""

class Game():
    def __init__(self):
        self.howToPlay = """
> This is the chess board, the black pieces are shown
at the top and the white pieces, at the bottom.
> Also, you have a legend of the pieces at the right
> To play, the player on turn will have to choose the
piece he or she wants to move by typing its cords.
> The cords are given by a letter and a number that are
both at the left and bottom of the board. Ex: G3
> Then, the possible moves for the chosen piece will be
displayed. They are shown by ( ) instead of [ ].
> You only have to choose one of the shown cord the same
way as before. Then it's the rival's turn
> Now you guys are all good to start playing!
>>> Press ENTER to go back to the main menu
        """
        self.menu = """
++++++++++++++++++++++++++++++++++++
            CHESS GAME
            1. Start Game
            2. How to Play
            3. Exit
                            by satender
++++++++++++++++++++++++++++++++++++
Choose an option:"""
        self.board = Board() 
       
        self.wPl = Player("w", wki) 
        self.bPl = Player("b", bki) 


    def displayMenu(self):
        print(self.menu) 

        while True:
            choice = input() 

            if choice != "" and choice.isnumeric():
                choice = int(choice)
                
                if choice == 1:
                    print("\n>>> GAME STARTED!\nGood luck, " + self.wPl.name + " and " + self.bPl.name + "!")
                    self.startGame(self.wPl, self.bPl) 
                elif choice == 2:
                    self.printHowToPlay()
                elif choice == 3:
                    print(">>> THANKS FOR PLAYING, COME BACK SOON!")
                    exit() 
                else:
                    print("Your choice must be a number between 1 and 3")
            else:
                print("Your choice must be a number [1-3]")


    def startGame(self, wPl, bPl):
        lastTurn = "b" 
        while True: 
            if lastTurn == "b":
                lastTurn = "w" 
                currentPl = self.wPl 
            else:
                lastTurn = "b"
                currentPl = self.bPl 

            (self.board).print(None) 

           
            if self.gameIsTied() != False:
                print(self.gameIsTied()) 
                exit() 

            
            if (currentPl.king).isOnCheck():      
                if (self.gameIsOver(currentPl) != False):
                    print(self.gameIsOver(currentPl))
                    exit() 
                else:
                    print(currentPl.teamName + " KING IS ON CHECK, PROTECT IT")
                    
                    (currentPl.king).protect()
            else:
                
                print(">>> " + currentPl.teamName + "'S TURN (" + currentPl.name + ")")
                self.runTurn(currentPl)


    def runTurn(self, currentPl):
        piece = self.getPieceToMove(currentPl.team) 
        to = self.getPositionTo(piece, currentPl.team, currentPl) 
        try:
            print(piece.moveTo(to[0], to[1])) 
        except:
            pass

    
    
    def printHowToPlay(self):
        print(">>> HOW TO PLAY\nThis is how the board looks like:") 
        (self.board).print(None) 
        print(self.howToPlay) 
        input() 
        self.displayMenu() 


    def getPieceToMove(self, team):
        while True:
            print("\nInsert the position of the piece to move:")
            piecePosition = input() 

            
            if len(piecePosition) == 0 or len(piecePosition) == 1:
                print("The input should be one letter and one digit, try again")
            else:
                if self.isValidPos(piecePosition):
                    if toSys(piecePosition, False):
                        
                        piecePosition = toSys(piecePosition, True)

                      
                        if self.validateForPiece(piecePosition, team):
                          
                            x = piecePosition[0]
                            y = piecePosition[1]
                           
                            piece = getPieceAtPosition(x, y)
                            

                            allPossibleMoves = piece.getMoves()
                            
                            if piece.__class__ == king:
                                allPossibleMoves = piece.discardCheckMoves(allPossibleMoves)

                            if len(allPossibleMoves) == 0:
                                print("No possible moves for " + piece.name + ", try another one")
                            else:
                                
                                return piece
                        else:
                            print("Empty spot, try another one")
                    else:
                        print("Invaid position, try another one")
                else:
                    print("Not a valid position, try another one.")
    
    
    def getPositionTo(self, piece, team, currentPl):
        
        allPossibleMoves = piece.getMoves()
        
        if piece.__class__ == king:
            allPossibleMoves = piece.discardCheckMoves(allPossibleMoves)

        (self.board).print(allPossibleMoves)

        piece.printPossibleMoves() 

        print('\nInsert "0" if you want to choose a different piece.')

        while True:
            positionTo = input() 

            
            if len(positionTo) == 0 or (positionTo != "0" and len(positionTo) == 1):
                print("The input should be one letter and one digit, try again")
            else:
                
                if positionTo == "0":
                    (self.board).print(None)
                    self.runTurn(currentPl) 
                    break

                if self.isValidPos(positionTo):
                    if toSys(positionTo, False):
                        positionTo = toSys(positionTo, True)
                        if [positionTo[0], positionTo[1]] in allPossibleMoves:
                            return positionTo 
                        else:
                            print("That move is not possible, check the list and try again")
                    else:
                        print("Invaid position, try another one")
                else:
                    print("Not a valid position, try another one.")


    def isValidPos(self, pos):
        if pos[0].isnumeric() and not pos[1].isnumeric():
            return True
        elif not pos[0].isnumeric() and pos[1].isnumeric():
            return True
        return False

    
    def validateForPiece(self, piecePosition, team):
        x = piecePosition[0]
        y = piecePosition[1]
        if not checkForPiece(x, y):
            return False
        else:
            if getPieceAtPosition(x, y).team != team:
                return False
        return True

   
    def gameIsTied(self):
        
        if (all_black_pieces == [bki]) and (all_white_pieces == [wki]):
            tieMessage = """
        +++++++++++++++++++++++++++++++++++++
                        GAME OVER   
            TIE BETWEEN BLACKS AND WHITES
        
        Congratulations, {pl1} and {pl2}!
        +++++++++++++++++++++++++++++++++++++
            """.format(pl1=self.wPl.name, pl2=self.bPl.name)
            return tieMessage
        
        return False
    

    def gameIsOver(self, currentPl):
        
        savingMoves = (currentPl.king).getSavingMoves()

        if len(savingMoves) == 0:
            endMessage = """
        +++++++++++++++++++++++++++++++++++++
                    GAME OVER
            {winnerTeam}'S ARE THE WINNERS
            CHECK MAKE ON {teamName}'S KING
        
        Congratulations!
        +++++++++++++++++++++++++++++++++++++
            """.format(winnerTeam=currentPl.opTeamName, teamName=currentPl.teamName)
            return endMessage
        
        return False