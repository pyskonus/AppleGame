import pygame
import A_frontend

mode = False
current_target = 0


def ulam_numbers(elements):
    """
    (int) -> list
    Precondition: elements > 2
    This function returns a list of ulam numbers of given length.
    >>> ulam_numbers(5)
    [1, 2, 3, 4, 6]
    >>> ulam_numbers(8)
    [1, 2, 3, 4, 6, 8, 11, 13]
    """
    result = [1, 2]
    candidates = []
    for iterator in range(elements - 2):
        for i in range(len(result)):
            for j in range(i + 1, len(result)):
                candidates.append(result[i] + result[j])
        candidates.sort()
        for number in candidates:
            if number > result[-1] and candidates.count(number) == 1:
                result.append(number)
                candidates = []
                break

    return result


def primecheck(integer):
    """
    (int) -> bool
    Precondition: integer > 0
    This function checks if a given number is prime.
    >>> primecheck(3)
    True
    >>> primecheck(12)
    False
    """
    for divider in range(2, round(integer ** 0.5) + 1):
        if integer % divider == 0:
            return False
    return True


def prime_numbers(elements):
    """
    (int) -> list
    Precondition: elements > 0
    Returns a list of prime numbers of a given length.
    >>> prime_numbers(3)
    [2, 3, 5]
    >>> prime_numbers(6)
    [2, 3, 5, 7, 11, 13]
    """
    result = []
    current_num = 2
    while len(result) < elements:
        if primecheck(current_num):
            result.append(current_num)
        current_num += 1

    return result


def lucky_numbers(elements):
    """
    (int) -> list
    Precondition: elements > 0
    This function returns a list of lucky numbers that are less than
    a given number.
    >>> lucky_numbers(3)
    [1]
    >>> lucky_numbers(17)
    [1, 3, 7, 9, 11, 15]
    """
    result = []
    for i in range(1, elements):
        result.append(i)

    for element in result:
        if element % 2 == 0:
            result.pop(result.index(element))

    for item in result:
        if (result.index(item) + 1) % 3 == 0:
            result.pop(result.index(item))

    for item in result:
        if (result.index(item) + 1) % 7 == 0:
            result.pop(result.index(item))

    return result


def distance(x1, y1, x2, y2):
    """
    (number, number, number, number) -> int
    This function returns a distance between two given points.
    >>> distance(0, 0, 3, 4)
    5
    >>> distance(0, 0, 12, 5)
    13
    """
    return round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)

red_ulam = ulam_numbers(200)
yellow_prime = prime_numbers(200)
green_lucky = lucky_numbers(609)

diapason = 5


def mode_control():
    # switch modes
    global mode
    global current_target

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        A_frontend.run = False

    if keys[pygame.K_a] and keys[pygame.K_p] and keys[pygame.K_l] and \
    keys[pygame.K_e]:
        mode = True
    elif keys[pygame.K_b] and keys[pygame.K_a] and keys[pygame.K_c] and \
    keys[pygame.K_k]:
        mode = False

    if keys[pygame.K_1]:
        current_target = 0
        pygame.display.set_caption("Ulam")
    elif keys[pygame.K_2]:
        current_target = 1
        pygame.display.set_caption("Prime")
    elif keys[pygame.K_3]:
        current_target = 2
        pygame.display.set_caption("Lucky")
