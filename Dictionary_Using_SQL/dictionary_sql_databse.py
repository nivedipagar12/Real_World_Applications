'''
Project 2 : Interactive English Dictionary using SQL database
            A program that takes a single word as input from user and displays its meaning.
            Features :
                    The program checks whether the provided word exists in the dictionary table of the available database
                    If not, then tries to find a close match and asks the user for confirmation
                    The program queries data from a table named Dictionary in a SQL database
Created on: 26/01/2020
Created by: Nivedita Pagar
'''


import mysql.connector
import difflib


def welcome_message():
    print("Hello and welcome to my dictionary !! \nWhat do want to know the meaning of ?")


def get_word():
    word_in = input("Enter a word : ")
    return word_in


welcome_message()
user_continue = True

while user_continue:

    word = get_word()

    # establish a connection to the database
    conn = mysql.connector.connect(
        user = "ardit700_student",
        password = "ardit700_student",
        host = "108.167.140.122",
        database = "ardit700_pm1database"
    )
    cursor = conn.cursor() # create a cursor to navigate through the database
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
    result = cursor.fetchall()

    if result:
        print(str(word) + " means : ")
        count = 0
        for item in result:
            count += 1
            print(str(count) + ") " + str(item[1]))
    else:
        query1 = cursor.execute("SELECT Expression FROM Dictionary") # Get the list of words without definitions
        word_list = cursor.fetchall()
        my_list = []
        for item in word_list:
            my_list.append(item[0]) # Add individual items to the list
        match = difflib.get_close_matches(word, my_list, n=1, cutoff=0.4)  # returns only one match
        if match:
            valid = False
            while not valid: # to check if user enters a valid keyword
                user_input_yesno = input("Did you mean '" + str(match[0] + "'") + " ? \nEnter 'y' for yes and 'n' for no : ")
                if user_input_yesno.lower() in ('yes', 'y'):
                    match = match[0]
                    query2 = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % match)
                    output = cursor.fetchall()
                    for item in output:
                        print(item[1])
                    break
                elif user_input_yesno.lower() in ('no', 'n'):
                    print("\n********Please double check the word********")
                    break
                else:
                    print("Please enter a valid keyword !! ")
        else:
            print("Oops !! Was there a typo ?")
    end = False
    while not end: # to check whether the user wants to search any more words
        user_input_continue = input("\nDo you want to search more ?\nEnter 'y' for yes and 'n' for no : ")
        if user_input_continue.lower() in ('y', 'yes'):
            user_continue = True
            break
        elif user_input_continue.lower() in ('n', 'no'):
            user_continue = False
            break
        else:
            print("Sorry, I didn't get you !!")
