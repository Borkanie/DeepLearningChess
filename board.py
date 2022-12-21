import numpy as np
from coordinate import coordinates
from piece import *
from square import square
from player import player



class board:
    def DoTurn(self,player:player):
        """Asks the player to make an action and checks to see if it is possible.

        Args:
            player (player): the player whose turn is 

        Returns:
            Tuple(piece,coordinate): 
        """
        doMove = False
        while doMove:
            playerPieceCoord = input()
            piece = player.HasPiece(coordinates(playerPieceCoord[0],playerPieceCoord[1]))
            if piece is None:
                continue
            doMove()
        print(f"You chose piece {piece.name} from position {piece.coordinates}")
        print(f"Where would you like to move it to?")
        doMove = False
        while doMove:
            newCoord = input()
            try:
                coord = coordinates(newCoord[0],newCoord[1])
                if self.matrix[coord.X,coord.Y].piece is None or player.HasPiece(coord) is not None:
                    print(f"that move is illegal please try again")
                    continue
                doMove = True
            except Exception:
                print(f"Incorrect coordinates {newCoord}")
        return [piece,coord]
    
    def SetUpBoard(self,player1:player,player2:player):
        """Generates the board layout where the first player plays on top and the second player on the bottom
        """
        
        if player1.whitePlayer is player2.whitePlayer:
            raise Exception(f"How can we have 2 {player1.GetColor()} players")
        
        for piece in player1.pieces:
            self.matrix.append(square(piece))
        for piece in player2.pieces:
            self.matrix.append(square(piece))

        for i in np.arange(2, 6):
            matrix = []
            for j in np.arange(0, 8):
                matrix.append(square(0, 0, "none"))
            self.matrix.append(matrix)

    def __init__(self):
        """Set's up a new board with pieces.
        Set's player1 as the first player.
        """
        self.matrix = []
        self.SetUpBoard()
        self.player1Turn = True

    def Draw(self):
        """Draws the current state of the table to the console using print statement.
        """
        for i in np.arange(0, 8):
            result = str(i + 1) + "|"
            for j in np.arange(0, 8):
                result += self.matrix[i][j].Draw() + " "
            print(result)
        print("  ---------------")
        print("  A B C D E F G H")

    def GetMoves(self,player1=True):
        """Returns all the possible moves for the selected player on the current stage of the board.

        Args:
            player1 (bool, optional): True if the targeted player is player 1 false if the targeted player is player 2. Defaults to True.
        """

        movements =[]
        for i in np.arange(0,8):
            for j in np.arange(0,8):
                if self.matrix[i][j].piece.player is player1:
                    movements.append([self.matrix[i][j].piece,self.matrix[i][j].piece.GetMoves()])

        for possibility in movements:
            for move in possibility:
                self.matrix[i][j].price == move[0]
