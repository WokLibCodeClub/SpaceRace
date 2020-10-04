#!/bin/python3

from turtle import *
from random import randint

# ============= Screen ==============

WIDTH = 400
HEIGHT = 400
screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor(0,0,0)
screen.bgpic('space-background.jpeg')
XMAX = WIDTH/2.0; XMIN = -WIDTH/2.0
YMAX = HEIGHT/2.0; YMIN = -HEIGHT/2.0
# Images
screen.register_shape("asteroid.png")
screen.register_shape("rocket.png")
# Animation control
screen.tracer(0)
screen.listen()

# ============= Rocket ==============


# ========== Rocks ==============

  
# ========== Scores ==================

  
# ======= Win or lose ===================


# ============ Main loop ================

playing = True

while playing:
      
  # Update the picture
  screen.update()