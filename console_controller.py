"""
ConsoleController: User interface for manually solving
Anne Hoy's problems from the console.
"""


# Copyright 2014, 2017 Dustin Wehr, Danny Heap, Bogdan Simion,
# Jacqueline Smith, Dan Zingaro
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


from toah_model import TOAHModel, IllegalMoveError
import sys


def move(model, origin, dest):
    """ Apply move from origin to destination in model.

    May raise an IllegalMoveError.

    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """

    try:
        model.move(origin, dest) # Moves the cheese.
        print(model) # Prints current state of the game
    except IllegalMoveError:
        raise IllegalMoveError


class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """

        self._model = TOAHModel(number_of_stools)
        self._num_cheeses = number_of_cheeses
        self._num_stools = number_of_stools

    def play_loop(self):
        """ Play Console-based game.

        @param ConsoleController self:
        @rtype: None

        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        """

        print("---------------------- Welcome to the Tour of Anne Hoy Game! -----------------------"
              "\nThe Goal: \nTo move all Cheeses to the Destination Stool.")
        u_input = input("-------------------------- Use the following controls: -------------------------- "
                        "\n\t1. Enter a Move ('M')"
                        "\n\t2. Quit Game('Q')")
        if u_input == 'M':
            print('=========================================')
            start = int(input("Enter start stool: "))
            dest = int(input("Enter dest stool: "))
            done = False
            while not done:
                try :
                    move(self._model, start, dest)  # makes the move!
                    done = True
                    print('------------------')
                except IllegalMoveError:
                    start = int(input("Error. Enter a new start: "))
                    dest = int(input("Enter a new dest: "))
        elif u_input == 'Q':
            sys.exit(0) # Exit the game.
        else:
            raise InvalidInputError


class InvalidInputError(Exception):
    '''An invalid input was entered'''

    pass

if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.

    done = False
    while not done:
        u_input = input("What would you like to do? [START] or [QUIT]: ")
        if u_input == 'START':
            num_stools = int(input("Great! How many stools are we using? (ie: 1,2,3, etc..): "))
            num_cheeses = int(input("Cool. Now, how many cheeses? "))
            console = ConsoleController(num_cheeses, num_stools)
            console.play_loop()  # Initiate the game.
            done = True
        else:
            print("Hope you enjoyed the game! Bye for now! .... Exiting....")
            sys.exit(0)
    print("Game over. Hope you enjoyed your stay! Bye for now!")
    sys.exit(0)

    # Leave lines below as they are, so you will know what python_ta checks.
    # You will need consolecontroller_pyta.txt in the same folder.
    import python_ta
    python_ta.check_all(config="consolecontroller_pyta.txt")
