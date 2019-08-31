"""
Project: fill in the blanks
Author: J. Verbiest
Last update: 17 December 2017
Note: written in Python 3
"""

import myquiz as mq

# The quotes
quote = [[[" __1__ is like a __2__ of __3__, you never know what you gonna get. \n Forrest __4__"],
          ['Life','box','chocolates','Gump']],
         [[" Your __1__ is limited, so don't waste it living someone else's __2__.\n"
           " Don't be trapped by dogma - which is living with the results of other __3__'s\n"
           " thinking. Don't let the noise of others' opinions drown out your own inner voice.\n"
           " And most important, have the __4__ to follow your heart and intuition.\nSteve Jobs."],
          ['time',"life","people","courage"]],
         [[" Stay __1__. Stay __2__. __3__ __4__"],
          ['hungry', "foolish","Steve","Jobs"]]]

# Start program
print(" Welcome.")
print(" You can choose a game level: 1, 2 or 3.\n")
game_level = input(" Which level to you like to play: ")

quote_and_answers = mq.select_quote_and_answers(game_level,quote)
mq.play(game_level,quote_and_answers[0][0],quote_and_answers[1])

#[EOF]