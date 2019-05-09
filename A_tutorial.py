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

def tutorial_main():
    # backend and frontend of the "tutorial" page

    pygame.display.set_caption("Tutorial")

    while True:

        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                return


        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            return

        Window.blit(background, (0, 0))

        Window.blit(tutorial_font.render( \
        "1) Use keys 1, 2, 3 to switch between numbers you want to shoot", \
        1, (0, 0, 0)), (50, 50))
        Window.blit(tutorial_font.render( \
        "2) Use keys Right, Left, Down to rotate the bow", \
        1, (0, 0, 0)), (50, 100))
        Window.blit(tutorial_font.render( \
        "3) Use keys A, S, D to move the bow", \
        1, (0, 0, 0)), (50, 150))
        Window.blit(tutorial_font.render( \
        "4) Press and hold key Up to shoot", \
        1, (0, 0, 0)), (50, 200))
        Window.blit(tutorial_font.render( \
        "5) Press key Esc to return to menu", \
        1, (0, 0, 0)), (50, 250))
        Window.blit(tutorial_font.render( \
        "6) Red apples represent Ulam numbers, yellow - prime", \
        1, (0, 0, 0)), (50, 300))
        Window.blit(tutorial_font.render( \
        "numbers and green - lucky numbers", \
        1, (0, 0, 0)), (72, 350))
        Window.blit(tutorial_font.render( \
        "7) Apples accelerate as they move, so be quick!", \
        1, (0, 0, 0)), (50, 400))
        Window.blit(tutorial_font.render( \
        "8) Look at the header of the window to see current target", \
        1, (0, 0, 0)), (50, 450))


        Window.blit(micro_font.render("press Esc to return to menu", \
        1, (0, 0, 0)), (190, 580))

        pygame.display.update()
