sentences = [ # Game has 3 or more levels and each level contains 4 or more blanks to fill in
"_1_ is a programming language named for Monty Python's Flying Circus.\nA _2_ is an immutable list of characters surrounded by quotes.\nA _3_ is an unordered collection of items of any type while a\n_4_ is an ordered collection of a single type.",
"A _1_ is an associative array that can contain any Python _2_ type.\nThe print() function and integer division are key differences between Python _3_ and _4_",
"Python supports _1_ programming with classes and multiple _2_.\nPython _3_ are defined by creating a function and inheriting from a _4_\neg. variable = Class(parameters)"]

answers = [['Python','string','list','array'],['dictionary', 'data', '2', '3'],['object-oriented', 'inheritance','objects','class']]

sentence_with_blanks = ""

def level_selector(): 
    """User selected level is printed for user, along with the appropriate sentence
    Args:
        None
    Returns:
        string: Returns position of level within sentences array
    """
    level = input("Please select a level to begin at: (1) Easy (2) Medium or (3) Hard. Type 'Q' to quit\n>> ")
    while True:
        try:
            level = int(level)
            if level == 1:
                print('Level is: Easy')
                return level - 1
            elif level == 2:
                print('Level is: Medium')
                return level - 1
            elif level == 3:
                print('Level is: Hard')
                return level - 1
            else:
                print("Please enter a valid number") # catches inputs that except doesn't
                level_selector()
        except ValueError: # catches any incorrect inputs not caught above
            print("Invalid input. Please enter a whole number.")
            level_selector()

def sentence_play(level, i):
    """Allows user to enter selection and validates user response
    Args:
        level (int): level selected by user
        i (int): blank number within sentence
    Returns:
        Does not return anything
    """
    if not i:
        i = 1
    else:    
        while i < 4:
            if i == 1:
                blank = 'first'
            elif i == 2:
                blank = 'second'
            elif i == 3:
                blank = 'third'
            else:
                blank = 'fourth'
            blank_input = input("What should be substituted in for the " + blank + " blank?\n>> ")

            # When player guesses correctly, new prompt shows with correct answer in the
            # previous blank and a new prompt for the next blank
            if correct_answer(level, i, blank_input):
                display_filled_sentence(level, i, blank_input)
                print("Nice work! You got that one right")
                i += 1
                if i > 4:
                    print("Great! You got them all right")
                    play_game()
            else: # When player guesses incorrectly, they are prompted to try again
                print('Not quite. Try again.')
                sentence_play(blank)
    play_game()

def correct_answer(level, blank_number, answer):
    """Validates user response against answers array
    Args:
        level (int): level selected by user
        blank_number (int): position of blank within sentence
        answer (string): input provided by user in sentence_play()
    Returns:
        boolean: Returns true if answer is correct
    """
    if str(answer) == answers[level - 1][blank_number - 1]:
        return True
    else:
        return False
    
def display_blank_sentence(level):
    """Validates user response against answers array
    Args:
        level (int): level selectd by user
    Returns:
        boolean: Returns true if answer is correct
    """
    try:
      print(sentences[level])
    except IndexError:
      print("requires integer between one and three")

def display_filled_sentence(level, position, blank_input):
    """Displays the sentence as the user fills it in
    Args:
        level (int): level selected by user
        position (int): position of blank within sentence
        blank_input (string): user answer for blank
    Returns:
        Does not return anything
    """
    sentence = sentences[level - 1]
    sentence.split(' ')
    for word in sentence:
        if word == '_' + str(position) + '_':
            word = blank_input
    sentence = ''.join(sentence)
    print(sentence)


def play_game():
    """Prompts user and plays through game
    Args:
        None
    Returns:
        Does not return anything
    """
    # Start game with a prompt to the user
    print("Welcome to the fill-in-the-blanks quiz")
    quit_game = ''
    while quit_game != 'Q' or 'q':
        # Immediately after running the program, user is prompted
        # to select a difficulty level from easy / medium / hard
        level = level_selector()
        display_blank_sentence(level)
        sentence_play(level, 1) # user attempts to fill in blanks
        play_game() # game starts over
    else:
        quit()

play_game() # game play starts when file is run
