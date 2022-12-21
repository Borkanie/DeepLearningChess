from coordinate import coordinates


tower = "tower"
horse = "horse"
bishop = "bishop"
queen = "queen"
king = "king"
pawn = "pawn"
pieces = [tower, horse, bishop, queen, king, pawn]


def valueOfPiece(piece: str):
    """
    Return the value of a piece based on the previously defined array

    Args:
        piece (str): the name of the piece

    Returns:
        int: The value perceived by the rules of chess
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


class piece:
    """A class representing a chess piece.
    It can be one of the predefined strings from 
    """

    def __init__(self, piece: str, player1Piece: bool, coordinate: coordinates):
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
                f"{piece} is not a valid piece please choose from:{pieces}")
        self.name = piece
        self.value = valueOfPiece(piece)
        self.whitePlayer = player1Piece
        self.coordinates = coordinate

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
        """Return an array with all the moves possible for the piece ,only restriction being that the moves have to happen on board.

        Returns:
            list<coordinates>: The list of possible coordinates on the table.
        """
        if self.name == pawn:
            return [coordinates(self.coordinates.X, self.coordinates.Y)]
        elif self.name == king:
            possibility = []
            for i in np.arange(-1, 1):
                for j in np.arange(-1, 1):
                    if self.coordinates.X+i < 0 or self.coordinates.Y+j < 0:
                        possibility.append(coordinates(
                            self.coordinates.X+i, self.coordinates.Y+j))
            return possibility
        elif self.name == queen:
            possibility = []
            for i in np.arange(-8, 8):
                if self.coordinates.X+i < 0 or self.coordinates.Y+i < 0:
                    possibility.append(coordinates(
                        self.coordinates.X+i, self.coordinates.Y+i))
            for i in np.arange(-8, 8):
                if self.coordinates.X+i < 0 or self.coordinates.Y < 0:
                    possibility.append(coordinates(
                        self.coordinates.X+i, self.coordinates.Y))
            for j in np.arange(-8, 8):
                if self.coordinates.X < 0 or self.coordinates.Y+j < 0:
                    possibility.append(coordinates(
                        self.coordinates.X, self.coordinates.Y+j))
            return possibility
        elif self.name == bishop:
            possibility = []
            for i in np.arange(-8, 8):
                if self.coordinates.X+i < 0 or self.coordinates.Y+i < 0:
                    possibility.append(coordinates(
                        self.coordinates.X+i, self.coordinates.Y+i))
            return possibility
        elif self.name == horse:
            return 'h'
        elif self.name == tower:
            possibility = []
            for i in np.arange(-8, 8):
                if self.coordinates.X+i < 0 or self.coordinates.Y < 0:
                    possibility.append(coordinates(
                        self.coordinates.X+i, self.coordinates.Y))
            for j in np.arange(-8, 8):
                if self.coordinates.X < 0 or self.coordinates.Y+j < 0:
                    possibility.append(coordinates(
                        self.coordinates.X, self.coordinates.Y+j))
            return possibility

    def GetColor(self):
        if self.whitePlayer:
            return "white"
        else:
            return "black"
