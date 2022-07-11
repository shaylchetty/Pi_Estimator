import pygame as p
import Floorboards
import ButtonPanel
import StatisticsPanel


def main():
    p.init()
    screen = p.display.set_mode((600, 600))
    clock = p.time.Clock()
    Floorboards.setup(screen)
    buttons = ButtonPanel.drawButtons(screen)
    needle_toss = False
    running = True
    count = 0
    countContact = 0
    p.display.set_caption("PI Estimator")
    font = p.font.SysFont('Times New Roman', 12)
    while running:
        if needle_toss == True:
            countContact = countContact + Floorboards.needle_toss(screen)
            count = count + 1
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            if event.type == p.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(event.pos):
                    needle_toss = True
                if buttons[1].collidepoint(event.pos):
                    needle_toss = False
                if buttons[2].collidepoint(event.pos):
                    main()
                    needle_toss = False
        ButtonPanel.drawPanel(screen)
        ButtonPanel.drawButtons(screen)
        StatisticsPanel.drawPanel(screen)

        text = StatisticsPanel.getStatTxt(count, countContact)
        StatisticsPanel.run_text(screen, text, (420, 20), font)
        p.display.flip()
        clock.tick(10)
    p.quit()


main()
