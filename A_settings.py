import pygame

pygame.init()

Window_side = 600
Window = pygame.display.set_mode((Window_side, Window_side))

# text
settings_font = pygame.font.SysFont('Algerian', 30)
micro_font = pygame.font.SysFont('Calibri', 20)
# images
background = pygame.image.load('menu_bg.jpg')
background = pygame.transform.scale(background, (Window_side, Window_side))

rotation_sensitivity = 2
moving_sensitivity = 2
current_setting = 0

def draw_settings():
    # frontend of the settings page

    global rotation_sensitivity, moving_sensitivity, current_setting

    Window.blit(background, (0, 0))

    Window.blit(micro_font.render("press Esc to return to menu", \
    1, (0, 0, 0)), (190, 580))

    if current_setting == 0:
        Window.blit(settings_font.render( \
        "Bow rotation sensitivity: " + str(rotation_sensitivity), \
        1, (255, 255, 255)), (95, 200))

        Window.blit(settings_font.render( \
        "Bow moving sensitivity: " + str(moving_sensitivity), \
        1, (0, 0, 0)), (105, 300))
    else:
        Window.blit(settings_font.render( \
        "Bow rotation sensitivity: " + str(rotation_sensitivity), \
        1, (0, 0, 0)), (95, 200))

        Window.blit(settings_font.render( \
        "Bow moving sensitivity: " + str(moving_sensitivity), \
        1, (255, 255, 255)), (105, 300))

    pygame.display.update()

def settings_main():
    #backend of the settings page

    global rotation_sensitivity, moving_sensitivity, current_setting

    pygame.display.set_caption("Settings")

    while True:

        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            return

        if keys[pygame.K_RIGHT]:
            if current_setting == 0:
                if rotation_sensitivity < 5:
                    rotation_sensitivity += 1
            else:
                if moving_sensitivity < 5:
                    moving_sensitivity += 1
            pygame.time.delay(150)
        elif keys[pygame.K_LEFT]:
            if current_setting == 0:
                if rotation_sensitivity > 1:
                    rotation_sensitivity -= 1
            else:
                if moving_sensitivity > 1:
                    moving_sensitivity -= 1
            pygame.time.delay(150)

        if (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
            if current_setting == 0:
                current_setting = 1
            else:
                current_setting = 0
            pygame.time.delay(150)

        draw_settings()
