'''
Project 1 : Interactive English Dictionary
            A program that takes a single word as input from user and displays its meaning.
            Features :
                    The program checks whether the provided word exists in the dictionary
                    If not then tries to find a close match and asks the user for confirmation
            Associated file : data.json

Created on: 23/01/2020
Created by: Nivedita Pagar
'''


import json
import difflib


def welcome_message():
    print("Hello and welcome to my dictionary !! \nWhat do want to know the meaning of ?")


def load_data():
    data = json.load(open("data.json"))
    return data


def get_word():
    user_input = input("Enter a word : ").lower()
    return user_input


def check_good_bad(data2, word1):
    if word1 not in data2.keys():
        return False
    else:
        return True


def check_matches(data3, word2):
    match = difflib.get_close_matches(word2, data3.keys(), n=1, cutoff=0.4) # returns only one match
    if len(match) != 0:
        return match
    else:
        return "none" # if no match was found with > 40 % similarity


def get_meaning(data3, word_in):
    return data3[word_in]


def ask_user():
    correct = False
    while not correct:
        yes_no = input("Do you want to search more ?? Press 'y' for yes and 'n' for no : ")
        if yes_no.lower() in ("y", "yes"):
            result = True
            break
        elif yes_no.lower() in ("n", "no"):
            result = False
            break
        else:
            print("Sorry, I don't follow !!")
    return result


user_continue = True
welcome_message()

while user_continue:
    data1 = load_data()
    word = get_word()
    good_bad = check_good_bad(data1, word)
    if good_bad:
        print(get_meaning(data1, word))
    else:
        answer = check_matches(data1, word)
        if answer == "none":
            print("Oops !! Was there a typo ?")
        else:
            word = answer
            print("Did you mean " + str(word) + " ? ")
            check = input("Enter 'y' for yes and 'n' for no : ")
            if check.lower() in ("yes","y"):
                word = str(word[0])
                print(word)
                print(get_meaning(data1, word))
            else:
                print("Please double check the word !!")
    user_continue = ask_user()

print("Ciao !!")
