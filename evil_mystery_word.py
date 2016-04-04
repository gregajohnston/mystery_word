import random
import operator


def print_no_guesses(list_of_words):
    print("You ran out of guesses! Better luck next time.")
    print("The mystery_word was {}.".format(random.choice(list_of_words)))

def print_guesses_remain(max_number):
    if max_number != 1:
        print("You have made {} bad guesses. You have {} remaining guesses.".format(8 - max_number, max_number))
    else:
        print("You have made {} bad guess. You have {} remaining guesses.".format(8 - max_number, max_number))

def exceeds_guess_count(max_number):
    return max_number <= 0

def print_won_game():
    print("You did it! Great!")

def does_user_replay():
    print("\nWould you like to play again? (Y)es/(N)o")
    answer = input("> ").lower()
    if answer == "y" or answer == "yes":
        main()

def update_board(character, index_number, game_string):
    if index_number == -1:
        return game_string
    else:
        game_list = list(game_string)
        game_list[index_number] = character
        return "".join(game_list)

def match_index_to_guess(character, string):
    try:
        return string.index(character)
    except ValueError:
        return -1

def separate_list_lengths(guess_char, word_list):
    selection_dict = {-1 : 0}
    for number in range(len(word_list[0])):
        selection_dict[number] = 0
    for word in word_list:
        if guess_char not in word:
            selection_dict[-1] += 1
        else:
            for index, character in enumerate(word):
                if guess_char == character:
                    selection_dict[index] += 1
    return max(selection_dict, key=lambda i: selection_dict[i])

def update_bad_list(bad_letters, word_list):
    new_word_list = []
    for word in word_list:
        remove_test = False
        for char in word:
            if char in bad_letters:
                remove_test = True
        if remove_test != True:
            new_word_list.append(word)
    return new_word_list

def update_good_list(guess_char, word_list, index):
    new_word_list = []
    for word in word_list:
        if match_index_to_guess(guess_char, word) == index:
            new_word_list.append(word)
    return new_word_list

def reselect_mystery_word_list(guess_char, word_list, good_letters, bad_letters, max_number):
    longest_set_index = separate_list_lengths(guess_char, word_list)
    if longest_set_index != -1:
        good_letters.append(guess_char)
        word_list = update_good_list(guess_char, word_list, longest_set_index)
    else:
        bad_letters.append(guess_char)
        max_number -= 1
        word_list = update_bad_list(bad_letters, word_list)
    return word_list, good_letters, bad_letters, longest_set_index, max_number

def request_guess(g_list, b_list):
    print("Please guess a letter:")
    letter_list = g_list + b_list
    while True:
        user_input = input("> ").upper()
        if len(user_input) == 1 and user_input.isalpha() and user_input not in letter_list:
            break
        elif user_input in letter_list:
            print("You have already guessed {}! Please try again.".format(user_input))
        else:
            print("{} is not a valid input. Please try again.".format(user_input))
    return user_input.upper()

def create_board(length_of_word):
    return_string = ""
    while length_of_word:
        return_string += "_"
        length_of_word -= 1
    return return_string

def get_max_guesses():
    return 8

def initialize_mystery_word_list(length_number):
    list_of_choices = []
    with open("/usr/share/dict/words") as f:
        for word in f:
            word = word.strip()
            if len(word) == length_number and word.upper() not in list_of_choices:
                list_of_choices.append(word.upper())
    return list_of_choices

def output_game_state(number, string):
    if len(string) == 0:
        print("\nThe mystery word is {} letters long.".format(number))
        print("_ " * number)
    for character in string:
        print("{} ".format(character), end="")
    print("")

def select_word_length(list_of_two_numbers):
    return random.randint(list_of_two_numbers[0], list_of_two_numbers[1])

def select_difficulty(input_str_or_char):
    bounds = [4, 6]
    if (input_str_or_char == "n" or
        input_str_or_char == "normal"):
        bounds = [6, 8]
    if (input_str_or_char == "h" or
        input_str_or_char == "hard"):
        bounds = [8, 45]
    return bounds

def request_difficulty():
    print("Please select a difficulty: (e)asy, (n)ormal, or (h)ard.")
    while True:
        user_input = input("> ").lower()
        if user_input in ["e", "easy", "n", "normal", "h", "hard"]:
            break
        print("Invalid selection. Please try again.")
    return user_input

def welcome_output():
    print("\nWelcome to Mystery Word!!!")
    print("The object is to find the mystery word by guessing letters.")

def main():
    welcome_output()

    mystery_word_length = select_word_length(select_difficulty(request_difficulty()))
    mystery_word_list = initialize_mystery_word_list(mystery_word_length)
    game_string, good_letters, bad_letters, max_guesses = "", [], [], get_max_guesses()
    output_game_state(mystery_word_length, game_string)
    game_string = create_board(mystery_word_length)

    while True:
        guess = request_guess(good_letters, bad_letters)
        mystery_word_list, good_letters, bad_letters, guess_position, max_guesses = \
            reselect_mystery_word_list(guess, mystery_word_list, good_letters, bad_letters, max_guesses)
        game_string = update_board(guess, guess_position, game_string)
        output_game_state(mystery_word_length, game_string)
        if "_" not in game_string:
             print_won_game()
             break
        if exceeds_guess_count(max_guesses):
            print_no_guesses(mystery_word_list)
            break
        else:
            print_guesses_remain(max_guesses)

    does_user_replay()

if __name__ == '__main__':
    main()
