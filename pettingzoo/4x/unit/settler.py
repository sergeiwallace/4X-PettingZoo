import functools
import random
from copy import copy

import numpy as np
from gymnasium.spaces import Discrete, MultiDiscrete

from pettingzoo import ParallelEnv
from unit import Unit


class Settler(Unit):
    """The metadata holds environment constants.

    The "name" metadata allows the environment to be pretty printed.
    """

    metadata = {
        "name": "4x_grid_v0",
    }

    def __init__(self, civ, x_pos: int, y_pos: int) -> None:
        """The init method takes in environment arguments.

        Should define the following attributes:
        - escape x and y coordinates
        - guard x and y coordinates
        - prisoner x and y coordinates
        - timestamp
        - possible_agents

        Note: as of v1.18.1, the action_spaces and observation_spaces attributes are deprecated.
        Spaces should be defined in the action_space() and observation_space() methods.
        If these methods are not overridden, spaces will be inferred from self.observation_spaces/action_spaces, raising a warning.

        These attributes should not be changed after initialization.
        """

        super().__init__(civ, "settler", x_pos, y_pos)

    def settle(self, tile):
        tile.create_city()
        return



