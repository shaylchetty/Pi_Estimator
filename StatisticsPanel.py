import pygame as p
import Floorboards

# import SimulationMain
# #circular import will cause error

PANEL_WIDTH = 200
PANEL_HEIGHT = 600


def drawPanel(screen):
    p.draw.rect(screen, "Black", (400, 0, PANEL_WIDTH, PANEL_HEIGHT))


def run_text(surface, text, pos, font, color=p.Color('red')):
    x, y = pos
    words = [word.split(' ') for word in text.splitlines()]
    max_width, max_height = surface.get_size()
    space = font.size(' ')[0]
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                y += word_height
                x = pos[0]
            surface.blit(word_surface, (x, y))
            x += word_width + space
        y += word_height
        x = pos[0]


def getStatTxt(count, countContact):
    approximationPI = ''
    pi = str(3.14159)

    # if count > 0:
    #     exprimental_Prob = str(countContact/count)
    if countContact > 0:
        approximationPI = str(round((2*Floorboards.getNeedleLength()
                              * count)/(Floorboards.getBoardWidth()*countContact), 5))
    text = "Needle Simulation:\n START to drop needles\n PAUSE to stop sim \n RESET to restart simulation.\n" \
           "# Needles Dropped: " + str(count) + " \n # Needles in Contact: " + str(countContact) + "\n\n" \
        "Value   of  PI: " + pi + "\n" \
        "Approx of PI: " + approximationPI + ""
    return text
    return count
