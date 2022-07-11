import pygame as p
import random as r
import math as m

PANEL_HEIGHT = PANEL_WIDTH = 400
NUM_OF_BOARDS = 10
BOARD_WIDTH = PANEL_WIDTH/NUM_OF_BOARDS
NEEDLE_LENGTH = (2/3) * BOARD_WIDTH


def getNeedleLength():
    return NEEDLE_LENGTH


def getBoardWidth():
    return BOARD_WIDTH


def setup(screen):
    p.draw.rect(screen, (179, 89, 150), (0, 0, 400, 400))
    for n in range(NUM_OF_BOARDS):
        p.draw.line(screen, (25, 0, 255), (n*BOARD_WIDTH, 0),
                    (n*BOARD_WIDTH, PANEL_HEIGHT), 2)
        p.draw.rect(screen, (124, 100, 2), (400, 0, 600, 600))
        p.draw.rect(screen, (0, 100, 128), (0, 402, 400, 600))


def needle_toss(screen):
    startPoint = (r.uniform(0, PANEL_WIDTH), r.uniform(0, PANEL_HEIGHT))
    angle = r.uniform(0, 2*m.pi)
    endPoint = (startPoint[0] + NEEDLE_LENGTH*m.cos(angle),
                startPoint[1] + NEEDLE_LENGTH*m.sin(angle))
    p.draw.line(screen, (100, 255, 255), startPoint, endPoint, 2)

    p1 = m.ceil(startPoint[0]/BOARD_WIDTH)
    p2 = m.ceil(endPoint[0]/BOARD_WIDTH)
    if p1 != p2:
        return 1
    else:
        return 0

    # return Needle
