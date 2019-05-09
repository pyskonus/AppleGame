import pygame
from math import sin, cos, radians
from random import randint
import A_settings
import A_backend
from A_backend import red_ulam, yellow_prime, green_lucky
lowlim_ulam = 0
lowlim_prime = 0
lowlim_lucky = 0

pygame.init()

# general objects declaration
Window_side = 600
Window = pygame.display.set_mode((Window_side, Window_side))
clock = pygame.time.Clock()


wall_x = Window_side
wall_y = 40
bow_x = 140
bow_y = 109
bow_x_coord = (Window_side - bow_x) // 2
bow_y_coord = Window_side - bow_y
arrow_x = 130
arrow_y = 67
angle = 0
triggered = False
apple_side = 100
lives = 5
points = 0
heart_side = 30

# loading images
bg = pygame.image.load('forest.jpg')
bg = pygame.transform.scale(bg, (Window_side, Window_side))
arrow_img = pygame.image.load('rotateable.png')
arrow_img = pygame.transform.scale(arrow_img, (arrow_x, arrow_y))
bows = [pygame.image.load('bow1.png'), pygame.image.load('bow2.png'),
pygame.image.load('bow3.png'), pygame.image.load('bow4.png'),
pygame.image.load('bow5.png'), pygame.image.load('bow6.png'),
pygame.image.load('bow7.png'), pygame.image.load('bow8.png'),
pygame.image.load('bow9.png'), pygame.image.load('bow10.png'),
pygame.image.load('bow11.png'), pygame.image.load('bow12.png')]
red_apple_img = pygame.transform.scale(pygame.image.load('red.png'), \
(apple_side, apple_side))
yellow_apple_img = pygame.transform.scale(pygame.image.load('yellow.png'), \
(apple_side, apple_side))
green_apple_img = pygame.transform.scale(pygame.image.load('green.png'), \
(apple_side, apple_side))
apple_img = pygame.transform.scale(pygame.image.load('colourful.png'), \
(apple_side, apple_side))
apples = [red_apple_img, yellow_apple_img, green_apple_img, apple_img]
hearts = [pygame.transform.scale(pygame.image.load('heart.png'), \
(heart_side, heart_side)), \
pygame.transform.scale(pygame.image.load('logo.png'), \
(heart_side, heart_side))]

# text
info_font = pygame.font.SysFont('Calibri', 22)
caption_font = pygame.font.SysFont('Calibri', 30, True)
final_font = pygame.font.SysFont('Calibri', 150, True)

class arrow():
    """
    This class represents a game object 'arrow'
    """

    global arrow_x

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.pace = 10
        self.side = arrow_x

    def draw(self, Win):
        # draw arrows
        Win.blit(pygame.transform.rotate(arrow_img, self.angle), \
        (self.x, self.y))

class target():
    """
    This class represents a game object 'apple'
    """
    global apple_side

    def __init__(self, x, y, race, caption):
        self.x = x
        self.y = y
        self.race = race
        self.side = apple_side
        self.pace = 0.002
        self.caption = caption

    def draw(self, Win):
        # draw apples
        if A_backend.mode:
            Win.blit(apples[3], (self.x, self.y))
            Win.blit(caption_font.render(self.caption, 1, (0, 0, 0)), \
            (self.x + 48 - len(self.caption) * 6, self.y + 47))
        else:
            Win.blit(apples[self.race], (self.x, self.y))
            Win.blit(caption_font.render(self.caption, 1, (0, 0, 0)), \
            (self.x + 48 - len(self.caption) * 6, self.y + 37))

frame = 0
fps = 48
sahaidak = []
apple_busket = []
run = True
iteration = 0
iterations_between_apples = 400
iterations_between_apples_lim = 60
apples_overall_count = 0

def apple_create():
    """
    This function creates game objects 'apple'
    """

    global Window_side, apple_side

    global lowlim_ulam, lowlim_prime, lowlim_lucky

    global iteration, iterations_between_apples, \
    iterations_between_apples_lim, apples_overall_count, apple_busket

    iteration += 1
    if iteration >= iterations_between_apples:
        iteration = 0
        number_sequence_choose = randint(0, 2)
        number_choose = randint(0, A_backend.diapason - 1)
        if number_sequence_choose == 0:
            apple_busket.append(target(randint(0, Window_side - apple_side), \
            -apple_side, 0, \
            str(red_ulam[lowlim_ulam + number_choose])))
            lowlim_ulam += 1
        elif number_sequence_choose == 1:
            apple_busket.append(target(randint(0, Window_side - apple_side), \
            -apple_side, 1, \
            str(yellow_prime[lowlim_prime + number_choose])))
            lowlim_prime += 1
        elif number_sequence_choose == 2:
            apple_busket.append(target(randint(0, Window_side - apple_side), \
            -apple_side, 2, \
            str(green_lucky[lowlim_lucky + number_choose])))
            lowlim_lucky += 1
        apples_overall_count += 1
    if apples_overall_count % 20 == 0 and \
    iterations_between_apples > iterations_between_apples_lim:
        iterations_between_apples -= 1

def drawings():
    ''' draws general objects in game scene '''

    global fps
    global frame
    global triggered
    global run

    if frame + 1 == 48:
        frame = 0
        sahaidak.append(arrow(bow_x_coord + 4, bow_y_coord, angle))


    Window.blit(bg, (0, 0))

    for apple in apple_busket:
        apple.draw(Window)

    if triggered:
        Window.blit(pygame.transform.rotate(bows[frame // 4], round(angle)), \
        (bow_x_coord, bow_y_coord))
        frame += 1
    else:
        Window.blit(pygame.transform.rotate(bows[0], round(angle)), \
        (bow_x_coord, bow_y_coord))

    for piu_piu in sahaidak:
        piu_piu.draw(Window)

    Window.blit(info_font.render("Points: " + str(points), \
    1, (0, 0, 230)), (5, 0))

    for i in range(lives):
        if A_backend.mode:
            Window.blit(hearts[1], (Window_side - heart_side * (i + 1), 0))
        else:
            Window.blit(hearts[0], (Window_side - heart_side * (i + 1), 0))

    if lives == 0:

        Window.fill((0, 0, 0))
        Window.blit(final_font.render(u"ЛОХ", 1, (255, 255, 255)), \
        (175, 250))
        pygame.display.update()
        pygame.time.wait(1000)
        run = False

    pygame.display.update()

def bow_control():
    # rotate and move the bow

    global triggered
    global frame
    global angle
    global bow_x, bow_y, bow_x_coord, bow_y_coord
    global Window_side

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and bow_x_coord > 0:
        bow_x_coord -= 1.5 * A_settings.moving_sensitivity
    elif keys[pygame.K_d] and bow_x_coord < Window_side - bow_x:
        bow_x_coord += 1.5 * A_settings.moving_sensitivity
    elif keys[pygame.K_s]:
        bow_x_coord = (Window_side - bow_x) // 2

    if keys[pygame.K_UP]:
        triggered = True
    else:
        frame = 0

    if keys[pygame.K_RIGHT] and angle > -85:
        angle -= 0.75 * A_settings.rotation_sensitivity
    elif keys[pygame.K_LEFT] and angle < 85:
        angle += 0.75 * A_settings.rotation_sensitivity
    elif keys[pygame.K_DOWN]:
        angle = 0

def frontend_main():
    """ main function of this module """

    global run
    global clock
    global sahaidak
    global Window_side
    global lives
    global points

    pygame.display.set_caption("Ulam")

    while run:
        clock.tick(fps)

        # this cycle is needed to quit the game
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                run = False

        apple_create()

        for pif_paf in sahaidak:
            if pif_paf.x < -99 or \
            pif_paf.x > Window_side + 99 or pif_paf.y < -99:
                sahaidak.pop(sahaidak.index(pif_paf))
            else:
                pif_paf.x -= pif_paf.pace * sin(radians(pif_paf.angle))
                pif_paf.y -= pif_paf.pace * cos(radians(pif_paf.angle))

            for apple in apple_busket:
                if A_backend.distance(pif_paf.x, pif_paf.y, apple.x, apple.y) <45:
                    apple_busket.pop(apple_busket.index(apple))
                    sahaidak.pop(sahaidak.index(pif_paf))
                    if apple.race == A_backend.current_target:
                        points += 1
                    else:
                        lives -= 1


        for apple in apple_busket:
            if apple.y > Window_side:
                apple_busket.pop(apple_busket.index(apple))
                if apple.race == A_backend.current_target:
                    lives -= 1
            else:
                apple.pace += 0.01
                apple.y += apple.pace

        bow_control()
        A_backend.mode_control()
        drawings()
