from A_frontend import Window_side
import pygame

pygame.init()

Window = pygame.display.set_mode((Window_side, Window_side))

# text
tutorial_font = pygame.font.SysFont('Calibri', 20)
micro_font = pygame.font.SysFont('Calibri', 20)
# images
background = pygame.image.load('menu_bg.jpg')
background = pygame.transform.scale(background, (Window_side, Window_side))


def credits_main():
    # backend of the "credits" page

    pygame.display.set_caption("Credits")

    while True:

        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            return

        Window.blit(background, (0, 0))

        Window.blit(tutorial_font.render( \
        u"5168 7559 3986 1544 - Приват Банк", \
        1, (0, 0, 0)), (150, 50))
        Window.blit(tutorial_font.render( \
        "Find us on Instagram: @miia_sonechko @pyskonus @yana_1171", \
        1, (0, 0, 0)), (40, 150))

        Window.blit(micro_font.render("press Esc to return to menu", \
        1, (0, 0, 0)), (190, 580))

        pygame.display.update()
