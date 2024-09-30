import pygame as pg
from matrix_function import *


class Object3d:
    def __init__(self, render):
        self.render = render
        self.vertexes = np.array(
            [
                (0, 0, 0, 1),
                (0, 1, 0, 1),
                (1, 1, 0, 1),
                (1, 0, 0, 1),
                (0, 0, 1, 1),
                (0, 1, 1, 1),
                (1, 1, 1, 1),
                (1, 0, 1, 1),
            ]
        )
        self.face = np.array(
            [
                (0, 1, 2, 3),
                (4, 5, 6, 7),
                (0, 4, 5, 1),
                (2, 3, 7, 6),
                (1, 2, 6, 5),
                (0, 3, 7, 4),
            ]
        )

    def translate(self, pos):
        self.vertexes = self.vertexes @ translate(pos)
