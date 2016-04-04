import random
import operator



def print_no_guesses(list_of_words):
    print("You ran out of guesses! Better luck next time.")
    print("The mystery_word was {}.".format(random.choice(list_of_words)))

def print_guesses_remain(number, max_number):
    if number != 1:
        print("You have made {} bad guesses. You have {} remaining guesses.".format(number, max_number - number))
    else:
        print("You have made {} bad guess. You have {} remaining guesses.".format(number, max_number - number))

def exceeds_guess_count(number, max_number):
    return number >= max_number

def print_won_game():
    print("You did it! Great!")

def check_win(list_of_words, list_of_letters):
    if len(list_of_words) != 1:
        return False
    for letter in list_of_words.split():
        if letter not in list_of_letters:
            return False
    return True









# def update_after_guess(character, string_list, count_number):
#     branch_dictionary = {-1 : 0}
#     for word in string_list:
#         if character not in word:
#             branch_dictionary[-1] += 1
#         for number in range(len(word)):
#             branch_dictionary[number] = 0
#     for word in string_list:
#         if character == word[number]:
#             branch_dictionary[number] += 1
#     return_string_list = []
#     return_boolean = True
#     index_value = max(branch_dictionary.items(), key=operator.itemgetter(1))[0]
#     if index_value == -1:
#         count_number += 1
#         for word in string_list:
#             if character not in word:
#                 return_string_list.append(word)
#                 return_boolean = False
#     else:
#         for word in string_list:
#             if character == word[index_value]:
#                 return_string_list.append(word)
#     return return_string_list, count_number, return_boolean, index_value



# def is_single_char(character, letter_list):
#     if len(character) != 1 or not character.isalpha():
#         return False, 0
#     else:
#         if check_duplicate_guess(character, list_of_letters):
#             print("You have already guessed the letter {}! Try again.".format(character))
#         else:
#             boolean = False
#     return character, boolean





# def update_game_state(string, list_of_letters, character, index_number):
#     print(">> ", end="")
#     for char in string:
#
#     for number in range(0, len(string)):
#         if string[number] in list_of_letters:
#             print("{} ".format(string[number]), end="")
#         else:
#             print("_ ", end="")
#     print("<<")

# def set_word_length(list_of_words):
#     if list_of_words:
#         return len(list_of_words[0])
#     return -1


def does_user_replay():
    print("\nWould you like to play again? (Y)es/(N)o")
    answer = input("> ").lower()
    if answer == "y" or answer == "yes":
        main()



def print_user_update(input_boolean):
    if input_boolean:
        print("Good guess! You found a letter!")
    else:
        print("Nice try... but that wasn't right.")





def update_board(character, index_number, game_string):
    print(game_string)
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

def reselect_mystery_word_list(guess_char, word_list, good_letters, bad_letters):
    longest_set_index = separate_list_lengths(guess_char, word_list)
    if longest_set_index == -1:
        bad_letters.append(guess_char)
        print(bad_letters)
    else:
        good_letters.append(guess_char)
        print(good_letters)
    new_word_list = []
    for word in word_list:
        remove_test = False
        for char in word:
            if char in bad_letters:
                remove_test = True
        if remove_test == False:
            new_word_list.append(word)

    for word in word_list:
        remove_test = True
        for char in word:
            if char in good_letters:
                remove_test = False
        if remove_test == False:
            new_word_list.append(word)

    # for word in word_list:
    #     if match_index_to_guess(guess_char, word) != longest_set_index:
    #             word_list.remove(word)
    print(new_word_list)
    return new_word_list, good_letters, bad_letters, longest_set_index

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
    return 2
    #return random.randint(list_of_two_numbers[0], list_of_two_numbers[1])

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
        mystery_word_list, good_letters, bad_letters, guess_position = reselect_mystery_word_list(guess, mystery_word_list, good_letters, bad_letters)
        game_string = update_board(guess, guess_position, game_string)
        output_game_state(mystery_word_length, game_string)

        # if "_" not in game_string:
        #     print("you win")
        #     break
        # if len(guessed_letters) >= max_guesses:
        #     print("you lose")
        #     break



    # while True:
    #
    #     guess, guessed_letters = request_guess(guessed_letters) #requires user input; returns the guess and updates the guess list
    #
    #     mystery_word_list, guess_count, correct_or_not, letter_location = update_after_guess(guess, mystery_word_list, guess_count) #TESTABLE
    #
    #     update_game_state(mystery_word_list[0], guessed_letters, guess, letter_location) #no return; print game 'board'
    #
    #     print_user_update(correct_or_not) #no return; print based on update_after_guess
    #
    #
    #     if check_win(mystery_word_list, guessed_letters): #TESTABLE
    #         print_won_game() #no return; prints win condition
    #         break
    #
    #     if exceeds_guess_count(guess_count, max_guesses): #TESTABLE
    #         print_no_guesses(mystery_word_list) #no return; prints loss condition
    #         break
    #
    #     print_guesses_remain(guess_count, max_guesses) #no return; prints continue condition

    does_user_replay() #no return; restarts main on user input

if __name__ == '__main__':
    main()
