#Just plays the game
from pyboy import PyBoy

game = PyBoy('_____________') #Enter path to ROM File of Street Fighter Alpha: Warriors' Dream

while True:
    game.tick()
