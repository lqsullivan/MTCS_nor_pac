# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 23:31:00 2018

@author: Sullysaurus
"""

import random
from abc import ABCMeta, abstractmethod

# Set up parent class that the movement policies inhereit from
"""
I don't understand the value of this besides abstract base classes making 
promises about certain things like printing prints and stuff and the parent
class guaranteeing a 'move' function in the class. I'll defer to kevinzhangftws
expertise in the matter :)
see https://www.python.org/dev/peps/pep-3119/ for more
"""
class policy(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def move(self, state):
        pass

# Set up random movement police
# Random move
class random_policy(policy):
    def move(self, state):
        """
        Asks game state for legal moves, randomly selects one and outputs it
        """
        return random.choice(self.legal_moves())
    
# 