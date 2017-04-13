import random
import string
from collections import defaultdict

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 14

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  ", len(wordlist), "words loaded.")
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

def get_word_score(word):
    score = 0
    for letter in word.replace(' ', ''):
        score += SCRABBLE_LETTER_VALUES[letter]
    if len(word) == HAND_SIZE:
        return score + 50
    return score
    
def display_hand(hand):
    ##     """
    ## Displays the letters currently in the hand.
    ## For example:
    ##display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    ##Should print out something like:
    ##a x x l l l e
    ## The order of the letters is unimportant.
    ## hand: dictionary (string -> int)
    ##"""
    display = ''
    for letter in hand.keys():
        for j in range(hand[letter]):
            display += letter + ' ' # the comma ensures everything in the for loop prints onthe same line
    print(display) # this just prints an empty line
    print
import random
import math
def deal_hand(n):
    ## """
    ## Returns a random hand containing n lowercase letters.
    ##At least n/3 of the letters in the hand should be VOWELS.
    ## Hands are represented as dictionaries. The keys are
    ##letters and the values are the number of times the
    ## particular letter is repeated in that hand.
    ## n: int >= 0
    ## returns: dictionary (string -> int)
    ##"""
    hand={}
    num_vowels = n / 3
    for i in range(math.ceil(num_vowels)):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
    for i in range(math.ceil(num_vowels), n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
    return hand 


def update_hand(hand, word):
##    try: word in wordlist
##    except Exception: print('Not a word.')
    word_dic = get_frequency_dict(word)
    for letter in word_dic.keys():
        hand[letter] -= word_dic[letter]
        if hand[letter] == 0:
            del hand[letter]
    return hand 

def is_valid_word(word, hand):
##     """
## Returns True if word is in the word_list and is entirely
##composed of letters in the hand. Otherwise, returns False.
##Does not mutate hand or word_list.
## word: string
##hand: dictionary (string -> int)
##word_list: list of strings
    word_dic = get_frequency_dict(word)
    ##Checks if enough letters in hand for the word, and if the word is legal
    if all (hand.get(x,0) >= word_dic[x] for x in word_dic.keys()) and word in points_dict:
        return True
       
    return False
import time

def run_play_hand(hand,word_list):
    time_control = 10.0
    print("You have %r seconds to play." % (time_control))
    return play_hand(hand,word_list, 0.0, time_control)


def play_hand(hand,word_list, score, time_control):
    display_hand(hand)
    word_bool = False
    start_time = time.time()
    while (not word_bool):
##        player_input = str(input("Make a move, bub. Give me a 'period' to end game. \n"))
        player_input = pick_best_word_faster(hand, sorted_dict)
##        player_input = pick_best_word(hand, points_dict)
        print(player_input)
        print
        if '.' in player_input:
            print('quitter, your score is', round(score,2))
            return
        word_bool = is_valid_word(player_input, hand)
        end_time = time.time()
        total_time = end_time - start_time
        if time_control - total_time < 0.0:
            print("You used too much time. You scored", round(score,2),"points.")
            return
    print("It took",total_time, "seconds to provide an answer.")
    print("You have", time_control - total_time, "seconds remaining.")
    new_hand = update_hand(hand, player_input)
    if total_time < 0.01:
        score += get_word_score(player_input)
    else: score += (get_word_score(player_input) / total_time)
    print('%r: score    %r: word score' % (round(score,2), get_word_score(player_input)))
    if not new_hand:
        print("you win! With a score of ", round(score,2) )
        return
    return play_hand(new_hand,word_list, score, time_control - total_time)

def pick_best_word(hand, points_dict):
    best_word = ''
    best_word_score = 0
    for word in points_dict.keys():
        if is_valid_word(word,hand):
            word_score = points_dict[word]
            if word_score > best_word_score:
                best_word = word
                best_word_score = word_score
    if best_word_score > 0:
        return best_word
    return '.'

def pick_best_word_faster(hand, sorted_points_dict):
    combo = combo_assist(hand)
    best_word = ''
    best_word_score = 0
    for i in combo:
        if i in sorted_points_dict:
            word_score = points_dict[sorted_points_dict[i]]
            if word_score > best_word_score:
                best_word_score = word_score
                best_word = sorted_points_dict[i]
    if best_word_score >0:
        return best_word
    return '.'       
            

def get_sorted_dict(wordlist):
    D = dict()
    for word in wordlist:
        temp = ''
        for i in sorted(word):
            temp += i  
        D[temp] = word
    return D
 
def combo_assist(hand):
    hand_letters = ''
    letter_count = []
    for i in hand.keys():
        hand_letters += i
 
    hand_letters = ''.join(sorted(set(hand_letters)))

    for i in hand_letters:

        letter_count.append(hand[i])
    combo = []
    combo_word = ''
    return combination(hand_letters, letter_count, 0,combo, combo_word)   
        
def combination(hand_letters, letter_count, position, combo, combo_word):
    
##    print(temp_count)
    a = combo_word
    
    for i in range(position, len(hand_letters)):
        
        if letter_count[i] != 0:
            
            combo_word += hand_letters[i]
            print("combo", combo_word)
            combo.append(combo_word)
            letter_count[i] -= 1
##            print(combo, temp_count)
            
            combination(hand_letters, letter_count, i, combo, combo_word)
##            print(combo, "combo word")
            
            letter_count[i] += 1
            combo_word = a
    return sorted(combo)
            
            
##        print(combo)
    return combo
combo = {'a':2,'f':1,'c':1,'b':1}
combo_assist(combo)                 
def get_words_to_points(word_list):
    
    a = {}
    for element in word_list:
        if len(element) <= HAND_SIZE:
            a[element] = get_word_score(element)
    return a

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
    # TO DO ...
   # delete this once you've completed Problem #4
    
    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            run_play_hand(hand.copy(), wordlist)
            print
        elif cmd == 'r':
            run_play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print ("Invalid command.")
global wordlist
wordlist = load_words()
global points_dict
points_dict = get_words_to_points(wordlist)
sorted_dict = get_sorted_dict(wordlist)   















def Ghost():
    turn = 1
    print("A game of Ghost! is under way")
    print
    a = True
    word_index = 1
    word = ''
    while a:
        
        
        
        if turn %2 == 1:
            player = 1
            while(True):
                cmd = input('Enter a letter. ')
                if valid_letter(cmd):
                    break
            word += cmd
        else:
            player = 2
            while(True):
                cmd = input('Enter a letter. ')
                if valid_letter(cmd):
                    break
            word += cmd
        if word in wordlist and len(word) > 3:
            print("Player",player ,'loses! Because', word,'is a word!')
            a = False
            break
        for i, letter in enumerate(wordlist[word_index-1:]):
            if letter[0:len(word)] == word:
                word_index = max(i,1)
                print("The current letters are " + word)
                break
                
            if letter[0:len(word)] > word:
                print(word,"cannot be a word. Player", player, 'loses on the #', turn, 'turn.')
                a = False
                break
        
        

        turn += 1
    
import string
def valid_letter(letter):
    
    if len(letter) == 1 and letter in string.ascii_letters:
            return True
    return False
            
##def turn():
##    while(True):
##        cmd = input('Enter a letter. ')
##        if valid_letter(cmd):
##            return cmd

def possible_word():
    pass
        
