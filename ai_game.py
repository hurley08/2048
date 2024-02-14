import tkinter as tk
from g2048 import logic
from g2048 import board
from g2048 import ai
from g2048 import game


NUMBER_OF_MOVES = 4
SAMPLE_COUNT = 50
SPM_SCALE_PARAM = 10
SL_SCALE_PARAM = 4
SEARCH_PARAM = 200
played = []

game_inst = game.Game()
ai.ai_play(game_inst)