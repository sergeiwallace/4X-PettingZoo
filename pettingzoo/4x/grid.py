import functools
from copy import copy
import numpy as np
from gymnasium.spaces import Discrete, MultiDiscrete
from pettingzoo import ParallelEnv
from civilization import Civilization
from unit.settler import Settler
from unit.warrior import Warrior

# from unit.archer import Archer
# from unit.builder import Builder
# from unit.scout import Scout
# import random

# NOTE: Use tutorial2_adding_game_logic.py and tutorial3_action_masking.py files as references


class Grid(ParallelEnv):
    metadata = {
        "name": "4x_grid_env",
    }

    def __init__(self):
        # TODO: create base class and specialized child classes for individual agents
        self.civilizations = {}
        # self.units = {"settler": {}, "builder": {}, "scout": {}, "warrior": {}, "archer": {}}
        self.possible_agents = ["settler", "builder", "scout", "warrior", "archer"]
        self.grid_width = 10
        self.grid_length = 10
        self.time_step = None

    def reset(self, seed=None, options=None):
        """ Reset set the environment to a starting point.

        It needs to initialize the following attributes:
        - agents
        - timestamp
        - prisoner x and y coordinates
        - guard x and y coordinates
        - escape x and y coordinates
        - observation
        - info

        And must set up the environment so that render(), step(), and observe() can be called without issues.
        """
        self.agents = copy(self.possible_agents)
        civ_names = ["Troy", "Greece"]
        # TODO: Generate start positions for civs with guaranteed number of tiles separating them
        for civ_name in civ_names:
            civ = Civilization(civ_name)
            self.civilizations[civ_name] = civ
            settler = Settler(self.civilizations[civ_name], 0, 0)
            # TODO: Should units be member variable of each civ or all in one dictionary
            self.civilizations[civ_name].units["settler"][settler.id] = settler
            warrior = Warrior(self.civilizations[civ_name], 0, 0)
            self.civilizations[civ_name].units["warrior"][warrior.id] = warrior

        self.time_step = 0
        # TODO: set settler position and other initial parameters

        # TODO: Create/collection observations
        # observations = {
        #     a: (
        #     )
        #     for a in self.agents
        # }
        #
        # # Get dummy info. Necessary for proper parallel_to_aec conversion
        # info = {a: {} for a in self.agents}
        #
        # return observations, info

    def step(self, actions):
        # Execute actions
        # TODO: Create scenarios for unit tests such as:
        #  - settler creates city in highest value tile,
        #  - warrior defends city against barbarian
        #  - builder auto-builds building in appropriate tile
        #  - scout auto-explores new territory while avoiding danger
        #  - archer attacks enemy unit
        #  - etc.

        # TODO: Should actions be stored with each unit?
        prisoner_action = actions["settler"]
        guard_action = actions["warrior"]

        # TODO: Add termination conditions i.e. civilization has no remaining cities or settlers
        # # Check termination conditions
        #
        # # Get observations
        # observations = {
        #     a: (
        #     )
        #     for a in self.agents
        # }
        #
        # # Get dummy info (not used in this example)
        # info = {a: {} for a in self.agents}
        #
        # if any(terminations.values()) or all(truncations.values()):
        #     self.agents = []
        #
        # return observations, rewards, terminations, truncations, info

    def render(self):
        """
        Renders the environment
        """
        grid = np.full((self.grid_length, self.grid_width), " ")
        for civ_name in self.civilizations.keys():
            for unit_type, units in self.civilizations[civ_name].units.items():
                for unit_id in units:
                    grid[units[unit_id].x_pos, units[unit_id].y_pos] = units[unit_type][:2].upper()
        print(f"{grid} \n")

    # Observation space should be defined here. lru_cache allows observation and action spaces to be memoized,
    # reducing clock cycles required to get each unit's space. If your spaces change over time, remove this line (
    # disable caching).
    @functools.lru_cache(maxsize=None)
    def observation_space(self, agent):
        # gymnasium spaces are defined and documented here: https://gymnasium.farama.org/api/spaces/
        return MultiDiscrete([self.grid_length * self.grid_width] * 3)

    # Action space should be defined here.
    # If your spaces change over time, remove this line (disable caching).
    @functools.lru_cache(maxsize=None)
    def action_space(self, agent):
        return Discrete(4)

    # FIXME: move action methods to relevant unit class
    def raze_city(self, city):
        return

    def transfer_city(self, civ, city):
        return

    def create_building(self, civ, tile):
        return

    def raze_building(self, building):
        return




