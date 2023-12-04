import functools
import random
from copy import copy

import numpy as np
from gymnasium.spaces import Discrete, MultiDiscrete

from pettingzoo import ParallelEnv


class Unit:
    """The metadata holds environment constants.

    The "name" metadata allows the environment to be pretty printed.
    """
    unique_ids = set()
    metadata = {
        "name": "4x_grid_v0",
    }
    # TODO: Replace unique unit id logic
    id_counter = 1

    def __init__(self, x_pos: int, y_pos: int, unit_type: str):
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
        self.id = self.id_counter
        self.unique_ids.add(self.id)
        self.id_counter += 1
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.type = unit_type
