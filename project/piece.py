"""
PARAMETHERS:
X -> number of the List
Y -> index on the List Y
team -> black or white
name -> name of the piece
chessman -> variable with the name of the symbol
onGame -> True if piece has not been killed yet
"""

class Piece():
  def __init__(self,x,y,team,name,chessman):
    self.x = x
    self.y = y
    self.team = team
    self.name = name
    self.chessman = chessman
    self.onGame = True

  def kill(self):
    self.onGame = False

  
    if self in all_black_pieces:
      all_black_pieces.remove(self)
    
    if self in all_white_pieces:
      all_white_pieces.remove(self)

  def moveTo(self, x, y):
   
    
    if not checkForPiece(x,y):
    
      rtMessage = "\n" + self.name + " moved to " + toBoard(x, y)
     
      self.x = x
      self.y = y
    else: #if it is to occupied spot, its a kill
      pieceOnSpot = getPieceAtPosition(x, y)
      if pieceOnSpot.team != self.team:
        #print kill message
        rtMessage = "\n" + pieceOnSpot.name + " killed by a " + self.name
        pieceOnSpot.kill()
        
        self.x = x
        self.y = y

   
    if self.__class__ == pawn:
      self.userMoves += 1

   
    #for white piece
    if (self.__class__ == pawn) and (self.team == "w") and (self.x == 0):
      self.replace()
    #for black piece
    if (self.__class__ == pawn) and (self.team == "b") and (self.x == 7):
      self.replace()
    
    return rtMessage 

 
  #prints the possible moves for a piece
  def printPossibleMoves(self):
      allPossibleMoves = self.getMoves()
  
      print("Chose your next move for the " + self.name +":")
      for move in allPossibleMoves:
          posX = move[0]
          posY = move[1]
          print(">>> " + toBoard(posX, posY))


  def discardImMoves(self, moves):
    toDelete = []

    #check if piece on move spot
    for move in moves:
      if checkForPiece(move[0], move[1]):
        pieceAtSpot = getPieceAtPosition(move[0], move[1])
        if self.team == pieceAtSpot.team:
         
          toDelete.append(move)

    #identifies moves outside of the board
    for move in moves:
      for cord in move:
        if cord < 0 or cord > 7:
          toDelete.append(move)

    #deletes moves outside the board
    for i in toDelete:
      if i in moves:
        moves.remove(i)

    
    finalMoves = []
    for move in moves:
      if move not in finalMoves:
        finalMoves.append(move)

    return finalMoves 


class pawn(Piece):
  def __init__(self, x, y, team):
   
    if team == "w":
      chessman = "♙"
      name = "White Pawn"
    else:
      chessman = "♟"
      name = "Black Pawn"

    Piece.__init__(self, x, y, team, name, chessman)
    self.userMoves = 0 
  

  def getMoves(self):
    moves = [] 
    a = self.x
    b = self.y

   
    if (self.team == "w"):
      a -= 1
      if not checkForPiece(a, b): 
        moves.append([a, b]) 

        if (self.userMoves == 0 and not checkForPiece(a-1, b)):
          self.firstMove = False
          moves.append([a-1,b]) 
    else:
      a += 1
      if not checkForPiece(a, b): 
        moves.append([a, b])

        if (self.userMoves == 0 and not checkForPiece(a+1, b)):
          self.firstMove = False
          moves.append([a+1,b]) 
    
    
    possEat1 = [a,b-1] 
    possEat2 = [a,b+1] 
    if (checkForPiece(possEat1[0], possEat1[1]) == True): 
      if (getPieceAtPosition(possEat1[0], possEat1[1]).team != self.team): 
        moves.append(possEat1) #
    if (checkForPiece(possEat2[0], possEat2[1]) == True):
      if (getPieceAtPosition(possEat2[0], possEat2[1]).team != self.team):
        moves.append(possEat2)

    return self.discardImMoves(moves)


  def getKillerMoves(self):
    moves = [] 
    a = self.x
    b = self.y
    
    if self.team == "w":
      a -= 1
    else: 
      a += 1


    possEat1 = [a,b-1]
    possEat2 = [a,b+1] 
    if (checkForPiece(possEat1[0], possEat1[1]) == True): 
      if (getPieceAtPosition(possEat1[0], possEat1[1]).team != self.team): 
        moves.append(possEat1)
    #same with second piece
    if (checkForPiece(possEat2[0], possEat2[1]) == True):
      if (getPieceAtPosition(possEat2[0], possEat2[1]).team != self.team):
        moves.append(possEat2)

    return self.discardImMoves(moves)
  

  def replace(self):
    x = self.x
    y = self.y
    printMes = """
    Choose one piece (number) to replace your pawn:
    1. ♕ ♛  Queen
    2. ♔ ♚  King
    3. ♗ ♝  Bishop
    4. ♘ ♞  Knight
    5. ♖ ♜  Rook
    6. ♙ ♟ Pawn
    """
    print(printMes)

    
    while True:  
      while True:
        try:
          choice = int(input())
          break
        except:
          print("Insert a number")

  
      if 1 <= int(choice) <= 5:
        choice = int(choice)
        print("") 
        
        
        if choice == 1:
          self.kill()
          addedQueen = queen(x, y, self.team)
          all_pieces.append(addedQueen)
          print("Pawn replaced by a Queen")
        elif choice == 2:
          self.kill()
          addedKing = king(x, y, self.team)
          all_pieces.append(addedKing)
          print("Pawn replaced by a King")
        elif choice == 3:
          self.kill()
          addedBishop = bishop(x, y, self.team)
          all_pieces.append(addedBishop)
          print("Pawn replaced by a Bishop")
        elif choice == 4:
          self.kill()
          addedKnight = knight(x, y, self.team)
          all_pieces.append(addedKnight)
          print("Pawn replaced by a Knight")
        elif choice == 5:
          self.kill()
          addedRook = rook(x, y, self.team)
          all_pieces.append(addedRook)
          print("Pawn replaced by a Rook")

        break
      else:
        print("Invalid input, please try again")


class rook(Piece):   
  def __init__(self, x, y, team):
  
    if team == "w":
      chessman = "♖"
      name = "White Rook"
    else:
      chessman = "♜"
      name = "Black Rook"

    Piece.__init__(self, x, y, team, name, chessman) 


  def getMoves(self):
    moves = [] 
    a = self.x
    b = self.y

    #stats adding the four next-moves
    moves.append([a+1, b])
    moves.append([a-1, b])
    moves.append([a, b+1])
    moves.append([a, b-1])

    i = 1

    while(not checkForPiece(a-i, b) and (a-i >= 0)):
      moves.append([a-i, b])

      
      if (checkForPiece(a-i-1, b)):
        if(getPieceAtPosition(a-i-1, b).team != self.team):
          moves.append([a-i-1, b])
      i += 1

    i = 1
    #GOING DOWN THE BOARD
    while(not checkForPiece(a+i, b) and (a+i <= 7)):
      moves.append([a+i, b])

      if(checkForPiece(a+i+1, b)):
        if (getPieceAtPosition(a+i+1, b).team != self.team):
          moves.append([a+i+1, b])
      i += 1
    
    i = 1
    #GOING LEFT THE BOARD
    while(not checkForPiece(a, b-i) and (b-i >= 0)):
      moves.append([a, b-i])

      if(checkForPiece(a, b-i-1)):
        if (getPieceAtPosition(a, b-i-1).team != self.team):
          moves.append([a, b-i-1])
      i += 1

    i = 1
    #GOING RIGHT THE BOARD
    while(not checkForPiece(a, b+i) and (b+i <= 7)):
      moves.append([a, b+i])

      if(checkForPiece(a, b+i+1)):
        if (getPieceAtPosition(a, b+i+1).team != self.team):
          moves.append([a, b+i+1])
      i += 1

    return self.discardImMoves(moves)


class knight(Piece):   
  def __init__(self, x, y, team):
  
    if team == "w":
      chessman = "♘"
      name = "White Knight"
    else:
      chessman = "♞"
      name = "Black Knight"

    Piece.__init__(self, x, y, team, name, chessman)


  def getMoves(self):
    moves = []
    a = self.x
    b = self.y

    #there are just 8 moves for every knight
    moves.append([a-2, b+1])
    moves.append([a-1, b+2])
    moves.append([a+1, b+2])
    moves.append([a+2, b+1])
    moves.append([a+2, b-1])
    moves.append([a+1, b-2])
    moves.append([a-1, b-2])
    moves.append([a-2, b-1])

    return self.discardImMoves(moves)


class bishop(Piece):   
  def __init__(self, x, y, team):
  
    if team == "w":
      chessman = "♗"
      name = "White Bishop"
    else:
      chessman = "♝"
      name = "Black Bishop"

    Piece.__init__(self, x, y, team, name, chessman) 


  def getMoves(self):
    moves = [] 
    a = self.x
    b = self.y

    #stats adding the four next-moves
    moves.append([a+1, b+1])
    moves.append([a+1, b-1])
    moves.append([a-1, b+1])
    moves.append([a-1, b-1])

    i = 1

    while(not checkForPiece(a-i, b+i) and (a-i >= 0) and (b+i <= 7)):
      moves.append([a-i, b+i])
      
      #checks if rook can eat a piece and add that move as possible
      if (checkForPiece(a-i-1, b+i+1)):
        if(getPieceAtPosition(a-i-1, b+i+1).team != self.team):
          moves.append([a-i-1, b+i+1])
          
      i += 1


    i = 1
    #GOING DOWN-RIGHT THE BOARD
    while(not checkForPiece(a+i, b+i) and (a+i <= 7) and (b+i <= 7)):
      moves.append([a+i, b+i])
      
      if(checkForPiece(a+i+1, b+i+1)):
        if (getPieceAtPosition(a+i+1, b+i+1).team != self.team):
          moves.append([a+i+1, b+i+1])
          
      i += 1
    
    i = 1
    #GOING UP-LEFT THE BOARD
    while(not checkForPiece(a-i, b-i) and (b-i >= 0) and (a-i >= 0)):
      moves.append([a-i, b-i])
      
      if(checkForPiece(a-i-1, b-i-1)):
        if (getPieceAtPosition(a-i-1, b-i-1).team != self.team):
          moves.append([a-i-1, b-i-1])
          
      i += 1

    i = 1
    #GOING DOWN-LEFT THE BOARD
    while(not checkForPiece(a+i, b-i) and (b+i >= 0) and (a+i <= 7)):
      moves.append([a+i, b-i])
      
      if(checkForPiece(a+i+1, b-i-1)):
        if (getPieceAtPosition(a+i+1, b-i-1).team != self.team):
          moves.append([a+i+1, b-i-1])
          
      i += 1

    return self.discardImMoves(moves)


class king(Piece):
  def __init__(self, x, y, team):
  
    if team == "w":
      chessman = "♔"
      name = "White King"
    else:
      chessman = "♚"
      name = "Black King"

    Piece.__init__(self, x, y, team, name, chessman) 
  

  def getMoves(self):
    moves = []
    a = self.x
    b = self.y

    #there are just 8 moves for every king
    moves.append([a-1, b])
    moves.append([a-1, b+1])
    moves.append([a, b+1])
    moves.append([a+1, b+1])
    moves.append([a+1, b])
    moves.append([a+1, b-1])
    moves.append([a, b-1])
    moves.append([a-1, b-1])
    
    return self.discardImMoves(moves)

 
  def getOpponetMoves(self):
    result = [] 

   
    if self.team == "w":
      teamList = all_black_pieces
    else:
      teamList = all_white_pieces

    for piece in teamList:
      
      if piece.__class__ != pawn:
        moves = piece.getMoves()
      else: 
        moves = piece.getKillerMoves() 

      for move in moves:
        #check if move is not repeated
        if move not in result:
          result.append(move)
    
    return result

  
  #Returns True is the king of the given team is on check
  #Otherwise, returns False
  def isOnCheck(self):
  
    posKing = [self.x, self.y]
    if self.team == "w":
      oppositeTeam = "b"
    else:
      oppositeTeam = "w"


    tPiece = None
    actTX = None
    actTY = None
    for piece in all_pieces:
      piecePos = [piece.x, piece.y]
      if piecePos == posKing and piece != self:
        tPiece = piece
        actTX = piece.x
        actTY = piece.y
    
        piece.moveTo(9, 9)
        break

  
    rivalMoves = self.getOpponetMoves()

  
    if tPiece != None:
      tPiece.moveTo(actTX, actTY)

    if posKing in rivalMoves:
      return True
    else:
      return False


  def getSavingMoves(self):
    savingKingMoves = []

    #set opposite team
    if self.team == "w":
      oppositeTeam = "b"
    else:
      oppositeTeam = "w"

    #get king's moves
    kingMoves = self.getMoves()


    actKingX = self.x
    actKingY = self.y

   
    for kingM in kingMoves:
      possX = kingM[0] 
      possY = kingM[1] 
    
      self.moveTo(possX, possY)
  
      if not self.isOnCheck():
        savingKingMoves.append([self.x, self.y])
    
   
    self.moveTo(actKingX, actKingY)

    return self.discardCheckMoves(savingKingMoves)


  def discardCheckMoves(self, moves):
    toDelete = [] 
    a = self.x 
    b = self.y

    
    for move in moves:
    
      pieceOnSpot = None
      posX = None
      posY = None
      if checkForPiece(move[0], move[1]):
        pieceOnSpot = getPieceAtPosition(move[0], move[1])
        #save piece on spot real position
        posX = pieceOnSpot.x
        posY = pieceOnSpot.y

      
        pieceOnSpot.moveTo(9, 9)

      
      self.moveTo(move[0], move[1])
      if self.team == "w":
        opTeam = "b"
      else:
        opTeam = "w"
      if self.isOnCheck():
        toDelete.append(move) #

    
      if pieceOnSpot != None:
        pieceOnSpot.moveTo(posX, posY)
    
      
      self.moveTo(a, b)
    
    
    for rem in toDelete:
      if rem in moves:
        moves.remove(rem)

    return moves 
  
  #--------------------------------------------------------------
  def protect(self):
    print("Move it to a saving position, shown below:")

    #get opposite team
    opTeam = "b" if self.team == "w" else "w"

    #get saving moves:
    savingMoves = king.getSavingMoves()

    #print board showing saving moves
    board.print(savingMoves)

    #show moves
    for move in savingMoves:
      posX = move[0]
      posY = move[1]
      print(">>> " + toBoard(posX, posY))
    
    while True:
      positionTo = input()

      if len(positionTo) == 0 or len(positionTo) == 1:
        print("The input should be one letter and one digit, try again")
      else:
        if toSys(positionTo, False):
          positionTo = toSys(positionTo, True)

          if [positionTo[0], positionTo[1]] in savingMoves:
            movePieceTo(king, positionTo[0], positionTo[1])
            break
          else:
            print("That move is not possible, check the list and try again")

        else:
          print("Invaid position, try another one")



class queen(Piece):  
  def __init__(self, x, y, team):
    #get symbol from symbols.py
    if team == "w":
      chessman = "♕"
      name = "White Queen"
    else:
      chessman = "♛"
      name = "Black Queen"
    
    Piece.__init__(self, x, y, team, name, chessman) 


  def getMoves(self):
    moves = []
    a = self.x
    b = self.y

    #Get moves like king's
    moves.append([a-1, b])
    moves.append([a-1, b+1])
    moves.append([a, b+1])
    moves.append([a+1, b+1])
    moves.append([a+1, b])
    moves.append([a+1, b-1])
    moves.append([a, b-1])
    moves.append([a-1, b-1])


    moves.append([a+1, b])
    moves.append([a-1, b])
    moves.append([a, b+1])
    moves.append([a, b-1])

    i = 1


    while(not checkForPiece(a-i, b) and (a-i >= 0)):
      moves.append([a-i, b])

      #checks if rook can eat a piece and add that move as possible
      if (checkForPiece(a-i-1, b)):
        if(getPieceAtPosition(a-i-1, b).team != self.team):
          moves.append([a-i-1, b])
      i += 1

    i = 1
    #GOING DOWN THE BOARD
    while(not checkForPiece(a+i, b) and (a+i <= 7)):
      moves.append([a+i, b])

      if(checkForPiece(a+i+1, b)):
        if (getPieceAtPosition(a+i+1, b).team != self.team):
          moves.append([a+i+1, b])
      i += 1
    
    i = 1
    #GOING LEFT THE BOARD
    while(not checkForPiece(a, b-i) and (b-i >= 0)):
      moves.append([a, b-i])

      if(checkForPiece(a, b-i-1)):
        if (getPieceAtPosition(a, b-i-1).team != self.team):
          moves.append([a, b-i-1])
      i += 1

    i = 1
    #GOING RIGHT THE BOARD
    while(not checkForPiece(a, b+i) and (b+i <= 7)):
      moves.append([a, b+i])

      if(checkForPiece(a, b+i+1)):
        if (getPieceAtPosition(a, b+i+1).team != self.team):
          moves.append([a, b+i+1])
      i += 1


    moves.append([a+1, b+1])
    moves.append([a+1, b-1])
    moves.append([a-1, b+1])
    moves.append([a-1, b-1])

    i = 1

    while(not checkForPiece(a-i, b+i) and (a-i >= 0) and (b+i <= 7)):
      moves.append([a-i, b+i])
      
      #checks if rook can eat a piece and add that move as possible
      if (checkForPiece(a-i-1, b+i+1)):
        if(getPieceAtPosition(a-i-1, b+i+1).team != self.team):
          moves.append([a-i-1, b+i+1])
          
      i += 1


    i = 1
    #GOING DOWN-RIGHT THE BOARD
    while(not checkForPiece(a+i, b+i) and (a+i <= 7) and (b+i <= 7)):
      moves.append([a+i, b+i])
      
      if(checkForPiece(a+i+1, b+i+1)):
        if (getPieceAtPosition(a+i+1, b+i+1).team != self.team):
          moves.append([a+i+1, b+i+1])
          
      i += 1
    
    i = 1
    #GOING UP-LEFT THE BOARD
    while(not checkForPiece(a-i, b-i) and (b-i >= 0) and (a-i >= 0)):
      moves.append([a-i, b-i])
      
      if(checkForPiece(a-i-1, b-i-1)):
        if (getPieceAtPosition(a-i-1, b-i-1).team != self.team):
          moves.append([a-i-1, b-i-1])
          
      i += 1

    i = 1
    #GOING DOWN-LEFT THE BOARD
    while(not checkForPiece(a+i, b-i) and (b+i >= 0) and (a+i <= 7)):
      moves.append([a+i, b-i])
      
      if(checkForPiece(a+i+1, b-i-1)):
        if (getPieceAtPosition(a+i+1, b-i-1).team != self.team):
          moves.append([a+i+1, b-i-1])
          
      i += 1
    
    return self.discardImMoves(moves)

"""
INITIAL POSITIONS
Position are set by the index of each list,
NOT by a matrix. "X" is number of the list and
"Y" is the index of the listX.
Position [0][0] is the top left spot
Position [7][7] is the bottom right spot
"""
#WHITES
wp1 = pawn(6,0,"w")
wp2 = pawn(6,1,"w")
wp3 = pawn(6,2,"w")
wp4 = pawn(6,3,"w")
wp5 = pawn(6,4,"w")
wp6 = pawn(6,5,"w")
wp7 = pawn(6,6,"w")
wp8 = pawn(6,7,"w")
wr1 = rook(7,0,"w")
wr2 = rook(7,7,"w")
wk1 = knight(7,1,"w")
wk2 = knight(7,6,"w")
wb1 = bishop(7,2,"w")
wb2 = bishop(7,5,"w")
wki = king(7,4,"w")
wqu = queen(7,3,"w")

#BLACKS
bp1 = pawn(1,0,"b")
bp2 = pawn(1,1,"b")
bp3 = pawn(1,2,"b")
bp4 = pawn(1,3,"b")
bp5 = pawn(1,4,"b")
bp6 = pawn(1,5,"b")
bp7 = pawn(1,6,"b")
bp8 = pawn(1,7,"b")
br1 = rook(0,0,"b")
br2 = rook(0,7,"b")
bk1 = knight(0,1,"b")
bk2 = knight(0,6,"b")
bb1 = bishop(0,2,"b")
bb2 = bishop(0,5,"b")
bki = king(0,4,"b")
bqu = queen(0,3,"b")

all_white_pieces = [wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8,wr1,wr2,wk1,wk2,wb1,wb2,wki,wqu]
all_black_pieces = [bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,br1,br2,bk1,bk2,bb1,bb2,bki,bqu]
all_pieces = [wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8,wr1,wr2,wk1,wk2,wb1,wb2,wki,wqu,bp1,bp2,
bp3,bp4,bp5,bp6,bp7,bp8,br1,br2,bk1,bk2,bb1,bb2,bki,bqu]


def toBoard(x, y):
  listX = [8,7,6,5,4,3,2,1,0,0,0,0]
  listY = ["A","B","C","D","E","F","G","H","0","0","0","0"]

  return listY[y] + str(listX[x])


def toSys(pos, tell):
  
  if len(pos) >= 3 and tell == True:
    print("")
    print('>>> Only "' + pos[:2] + '" in consideration.')

  #check if input is type A3 or 3A
  if pos[0].isnumeric():
    num = pos[0]
    let = (pos[1]).upper()
  else:
    let = (pos[0]).upper()
    num = pos[1]

  listY = ["A","B","C","D","E","F","G","H"]
  listX = [8,7,6,5,4,3,2,1]

  if (let in listY) and 1 <= int(num) <= 8:
    return listX.index(int(num)), listY.index(let)


def checkForPiece(x, y):
  for piece in all_pieces:
    if piece.onGame == True:
      if piece.x == x and piece.y == y:
        return True 
  return False


def getPieceAtPosition(x,y):
  for piece in all_pieces:
    if piece.onGame == True:
      if piece.x == x and piece.y == y:
        return piece
  return None