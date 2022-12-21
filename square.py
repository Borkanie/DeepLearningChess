from piece import *
from coordinate import coordinates


class square:
    """A square on the chess board.
    It can hold a piece or it can be empty.
    Empty squares are having the field self.piece as equal to None.
    """

    def __init__(self, x: int, y: int, pieceName: str, player1=True):
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
            self.piece = piece(pieceName, player1, self.coordinates)
        else:
            self.piece = None

    def __init__(self, piece: piece):
        """Creates a square filled with the given piece using it's coordinates.

        Args:
            piece (piece): The piece that we want place.
        """
        self.coordinates = piece.coordinates
        self.piece = piece

    def Draw(self):
        """Returns the symbol representing the square as a string.

        Returns:
            str: The symbol for the square.
        """
        if self.piece is not None:
            return self.piece.Draw()
        else:
            return '0'
