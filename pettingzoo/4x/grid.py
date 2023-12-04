import functools
from copy import copy
import numpy as np
from gymnasium.spaces import Discrete, MultiDiscrete
from pettingzoo import ParallelEnv
from unit.settler import Settler
# import random
# from unit.archer import Archer
# from unit.builder import Builder
# from unit.warrior import Warrior
# from unit.scout import Scout


class Grid(ParallelEnv):
    """The metadata holds environment constants.

    The "name" metadata allows the environment to be pretty printed.
    """

    metadata = {
        "name": "4x_grid_env",
    }

    def __init__(self):
        """The init method takes in environment arguments.

        Should define the following attributes:
        - escape x and y coordinates
        - guard x and y coordinates
        - prisoner x and y coordinates
        - timestamp
        - possible_agents

        Note: as of v1.18.1, the action_spaces and observation_spaces attributes are deprecated. Spaces should be
        defined in the action_space() and observation_space() methods. If these methods are not overridden,
        spaces will be inferred from self.observation_spaces/action_spaces, raising a warning.

        These attributes should not be changed after initialization.
        """

        # TODO: create base class and specialized child classes for individual agents
        self.units = {"settler": {}, "builder": {}, "scout": {}, "warrior": {}, "archer": {}}
        self.x_length = 10
        self.y_length = 10
        self.escape_y = None
        self.escape_x = None
        self.guard_y = None
        self.guard_x = None
        self.prisoner_y = None
        self.prisoner_x = None
        self.time_step = None
        self.possible_agents = ["builder", "scout", "warrior", "archer"]

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
        self.time_step = 0
        settler = Settler(0, 0)
        self.units["settler"][settler.id] = settler
        # TODO: set settler position and other initial parameters
        # self.prisoner_x = 0
        # self.prisoner_y = 0
        #
        # self.guard_x = 6
        # self.guard_y = 6
        #
        # self.escape_x = random.randint(2, 5)
        # self.escape_y = random.randint(2, 5)

        # observations = {
        #     a: (
        #         self.prisoner_x + 7 * self.prisoner_y,
        #         self.guard_x + 7 * self.guard_y,
        #         self.escape_x + 7 * self.escape_y,
        #     )
        #     for a in self.agents
        # }
        #
        # # Get dummy info. Necessary for proper parallel_to_aec conversion
        # info = {a: {} for a in self.agents}
        #
        # return observations, info

    def step(self, actions):
        """
        Takes in an action for the current unit (specified by agent_selection).

        Needs to update:
        - prisoner x and y coordinates
        - guard x and y coordinates
        - terminations
        - truncations
        - rewards
        - timestamp
        - info

        And any internal state used by observe() or render()
        """
        # Execute actions
        # TODO: Create scenarios for unit tests such as:
        #  - settler creates city in highest value tile,
        #  - warrior defends city against barbarian
        #  - builder auto-builds building in appropriate tile
        #  - scout auto-explores new territory while avoiding danger
        #  - archer attacks enemy unit
        #  - etc.

        # prisoner_action = actions["prisoner"]
        # guard_action = actions["guard"]
        #
        # if prisoner_action == 0 and self.prisoner_x > 0:
        #     self.prisoner_x -= 1
        # elif prisoner_action == 1 and self.prisoner_x < 6:
        #     self.prisoner_x += 1
        # elif prisoner_action == 2 and self.prisoner_y > 0:
        #     self.prisoner_y -= 1
        # elif prisoner_action == 3 and self.prisoner_y < 6:
        #     self.prisoner_y += 1
        #
        # if guard_action == 0 and self.guard_x > 0:
        #     self.guard_x -= 1
        # elif guard_action == 1 and self.guard_x < 6:
        #     self.guard_x += 1
        # elif guard_action == 2 and self.guard_y > 0:
        #     self.guard_y -= 1
        # elif guard_action == 3 and self.guard_y < 6:
        #     self.guard_y += 1
        #
        # # Check termination conditions
        # terminations = {a: False for a in self.agents}
        # rewards = {a: 0 for a in self.agents}
        # if self.prisoner_x == self.guard_x and self.prisoner_y == self.guard_y:
        #     rewards = {"prisoner": -1, "guard": 1}
        #     terminations = {a: True for a in self.agents}
        #
        # elif self.prisoner_x == self.escape_x and self.prisoner_y == self.escape_y:
        #     rewards = {"prisoner": 1, "guard": -1}
        #     terminations = {a: True for a in self.agents}
        #
        # # Check truncation conditions (overwrites termination conditions)
        # truncations = {a: False for a in self.agents}
        # if self.time_step > 100:
        #     rewards = {"prisoner": 0, "guard": 0}
        #     truncations = {"prisoner": True, "guard": True}
        # self.time_step += 1
        #
        # # Get observations
        # observations = {
        #     a: (
        #         self.prisoner_x + 7 * self.prisoner_y,
        #         self.guard_x + 7 * self.guard_y,
        #         self.escape_x + 7 * self.escape_y,
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
        grid = np.full((self.x_length, self.y_length), " ")
        for unit_type, units in self.units.items():
            for unit_id in units:
                grid[units[unit_id].x_pos, units[unit_id].y_pos] = units[unit_type][:2].upper()
        print(f"{grid} \n")

    # Observation space should be defined here. lru_cache allows observation and action spaces to be memoized,
    # reducing clock cycles required to get each unit's space. If your spaces change over time, remove this line (
    # disable caching).
    @functools.lru_cache(maxsize=None)
    def observation_space(self, agent):
        # gymnasium spaces are defined and documented here: https://gymnasium.farama.org/api/spaces/
        return MultiDiscrete([self.x_length * self.y_length] * 3)

    # Action space should be defined here.
    # If your spaces change over time, remove this line (disable caching).
    @functools.lru_cache(maxsize=None)
    def action_space(self, agent):
        return Discrete(4)
