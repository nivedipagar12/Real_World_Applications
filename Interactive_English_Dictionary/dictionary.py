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


def translate():
    print("Hello and welcome to my dictionary !! \nWhat do want to know the meaning of ?")
    data = json.load(open("data.json"))
    cont = True
    while cont:
        user_input = input("\n\nEnter a word : ").lower()
        if user_input in data.keys():
            output = data[user_input]
            for item in output:
                print(item)
        elif user_input.capitalize() in data.keys():
            output = data[user_input.capitalize()]
            for item in output:
                print(item)
        elif user_input.upper() in data.keys():
            output = data[user_input.upper()]
            for item in output:
                print(item)
        else:
            match = difflib.get_close_matches(user_input, data.keys(), n=1, cutoff=0.4)  # returns only one match
            if isinstance(match, list):
                user_input_yesno = input("Did you mean " + str(match) + " ? \nEnter 'y' for yes and 'n' for no : ")
                if user_input_yesno.lower() in ('yes', 'y'):
                    match = match[0]
                    output = data[match]
                    for item in output:
                        print(item)
                elif user_input_yesno.lower() in ('no', 'n'):
                    print("\n********Please double check the word********")
            else:
                print("Oops !! Was there a typo ?")
        end = False
        while not end:
            user_input_continue = input("\nDo you want to search more ?\nEnter 'y' for yes and 'n' for no : ")
            if user_input_continue in ('y', 'yes'):
                cont = True
                break
            elif user_input_continue in ('n', 'no'):
                cont = False
                break
            else:
                print("Sorry, I didn't get you !!")


translate()
