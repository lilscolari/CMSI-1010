"""
Name: Cameron Scolari
Collaborators: N/A
Date: 10/13/2022
Description: Blue square turns green if mouse button is pressed within square. Blue square turns red is mouse button is not pressed within square.
"""
from graphics import *

# Create the graphics window.
win = GraphWin('Mouse Pointer', 300, 300)

# Draw a rectangle using the graphics library.
minx = 100
miny = 100
maxx = 200
maxy = 200
r = Rectangle(Point(minx, miny), Point(maxx, maxy))
r.setFill('blue')
r.draw(win)

# Get the mouse coordinates.
while True:
    # For now, all your code must be within this loop.
    # Without the loop, you would only be able to click once!
    p = win.getMouse()
    x = p.getX()
    y = p.getY()
    print('x: ', x, ', y: ', y)

    if (x >= 100 and x <= 200) and (y >= 100 and y <= 200):
        r.setFill('green')
    else:
        r.setFill('red')