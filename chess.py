import numpy as np


tower = "tura"

horse = "cal"

bishop = "nebun"

queen = "regina"

king = "rege"

pawn = "pain"

pieces = [pawn, king, queen, bishop, horse, tower]

def valueOfPiece(peice: str):
    """
    Return the value of a piece based on the previously defined array

    Args:
        peice (str): the name of the piece

    Returns:
        int: The value precieved by the rules of chess
    """
    if piece == pawn:

        return 1

    if piece == king:

        return -1

    if piece == queen:

        return 9

    if piece == bishop:

        return 3

    if piece == horse:

        return 3

    if piece == tower:

        return 3

    return 0

class coordinates:
    """ A class represting the X Y coordinates of a chess board using two integers
    """
    def __init__(self,x:int,y:int):
        self.X = x
        self.Y = y

class piece:
    """A class representing a chess piece.
    It can be one of the predefined strings from 
    """
    def __init__(self, piece: str, player1Piece: bool,coordinate:coordinates):
        """Creates a new chess piece.

        Args:
            piece (str): The type of the piece
            player1Piece (bool): If TRUE than piece will belong to player 1 if FALSE it will belong to player 2
            coordinate (coordinates): The coordinates on the table at which point the piece will reside

        Raises:
            Exception: _description_
        """
        if piece not in pieces:
            raise Exception(
                f"{peice} is not a valid peice please choose from:{pieces}")
        self.name = piece
        self.value = valueOfPiece(piece)
        self.player = player1Piece
        self.coordinates=coordinate

    def Draw(self):
        """Returns a string representing the piece.

        Returns:
            str: The symbol for the chess piece.
        """
        if self.name == pawn:
            return 'p'
        elif self.name == king:
            return 'K'
        elif self.name == queen:
            return 'Q'
        elif self.name == bishop:
            return 'b'
        elif self.name == horse:
            return 'h'
        elif self.name == tower:
            return 'T'

    def GetMoves(self):
        """Return an aray with all the moves possible for the piece ,only restriction being that the moves have to happen on board.

        Returns:
            list<coordinates>: The list of possible coordinates on the table.
        """
        if self.name == pawn:
            return [coordinates(self.coordinates.X, self.coordinates.Y)]
        elif self.name == king:
            posib = []
            for i in np.arange(-1,1):
                for j in np.arange(-1,1):
                    if self.coordinates.X+i<0 or self.coordinates.Y+j<0:
                        posib.append(coordinates(self.coordinates.X+i, self.coordinates.Y+j))
            return posib
        elif self.name == queen:
            posib = []
            for i in np.arange(-8,8):
                if self.coordinates.X+i<0 or self.coordinates.Y+i<0:
                    posib.append(coordinates(self.coordinates.X+i, self.coordinates.Y+i))
            for i in np.arange(-8,8):
                if self.coordinates.X+i<0 or self.coordinates.Y<0:
                    posib.append(coordinates(self.coordinates.X+i, self.coordinates.Y))
            for j in np.arange(-8,8):
                if self.coordinates.X<0 or self.coordinates.Y+j<0:
                    posib.append(coordinates(self.coordinates.X, self.coordinates.Y+j))
            return posib
        elif self.name == bishop:
            posib = []
            for i in np.arange(-8,8):
                if self.coordinates.X+i<0 or self.coordinates.Y+i<0:
                    posib.append(coordinates(self.coordinates.X+i, self.coordinates.Y+i))
            return posib
        elif self.name == horse:
            return 'h'
        elif self.name == tower:
            posib = []
            for i in np.arange(-8,8):
                if self.coordinates.X+i<0 or self.coordinates.Y<0:
                    posib.append(coordinates(self.coordinates.X+i, self.coordinates.Y))
            for j in np.arange(-8,8):
                if self.coordinates.X<0 or self.coordinates.Y+j<0:
                    posib.append(coordinates(self.coordinates.X, self.coordinates.Y+j))
            return posib




class square:
    """A square on the chess board
    """
    def __init__(self, x: int, y: int, pieceName: str,player1=True):
        """Creates a square on the board on the given coordinates.
        If pieceName is not in the list of pieces than the square will be declared as empty.

        Args:
            x (int): Position on the horizontal axis (Labeled by letters).
            y (int): Position on the vertical axis.
            pieceName (str): The piece we want to place on the square.
            player1 (bool): Set's the chess to player 1 if True and to player 2 if False (default is True)
        """
        self.coordinates = coordinates(x, y)
        if pieceName in pieces:
            self.piece = piece(pieceName, player1,self.coordinates)
        else:
            self.piece = None

    def Draw(self):
        """Returns the symbol representing the square as a string.

        Returns:
            str: The symbol for the square.
        """
        if self.piece is not None:
            return self.piece.Draw()
        else:
            return '0'


class board:
    def SetUpBoard(self):
        """Generates the board layout where the first player plays on top and the second player on the bottom
        """
        self.matrix.append([square(0, 0, tower), square(0, 1, horse), square(0, 2, bishop), square(0, 3, king),
                            square(0, 4, queen), square(0, 5, bishop), square(0, 6, horse), square(0, 7, tower)])

        self.matrix.append([square(1, 0, pawn), square(1, 1, pawn), square(1, 2, pawn), square(1, 3, pawn),
                            square(1, 4, pawn), square(1, 5, pawn), square(1, 6, pawn), square(1, 7, pawn)])
        
        for i in np.arange(2, 6):
            matrix = []
            for j in np.arange(0, 8):
                matrix.append(square(0, 0, "none"))
            self.matrix.append(matrix)

        self.matrix.append([square(6, 0, pawn), square(6, 1, pawn), square(6, 2, pawn), square(6, 3, pawn),
                            square(6, 4, pawn), square(6, 5, pawn), square(6, 6, pawn), square(6, 7, pawn)])

        self.matrix.append([square(7, 0, tower), square(7, 1, horse), square(7, 2, bishop), square(7, 3, king),
                            square(7, 4, queen), square(7, 5, bishop), square(7, 6, horse), square(7, 7, tower)])

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
            player1 (bool, optional): True if the targeted player is player 1 false if the tageted player is player 2. Defaults to True.
        """
        
       
        movements =[]
        for i in np.arange(0,8):
            for j in np.arange(0,8):
                if self.matrix[i][j].piece.player is player1:
                    movements.append([self.matrix[i][j].piece,self.matrix[i][j].piece.GetMoves()])
        
        for possibil in movements:
            for move in possibil:
                self.matrix[i][j].price == move[0]
if __name__ == "__main__":
    board = board()
    board.Draw()
