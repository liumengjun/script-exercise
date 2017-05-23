# -----------------
# User Instructions
#
# Write a function, play_pig, that takes two strategy functions as input,
# plays a game of pig between the two strategies, and returns the winning
# strategy.
#

import random
from functools import lru_cache

possible_moves = ['roll', 'hold']
other = {1: 0, 0: 1}
goal = 50


def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    (p, me, you, pending) = state
    return (other[p], you, me + pending, 0)


def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    (p, me, you, pending) = state
    if d == 1:
        return (other[p], you, me + 1, 0)  # pig out; other player's turn
    else:
        return (p, me, you, pending + d)  # accumulate die roll in pending


def clueless(state):
    "A strategy that ignores the state and chooses at random from possible moves."
    return random.choice(possible_moves)


def hold_at(x):
    """Return a strategy that holds if and only if 
    pending >= x or player reaches goal."""

    def strategy(state):
        (p, me, you, pending) = state
        return 'hold' if (pending >= x or me + pending >= goal) else 'roll'

    strategy.__name__ = 'hold_at(%d)' % x
    return strategy


def dierolls():
    "Generate die rolls."
    while True:
        yield random.randint(1, 6)


def play_pig(A, B, rolls=dierolls()):
    """Play a game of pig between two players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player."""

    strategies = [A, B]
    state = (0, 0, 0, 0)
    while True:
        (p, me, you, pending) = state
        if me >= goal:
            print(state)
            return strategies[p]
        elif you >= goal:
            print(state)
            return strategies[other[p]]
        else:
            action = strategies[p](state)
            if action == 'hold':
                state = hold(state)
            elif action == 'roll':
                state = roll(state, next(rolls))
            else:
                return strategies[other[p]]


def always_roll(state):
    return 'roll'


def always_hold(state):
    return 'hold'


def Q_pig(state, action, Pwin):
    "The expected value of choosing action in state."
    if action == 'hold':
        return 1 - Pwin(hold(state))
    if action == 'roll':
        return (1 - Pwin(roll(state, 1))
                + sum(Pwin(roll(state, d)) for d in (2, 3, 4, 5, 6))) / 6.
    raise ValueError


def best_action(state, actions, Q, U):
    "Return the optimal action for a state, given U."

    def EU(action): return Q(state, action, U)

    return max(actions(state), key=EU)


def pig_actions(state):
    "The legal actions from a state."
    _, _, _, pending = state
    return ['roll', 'hold'] if pending else ['roll']


@lru_cache(maxsize=None)
def Pwin(state):
    """The utility of a state; here just the probability that an optimal player
    whose turn it is to move can win from the current state."""
    # Assumes opponent also plays with optimal strategy.
    (p, me, you, pending) = state
    if me + pending >= goal:
        return 1
    elif you >= goal:
        return 0
    else:
        return max(Q_pig(state, action, Pwin)
                   for action in pig_actions(state))


def Pwin2(state):
    """The utility of a state; here just the probability that an optimal player
    whose turn it is to move can win from the current state."""
    _, me, you, pending = state
    return Pwin3(me, you, pending)


@lru_cache(maxsize=None)
def Pwin3(me, you, pending):
    "the probability of winning for player with score me to you, and pending."
    # it doesn't calc opponent's state so it's faster than Pwin
    if me + pending >= goal:
        return 1
    elif you >= goal:
        return 0
    else:
        Proll = (1 - Pwin3(you, me + 1, 0) +
                 sum(Pwin3(me, you, pending + d) for d in (2, 3, 4, 5, 6))) / 6.
        return (Proll if not pending else
                max(Proll, 1 - Pwin3(you, me + pending, 0)))


@lru_cache(maxsize=None)
def win_diff(state):
    "The utility of a state: here the winning differential (pos or neg)."
    (p, me, you, pending) = state
    if me + pending >= goal or you >= goal:
        return (me + pending - you)
    else:
        return max(Q_pig(state, action, win_diff)
                   for action in pig_actions(state))


def max_diffs(state):
    """A strategy that maximizes the expected difference between my final score
    and my opponent's."""
    return best_action(state, pig_actions, Q_pig, win_diff)


def max_wins(state):
    "The optimal pig strategy chooses an action with the highest win probability."
    return best_action(state, pig_actions, Q_pig, Pwin)


def max_wins2(state):
    "The optimal pig strategy chooses an action with the highest win probability."
    return best_action(state, pig_actions, Q_pig, Pwin2)


def test():
    # for _ in range(10):
    #     winner = play_pig(always_hold, always_roll)
    #     assert winner.__name__ == 'always_roll'

    # A, B = hold_at(50), clueless
    # # rolls = iter([6, 6, 6, 6, 6, 6, 6, 6, 2])
    # assert play_pig(A, B) == A

    # def dup_op(state):
    #     return hold_at(50)(state)
    # A, B = dup_op, hold_at(50)
    # print(play_pig(A, B))

    # A, B = max_wins, max_diffs
    # print(play_pig(A, B))
    # # print(Pwin.cache_info())

    A, B = max_wins2, max_diffs
    print(play_pig(A, B))
    # print(Pwin3.cache_info())

    return 'test passes'


print(test())
