# Problem Set 5: 6.00 Word Game
# Name:  Leena Suresh
# Collaborators: None
# Time: 1 hour
#

import random
import string
from globalfunctions import *
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

# -----------------------------------

# Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0
    if len(word) == n:
        score = 50
    for a in word:
        score += SCRABBLE_LETTER_VALUES[a]
    return score

#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line
    return None

#
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    updated_hand = {}
    
    updated_hand = dict(hand)
    
    for letter in word:
        if updated_hand[letter] == 1:
            del updated_hand[letter]
        else:
            updated_hand[letter] = updated_hand.get(letter, 0) - 1
            
    return updated_hand

# Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
    value = None
    updated_hand = update_hand(hand, word)
    for a in updated_hand:
        if updated_hand[a] < 0:
            value = False
            break
    else:
        for b in word_list:
            if b == word:
                value = True
    return value
        
#Pick the best word
        

def play_hand(hand, word_list):
    
    #Initializing Variables Begin
    word_score = 0
    Tot_score = 0
    end_game = False
    start_time = 0
    end_time = 0
    total_time = 0
    time_limit = 0
    #Initializing Variables end

    #Prompt the user for a time limit for each player

    time_limit = readVal(float, "Please enter the time limit, in seconds, for the player", "That is not a valid entry for time! Please enter a floating point value")

    #Exception handling for time limit ^^^
    
    print "Your current hand is"
    display_hand(hand)                                  # Display the current hand
    
    while len(hand) > 0:    
                
        start_time = time.time()                                                                #Begin Time Block
        word = raw_input("Please enter your word or enter '.' if you wish to end the game ")            
        end_time = time.time()                                                                  #End Time Block
        
        if (word == '.'):                                                                     #Check if the player has ended the game
            print "You have ended the game"                                                 
            break

        if not((is_valid_word(word, hand, word_list))):
            print "Oops! You made a boo boo. That's not a word. Try again!"                   #Check if its a valid word
        else:
            
            total_time = end_time - start_time                                                          #Calculate the remaining time
            rem_time = round(time_limit - total_time, 2)
                
            if total_time < 1:
                total_time = 1          #If it takes less than a second to answer, total time is taken as one second
            total_time = total_time
                
            print "It took", total_time, "to enter your word"
            print "You have ", rem_time, "remaining"

            if rem_time < 0:                                                                                #Check if the player exceeds his time limit
                print "You have exceeded your time limit. Your game ends here and unfortunately, your last word can not be scored."
                break
            
            else:
                word_score = round((get_word_score(word, len(hand))/total_time),2)                          #Calculate word score and the total score so far
                Tot_score = (Tot_score + word_score)
            
                hand = update_hand(hand,word)
            
                print word, "earned", word_score, "points"

                print "Your total score so far is", Tot_score
            
            if len(hand) > 0:
                print "The remaining letters in your hand is"                                               #Remaining letters in the hand
                display_hand(hand)      
            else:
                print "You have used up all the letters in your hand. Your game ends here"
                break

    print "Your total score for this game is", Tot_score


# Playing a game
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """ 

    hand = deal_hand(HAND_SIZE) # random init
    
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

