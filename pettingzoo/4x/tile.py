from dataclasses import dataclass
from city import City

class Tile:

    def __init__(self, x_pos, y_pos, terrain):
        self.position = Position(x_pos, y_pos)
        # TODO: Does terrain need it's own class / dataclass?
        self.terrain = terrain

    def create_city(self, civ):
        return

@dataclass
class Position:
    x: int
    y: int

