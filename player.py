import numpy as np
from coordinate import coordinates
from piece import *


class player:
    def __init__(self, player1: bool):
        self.points = 8*1+3*2+3*2+5*2+9*1+1000
        self.whitePlayer = player1
        self.pieces = self.GetDefaultChessPieces()
        self.kingIsUnderAttack = False

    def GetDefaultChessPieces(self):
        """Returns the default configuration for a given player based on the value of the constructor defined player flag.

        Returns:
            list<pieces> : a list of pieces tarting with the first 8 being pawns and the rest are the other pieces.
        """
        pieces = []
        for i in np.arange(0, 8):
            if self.whitePlayer:
                pieces.append(piece(pawn, self.whitePlayer, coordinates(i, 1)))
            else:
                pieces.append(piece(pawn, self.whitePlayer, coordinates(i, 6)))
        if self.whitePlayer:
            kingRow = 0
        else:
            kingRow = 7
        pieces.append(piece(tower, self.whitePlayer, coordinates(0, kingRow)))
        pieces.append(piece(horse, self.whitePlayer, coordinates(1, kingRow)))
        pieces.append(piece(horse, self.whitePlayer, coordinates(2, kingRow)))
        pieces.append(piece(queen, self.whitePlayer, coordinates(3, kingRow)))
        pieces.append(piece(king, self.whitePlayer, coordinates(4, kingRow)))
        pieces.append(piece(horse, self.whitePlayer, coordinates(5, kingRow)))
        pieces.append(piece(horse, self.whitePlayer, coordinates(6, kingRow)))
        pieces.append(piece(tower, self.whitePlayer, coordinates(7, kingRow)))
        return pieces

    def GetColor(self):
        """Returns the color of the player based on the boolean player flag.

        Returns:
            string: The color "white" or "black".
        """
        if self.whitePLayer:
            return "white"
        else:
            return "black"

    def HasPiece(self, pieceToSearch: str):
        for piece in self.pieces:
            if pieceToSearch is piece.name:
                return piece
        return None

    def HasPiece(self, coordinates: coordinates):
        for piece in self.pieces:
            if coordinates is piece.coordinates:
                return piece
        return None
