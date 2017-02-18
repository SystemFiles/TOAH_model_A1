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
    def less_than_4(model: 'TOAHModel', bad_stool = 0):
        '''Recursive call on tour if cheeses < 4'''
        #if bad_stool == 0:
        print(model)
        cheese = model.remove_top_cheese(0)
        first_empty = 0
        while model.get_top_cheese(first_empty) is not None:
            first_empty += 1
        while model.get_height_of_stool(0) != 0:
            model.add(cheese, 0)
            model.move(0, first_empty)
            cheese = model.remove_top_cheese(0)
            first_empty += 1
        model.add(cheese, 0)
        model.move(0, model.get_number_of_stools()-1)
        print(model)
        for i in range(1, model.get_number_of_cheeses()):
            model.move(model.get_number_of_cheeses()-i,
                       model.get_number_of_stools()-1)                
        '''else:
            print('else')
            cheese = model.remove_top_cheese(0)
            first_empty = 0
            while model.get_top_cheese(first_empty) is not None:
                first_empty += 1
            while model.get_height_of_stool(0) != 0:
                model.add(cheese, 0)
                model.move(0, first_empty)
                cheese = model.remove_top_cheese(0)
                first_empty += 1
            model.add(cheese, 0)
            model.move(0, model.get_number_of_stools()-1)
            for i in range(1, model.get_number_of_cheeses()):
                model.move(model.get_number_of_cheeses()-i,
                           model.get_number_of_stools()-1)               

            ==============
            model.move(2, 3)
            empty_stools = []
            for stool in range(model.get_number_of_stools()):
                if model.get_top_cheese(stool) is not None:
                    empty_stools.append(stool)
            for i in empty_stools:
                model.move(1, i-1)
            while not model.is_done():
                biggest_cheese = model.get_top_cheese(0)
                for i in range(model.get_number_of_stools()-1):
                    if (model.get_top_cheese(i) is not None) and \
                       (biggest_cheese is None or \
                       biggest_cheese.size < model.get_top_cheese(i).size):
                        biggest_cheese = model.get_top_cheese(i)
                model.move(model.get_cheese_location(biggest_cheese), 3)'''
                
            
    def equal_to_4(model: 'TOAHModel', bad_stool = 0):
        '''Recursive call on tour if cheeses == 4'''
        model.move(0, model.get_number_of_stools()-1)
        model.move(0, 1)
        model.move(model.get_number_of_stools()-1, 1)
        cheese = model.remove_top_cheese(0)
        i = 2
        while model.get_height_of_stool(0) != 0:
            model.add(cheese, 0)
            model.move(0, i)
            cheese = model.remove_top_cheese(0)
            i += 1
        model.add(cheese, 0)
        model.move(0, model.get_number_of_stools() - 1)
        model.move(model.get_number_of_stools() - 2,
                   model.get_number_of_stools() - 1)
        model.move(1, 0)
        model.move(1, model.get_number_of_stools()-1)
        model.move(0, model.get_number_of_stools()-1)

    def more_than_4(model: 'TOAHModel', bad_stool = 0):
        '''Recursive call on tour if cheeses == 4'''
        first_empty = 0
        while not model.get_top_cheese(first_empty) is None:
            first_empty += 1
        for i in range(1, model.get_number_of_stools()):
            model.move(0, model.get_number_of_stools()-i)
        for i in range(2, model.get_number_of_stools()):
            model.move(i, 1)
        if model.get_height_of_stool(0) > (model.get_number_of_stools() - 2):
            equal_to_4(model, first_empty)
        else:
            less_than_4(model, first_empty)
        
    #while not model.is_done():
    if model.get_number_of_cheeses() < model.get_number_of_stools():
        less_than_4(model)
    elif model.get_number_of_cheeses() == model.get_number_of_stools():
        equal_to_4(model)
    else:
        more_than_4(model)

    print(model)
    print(model.get_move_seq())

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
