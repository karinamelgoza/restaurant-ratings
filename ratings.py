"""Restaurant rating lister."""


# put your code here

# create dictionary where ratings will be stored
from os import sep
import random
from typing import List


ratings = {}

# import .txt file

f = open('scores.txt', 'r')
# for i in f:
#     print(i)
# print(f.readlines()[0])

# loop through each line in .txt file and split it into strings at the :
for i in f:
    splitline = i.split(':')
    # add key value pair to dictionary
    ratings[splitline[0]] = splitline[1].strip('\n')

f.close()

# print(ratings)


# print("If you would like to ...\n see restaurant ratings, please type: ratings\n rate a new restaurant, please type: rate\n quit, please type: quit")
# user_input = input()


def alph_sort():
    # stores key value pairs as tuples in a list
    x = ratings.items()
    # print(x)
    ratings_sorted = sorted(x)
    # print(ratings_sorted)

    # loops through each index and access the index of each tuple
    for i in ratings_sorted:
        print(i[0], ' is rated at ', i[1], '.', sep='')


def add_ratings():
    new_res = input('Add restaurant name:\n')
    new_score = input('Score the restaurant from 1-5:\n')
    while int(new_score) not in range(1, 6):
        new_score = input('Please enter a number between 1-5:')
    else:
        ratings[new_res.title()] = new_score
    # alph_sort()
    # add_ratings()


# def user_options():
#     if user_input == 'ratings':
#         alph_sort()
#     elif user_input == 'rate':
#         add_ratings()


# user_options()

def rate_random():
    ran_res = random.choice(list(ratings.items()))
    print(ran_res[0], ' is rated at ', ran_res[1], '.', sep='')
    updated_score = input('new score between 1-5:\n')
    ratings[ran_res[0]] = updated_score
    # print(ratings)


def initial_input():
    print("If you would like to ...\n see restaurant ratings, please enter: ratings\n rate a new restaurant or update an existing one, please enter: rate\n update a random restaurant, please enter: random\n quit, enter: quit")
    user_input = input()

    def user_options():
        if user_input == 'ratings':
            alph_sort()
            initial_input()
        elif user_input == 'rate':
            add_ratings()
            initial_input()
        elif user_input == 'random':
            rate_random()
            initial_input()
        elif user_input == 'quit':
            print('Have a nice day!')
        else:
            print("That's not an option")
            initial_input()

    user_options()


initial_input()
