#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import math


class PhysObject:

    AU = 149.6e6 * 1000
    GRAVITY = 6.6742e-11
    SCALE = 150 / AU
    TIMESTEP = 86400  # number of seconds in one day

    def __init__(self, x, y, mass, radius, color):
        """
            self -> The Physical Object itself
            x -> A location of the physical object(further related as the object) on x-coordinate(2D)
            y -> A location of the object on y-coordinate(2D)
            mass -> The mass of the object in kilograms
            radius -> The radius of the object in meters
            color -> The color of the object to be shown on the screen
        """

        self.x = x
        self.y = y

        self.x_vel = 0
        self.y_vel = 0

        self.mass = mass
        self.radius = radius
        self.color = color

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        self.luminosity = None
        self.habitability = None

    def calculate_force(self, other):
        """
            self -> The object itself
            other -> The other object that is causing a force
        """

        distance_x = other.x - self.x
        distance_y = other.y - self.y

        total_distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = total_distance

        force = self.GRAVITY * self.mass * other.mass / total_distance \
            ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return (force_x, force_y)

    def update_position(self, physObjects):
        """
            self -> The object itself
            physObjects -> All the other objects that exist in the Solar System and causing force to the object(self)
        """

        total_fx = 0
        total_fy = 0

        for physObject in physObjects:
            if self != physObject:
                (fx, fy) = self.calculate_force(physObject)
                total_fx += fx
                total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        self.orbit.append((self.x, self.y))

    def draw_object(self, screen, FONT, WIDTH, HEIGHT):
        """
        self -> The object itself
        screen -> The screen on which the object will be drawn 
        FONT -> The font of the text of the distance of the objects to the sun
        WIDTH -> The width of the screen
        HEIGHT -> The height of the screen

        """

        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                (x, y) = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))
            pygame.draw.lines(screen, self.color, False, updated_points)

        pygame.draw.circle(screen, self.color, (x, y), self.radius)
        label_color = (255, 255, 255)
        distance_text = FONT.render(f"{round(self.distance_to_sun / self.AU, 3)}AU", 1, label_color)
        screen.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))