import pygame
import math
from astro.physical_object import PhysObject
from pygameHelper.button import Button

WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
GREEN = (3, 75, 3)
DARK_GREY = (80, 78, 81)
LAVENDER = (210, 207, 218)
BROWN_YELLOW = (204, 153, 102)
LIGHT_BLUE = (209,231,231)
ONEMORE_BLUE = (75, 112, 121)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")
FONT = pygame.font.SysFont("comicsans", 16)
add_button = Button(50, 50, pygame.image.load('icons/add-button.png').convert_alpha())

if __name__ == "__main__":
    done = False
    clock = pygame.time.Clock()

    sun = PhysObject(0, 0, 1.98892 * 10**30, 30, YELLOW)
    sun.sun = True

    mercury = PhysObject(0.387 * PhysObject.AU, 0, 3.3 * 10**23, 8, DARK_GREY)
    mercury.y_vel = -47.4 * 1000

    venus = PhysObject(0.723 * PhysObject.AU, 0, 4.8685 * 10**24, 14, WHITE)
    venus.y_vel = -35.02 * 1000

    earth = PhysObject(-1 * PhysObject.AU, 0, 5.9742 * 10**24, 16, BLUE)
    earth.y_vel = 29.783 * 1000

    mars = PhysObject(-1.524 * PhysObject.AU, 0, 6.39 * 10**23, 12, RED)
    mars.y_vel = 24.077 * 1000

    jupyter = PhysObject(5.2 * PhysObject.AU, 0, 1.898 * 10**27, 45, LAVENDER)
    jupyter.y_vel = 13.06 * 1000

    saturn = PhysObject(-9.5 * PhysObject.AU, 0,5.683 * 10**26, 35, BROWN_YELLOW)
    saturn.y_vel = 9.68 * 1000

    uranus = PhysObject(19.8 * PhysObject.AU, 0, 6.39 * 10**23, 12, LIGHT_BLUE)
    uranus.y_vel = 6.8 * 1000

    neptune = PhysObject(-30 * PhysObject.AU, 0, 1.024 * 10**26, 12, RED)
    neptune.y_vel = 5.43 * 1000

    physObjects = [sun, mercury, venus, earth, mars, jupyter, saturn, uranus, neptune]

    while not done:
        clock.tick(60)
        screen.fill((29, 41, 81)) # color code of space blue

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if add_button.draw(screen):
                    new_mass = eval(input("Input the mass of the planet as scientific notation(ex: 5.683 * 10**26): "))
                    new_distance = float(input("Enter its distance from the Sun in AU: ")) * physObject.AU
                    new_velocity = float(input("Enter the velocity in kilometers: ")) * 1000
                    new_object = PhysObject(new_distance, 0, new_mass, 15, BLACK)
                    new_object.y_vel = new_velocity
                    physObjects.append(new_object)


        for physObject in physObjects:
            physObject.update_position(physObjects)
            physObject.draw_object(screen, FONT, WIDTH, HEIGHT)
            
        pygame.display.update()

    pygame.display.quit()