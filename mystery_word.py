import random


def get_max_guesses():
    return 8


def print_no_guesses(string):
    print("You ran out of guesses! Better luck next time.")
    print("The mystery_word was {}.".format(string))


def print_guesses_remain(number, max_number):
    if number != 1:
        print("You have made {} bad guesses.".format(8 - max_number), end='')
        print("You have {} remaining guesses.".format(max_number))
    else:
        print("You have made {} bad guess.".format(8 - max_number), end='')
        print("You have {} remaining guesses.".format(max_number))


def exceeds_guess_count(number, max_number):
    return number >= max_number


def print_won_game():
    print("You did it! Great!")


def check_win(string, list_of_letters):
    for letter in string:
        if letter not in list_of_letters:
            return False
    return True


def update_game_state(string, list_of_letters):
    print(">> ", end="")
    for number in range(0, len(string)):
        if string[number] in list_of_letters:
            print("{} ".format(string[number]), end="")
        else:
            print("_ ", end="")
    print("<<")


def print_user_update(t_or_f):
    if t_or_f:
        print("Good guess! You found a letter!")
    else:
        print("Nice try... but that wasn't right.")


def update_after_guess(character, string, number):
    if character in string:
        return True, number
    else:
        return False, number + 1


def check_duplicate_guess(character, list_of_letters):
    return character in list_of_letters


def is_single_char(character, boolean, list_of_letters):
    if len(character) != 1 or not character.isalpha():
        print("Invalid input. Please try again.")
    else:
        if check_duplicate_guess(character, list_of_letters):
            print("You have already guessed the", end=' ')
            print("letter {}! Try again.".format(character))
        else:
            boolean = False
    return character, boolean


def request_guess(list_of_letters):
    loop_condition = True
    while loop_condition:
        user_input, loop_condition = is_single_char(
            input("Please guess a letter: ").upper(),
            loop_condition, list_of_letters)
    list_of_letters.append(user_input)
    return user_input, list_of_letters


def output_word_size(string):
    print("The mystery word is {} letters long.".format(len(string)))


def initial_game_output():
    print("Please select a difficulty: (e)asy, (n)ormal, or (h)ard.")
    user_input = input("> ")
    if user_input.lower() not in ["e", "easy", "n", "normal", "h", "hard"]:
        print("Invalid selection. Please try again.")
        initial_game_output()
    return user_input


def select_difficulty(string_or_char):
    bounds = [4, 6]
    if (string_or_char.lower() == "n" or
            string_or_char.lower() == "normal"):
        bounds = [6, 8]
    if (string_or_char.lower() == "h" or
            string_or_char.lower() == "hard"):
        bounds = [8, 1000]
    return bounds


def select_mystery_word(list_of_two_numbers):
    list_of_choices = []
    with open("/usr/share/dict/words") as f:
        for word in f:
            word = word.strip()
            if (len(word) >= list_of_two_numbers[0] and
                    len(word) <= list_of_two_numbers[1]):
                list_of_choices.append(word)
    return random.choice(list_of_choices).upper()


def welcome_output():
    print("\nWelcome to Mystery Word!!!")
    print("The object is to find the mystery word by guessing letters.")


def does_user_replay():
    print("\nWould you like to play again? (Y)es/(N)o")
    answer = input("> ").lower()
    if answer == "y" or answer == "yes":
        main()


def main():

    welcome_output()

    mystery_word = select_mystery_word(
                    select_difficulty(
                        initial_game_output()))

    guessed_letters, guess_count, max_guesses = [], 0, get_max_guesses()

    output_word_size(mystery_word)

    update_game_state(mystery_word, guessed_letters)

    while True:
        guess, guessed_letters = request_guess(guessed_letters)

        update_game_state(mystery_word, guessed_letters)

        return_boolean, guess_count = update_after_guess(
                guess, mystery_word, guess_count)

        print_user_update(return_boolean)

        if check_win(mystery_word, guessed_letters):
            print_won_game()
            break

        if exceeds_guess_count(guess_count, max_guesses):
            print_no_guesses()
            break

        print_guesses_remain(guess_count, max_guesses)

    does_user_replay()

if __name__ == '__main__':
    main()
