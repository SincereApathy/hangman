
import random

def print_board(incorrect_guess_count):
    board = list()

    board.append("|    |    |")
    if incorrect_guess_count >= 1:
        board.append("|    O    |")

    if incorrect_guess_count == 2:
        board.append("|    |    |")
    elif incorrect_guess_count == 3:
        board.append("|    |    |")
        board.append("|   /     |")
    elif incorrect_guess_count == 4:
        board.append("|    |    |")
        board.append("|   / \   |")
    elif incorrect_guess_count == 5:
        board.append("|   /|    |")
        board.append("|   / \   |")
    elif incorrect_guess_count == 6:
        board.append("|   /|\   |")
        board.append("|   / \   |")
        board.append("|GAME OVER|")

    for line in board:
        print(line)


def get_random_word():
    word_list = ["LASAGNA","FISHING","HUNTING","PROGRAM","SYSTEM",
                 "RANDOM","ALGEBRA","PHYSICS","CALCULUS","RACECAR",
                 "DISEASE","POPCORN","ETHANOL","ELEPHANT","FINALLY"]
    rand_number = random.randrange(0,len(word_list))

    return word_list[rand_number]




game_in_progress = True



while game_in_progress:
    magic_word = get_random_word()
    incorrect_picks = 0
    board = ["_"] * len(magic_word)
    guessed_letters = list()
    msg = "Guess a letter: "
    print("Welcome to Hangman!")
    
    while incorrect_picks < 7:
        if incorrect_picks != 6:
            print("")
            print("Current Word: " + " ".join(board))
            print("Guessed letters: " + " ".join(guessed_letters))
            print_board(incorrect_picks)
        else:
            print("")
            print_board(incorrect_picks)
            print("The word was {0}".format(magic_word))
            break
        
        cur_letter = input(msg)
        guessed_letters.append(cur_letter)
        
        if cur_letter in magic_word:
            for i, char in enumerate(magic_word):
                if char == cur_letter:
                    board[i] = cur_letter
        else:
            print("Sorry, the word does not contain {0}.".format(cur_letter))
            incorrect_picks += 1

        if "_" not in board:
            print("Congrats you win! The word was {0}.".format(magic_word))
            break



    


    
    
