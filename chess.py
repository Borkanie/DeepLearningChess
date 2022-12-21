import numpy as np
from coordinate import coordinates
from piece import *
from square import square
from player import player
from board import board

class chessGame:
    def __init__(self):
        self.board = board()
        self.player1 = player(True)
        self.player2 = player(False)
        self.board.SetUpBoard(self.player1,self.player2)
        self.player1turn=True

    def Play(self):
        while(True):
            chess.Draw()
            if self.player1.points > 200:
                return self.player1
            if self.player2.points > 200:
                return self.player2
            if self.player1turn:
                print(f"It is {self.player1.GetColor()}'s turn please choose a piece ot move:")
           

    def Draw(self):
        self.board.Draw()

if __name__ == "__main__":
    chess = chessGame()
    winner = chess.Play()
