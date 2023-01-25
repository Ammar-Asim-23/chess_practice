'''This class is responsible for storing all the information about the chess game. Its also
 responsibe for determining the valid moves at the current state. It will also keep a move log.'''

class GameState():
    def __init__(self):
        
        #The board is a 8X8 2d list and each element has two chars.
        #1st char = color of piece (b=black,w=white,-=blank)
        #2nd char = type of piece (R=rook, N= knight, B=bishop, Q=queen, K=king, p=pawn)
        #The string "--" represents empty space
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--","--", "--", "--"], 
            ["--", "--", "--", "--", "--","--", "--", "--"],
            ["--", "--", "--", "--", "--","--", "--", "--"],
            ["--", "--", "--", "--", "--","--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR"]]
        
        self.white_to_move = True
        self.move_log = []
            