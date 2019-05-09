import pygame
from A_frontend import Window_side, frontend_main
import A_settings
import A_tutorial
import A_credits

UPkey_prev = False
DOWNkey_prev = False
current_option = 0
options = ["Start", "Settings", "Tutorial", "Credits", "Quit"]
overall_options = 5
buttons_y_coords = [100, 200, 300, 400, 500]
button_x = 300
button_y = 80
all_x = 190

pygame.init()

Window = pygame.display.set_mode((Window_side, Window_side))


# text
capital_font = pygame.font.SysFont('Calibri', 50)
menu_font = pygame.font.SysFont('Algerian', 50)
micro_font = pygame.font.SysFont('Calibri', 20)
# images
background = pygame.image.load('menu_bg.jpg')
background = pygame.transform.scale(background, (Window_side, Window_side))

def draw_menu():
    # draws the menu page

    global current_option

    Window.blit(background, (0, 0))

    Window.blit(capital_font.render("iGame", 1, (0, 0, 0)), (240, 20))

    for i in range(len(options)):
        if i == current_option:
            Window.blit(menu_font.render(options[i], 1, \
            (255, 255, 255)), (all_x, buttons_y_coords[i]))
        else:
            Window.blit(menu_font.render(options[i], 1, \
            (0, 0, 0)), (all_x, buttons_y_coords[i]))

    Window.blit(micro_font.render("press space to choose", 1, (0, 0, 0)), \
    (220, 580))

    pygame.display.update()


def menu_main():
    # backend of the menu page

    pygame.display.set_caption("Menu")

    global current_option

    while True:

        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                return

        draw_menu()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if current_option == 0:
                current_option = overall_options - 1
            else:
                current_option -= 1
            pygame.time.delay(150)
        elif keys[pygame.K_DOWN]:
            if current_option == overall_options - 1:
                current_option = 0
            else:
                current_option += 1
            pygame.time.delay(150)

        if keys[pygame.K_SPACE]:
            if current_option == 0:
                frontend_main()
            elif current_option == 1:
                A_settings.settings_main()
            elif current_option == 2:
                A_tutorial.tutorial_main()
            elif current_option == 3:
                A_credits.credits_main()
            elif current_option == 4:
                return
