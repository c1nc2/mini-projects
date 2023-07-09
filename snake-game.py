import pygame as pg
"""importing pygame module/library"""

"""assigning the elements to their own variables"""
segments = [15, 16, 17]
size = segments[0]
### size <- variable, is the width and height
theway = segments[1]
### theway is the direction that the snake moves
head = segments[2]

n = theway
### n will help us get to x
apple_positioon = 99

"""shows the screens"""
screen_dimensions = [225] * 2
screen_surface = pg.display.set_mode(screen_dimensions, pg.SCALED)
screen_fill = screen_surface.fill

"""this the game functionality; putting some conditions here"""
while segments.count(head) % 2 * head % n * (head & 240):
    ### check if two overlaped or if the snake is out of the screen. if its false
    ### the game is over and it exists.

    if e := pg.event.get(768):
        ### check if any arrow key is pressed. if true, saves to the "e" variable

        theway = (e[0].key % 4 * 17 + 15) % 49 - n
        ### here this line just evaluates the key pressed numbers to theway

    segments = segments[apple_positioon != head:] + [head + theway]
    ### removes tail & adds new head. if it hits the apple, only adds new head, not remove the tail

    screen_fill('green')
    ### fill the screen with black color

    if apple_positioon == head:
        ### this conditional just check if the head of the snake hit the apple
        apple_positioon = segments[0]
        ### move apple to tail

    for i, v in enumerate([apple_positioon] + segments):
        ### loop used to draw, uses i variable to check if thats apple or just segments
        screen_fill('black' if i else 'red',
                            ((v - 1) % n * size, (v - n) // n * size, size, size))
        ### if loop goes for apple, draws "red" else "green" evaluates 

    pg.display.flip()
    """just updates the display everytime"""

    head+= theway 
    """head moves to theway"""

    pg.time.wait(100)
    """this delays the 100 milliseconds"""