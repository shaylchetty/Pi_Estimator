import pygame as p

PANEL_WIDTH = 400
PANEL_HEIGHT = 200
NUM_OF_BUTTONS = 3
BUTTON_WIDTH = PANEL_WIDTH/NUM_OF_BUTTONS


def drawPanel(screen):
    p.draw.rect(screen, (0, 255, 0), (0, 400, PANEL_WIDTH, PANEL_HEIGHT))


def drawButtons(screen):
    buttons = []
    colors = [(100, 255, 0), (255, 255, 100), (255, 100, 0)]
    labels = ['START', 'PAUSE', 'RESET']
    font = p.font.SysFont('Times New Roman', 25)
    for b in range(NUM_OF_BUTTONS):
        button = p.draw.rect(screen, colors[b],
                             (b*BUTTON_WIDTH, 400, BUTTON_WIDTH, PANEL_HEIGHT))
        text = font.render(labels[b], True, (0, 0, 0))
        screen.blit(text, button)
        buttons.append(button)
    return buttons

