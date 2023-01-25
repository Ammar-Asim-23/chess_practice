'''This is our main driver file. It will be responsible for handling 
user input and displaying the current GameState object.'''

import pygame as p
import Chess_Engine

WIDTH=HEIGHT = 512
DIMENSION = 8
SQ_SIZE = WIDTH//DIMENSION
MAXFPS = 15
IMAGES= {}

''' Initialize a global dictionary of images.
This will be called exactly once in main as it a time consuming process'''

def loadImages():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR","bp", "wp","wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f'images/{piece}.png'), (SQ_SIZE,SQ_SIZE))
        
