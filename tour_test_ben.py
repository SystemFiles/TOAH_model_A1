"""
functions to run TOAH tours.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "main":'
import time
from toah_model import TOAHModel


def tour_of_four_stools(model: 'TOAHModel', delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    """

    # Some variables to keep track of.
    num_c = model.get_number_of_cheeses()
    k = 0

    if num_c <= 0:
        return  # Nothing...No cheeses to move
    elif num_c == 1:
        model.move(0, 3)  # Move from first stool to last.
        if animate:
            time.sleep(delay_between_moves)  # Make delay.
            animate_console(model) # Animate
    else:
        if num_c > 2:
            k = 2
        else:
            k = 1
        # ^ We now have an optimal K..., I just can't figure out
        # the recursive call.


        if animate: # Animate recursive.
            time.sleep(delay_between_moves)  # Make delay.
            animate_console(model) # Animate


def animate_console(model: 'TOAHModel') -> None:
    '''Animates the state of the game automatically as
    tour solves the puzzle'''

    print("\n" * 100)  # Simulates the console being cleared..
    print(model)  # Displays the state of the game..

    return
if __name__ == '__main__':
    num_cheeses = 4
    delay_between_moves = 0.5
    console_animate = False

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheeses=num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())
    # Leave files below to see what python_ta checks.
    # File tour_pyta.txt must be in same folder
    import python_ta
    python_ta.check_all(config="tour_pyta.txt")
