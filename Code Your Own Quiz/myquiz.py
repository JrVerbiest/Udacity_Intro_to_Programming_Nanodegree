"""
Author: J. Verbiest
# Last update: 17 December 2017
"""
import sys

def message():
    """
    Print message and exit python script
    :return: a message
    """
    print("Wrong level selected.")
    sys.exit()


def select_quote_and_answers(game_level,quotes):
    """
    This function will select the quote and the answers
    :param game_level: the game level
    :param quotes: the quotes
    :return: the quote and the answers given the selected game level
    """
    if game_level == "1" or game_level == "2" or game_level == "3":
        game_level = int(game_level)
        return quotes[game_level - 1]
    else:
        message()


def get_nmb_of_guesses(game_level):
    """
    Get the number of guesses that a user can try.
    :param game_level: the game level
    :return: the number of guesses that an user can try.
    """
    if game_level == "1":
        # In level 1 you can make 4 guesses
        return 4
    elif game_level == '2':
        # In level 2 you can make 3 guesses
        return 3
    elif game_level == '3':
        # In level 3 you can make 2 guesses
        return 2
    else:
        message()


def replace_word(the_quote, answers, word_nmb):
    """
    This function fill in the correct word in the quote
    :param the_quote: the quote
    :param answers: the answers for the given quote
    :param word_nmb: the location of the word to fill in
    :return: the quote with the word filled in
    """
    the_quote = the_quote.replace("__" + str(word_nmb) + "__", answers[word_nmb - 1])
    return the_quote


def calc_nmb_of_nmb_of_guesses(nmb_of_guesses):
    """
    Calculate number of guesses
    :param nmb_of_guesses: the number of guesses
    :return: number of guesses - 1
    """
    nmb_of_guesses = nmb_of_guesses - 1
    print(" You can try: " + str(nmb_of_guesses) + " times.")
    return nmb_of_guesses


def play(game_level,the_quote,answers):
    """
    This function checks if the guesses are correct.
    :param game_level: the game level
    :param the_quote: the quote given the selected game level
    :param answers: the answers given the selected game level
    :return: none
    """

    word_nmb = 1
    nmb_of_guesses = get_nmb_of_guesses(game_level)

    while word_nmb <= len(answers) and nmb_of_guesses !=0:
        print(the_quote+"\n You can try: "+str(nmb_of_guesses)+" times.")

        correct = 'FALSE'

        while nmb_of_guesses != 0 and correct != 'TRUE':
            word = input(" __"+str(word_nmb)+"__ = ")
            if word == answers[word_nmb-1]:
                the_quote = replace_word(the_quote, answers, word_nmb)
                nmb_of_guesses = get_nmb_of_guesses(game_level)
                correct = 'TRUE'
            else: nmb_of_guesses = calc_nmb_of_nmb_of_guesses(nmb_of_guesses)

        word_nmb = word_nmb+1

    if nmb_of_guesses == 0: print("\n Sorry game over.\n")
    else: print("Congratulations! \n" +the_quote)

#[EOF]