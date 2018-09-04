
import networkx as nx
from tic_tac_toe import game_state
from play_policies import random_policy


class StateNode(object):
    def __init__(self, board):
        self.state = board
        self.parent = None
        self.child = None


def play_game(player_policies):
    """
    :param player_policies: List of policy classes for players X and O
     which determine how each player moves given a particular state. Each
     policy class should inherit from Policy.
    :return: Returns a NetworkX Graph object describing the game
    """
    game = game_state()

    # Keep track of the game tree
    G = nx.DiGraph()
    # Todo: use the newly implemented hashing method
    G.add_node(str(game))
    root = str(game)
    current = root

    plies = 0

    while game.winner() is None:
        for player_policy in player_policies:
            plies += 1
            print("\n================ ( Ply #{}. It is {}'s move. ) ================".format(plies, game.turn()))
            
            rp = random_policy()
            
            game.move(rp.move(game))

            previous = current
            G.add_node(str(game))
            current = str(game)
            G.add_edge(previous, current)

            if game.winner() is not None:
                break

    print('Game over. Winner is {}.'.format(game.winner()))

    return G, game.winner()
