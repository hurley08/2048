import tkinter as tk
from g2048 import board, ai, logic



played = []
brd = board.Board()
game_inst = game.Game()
ai.ai_play(game_inst)