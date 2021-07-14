"""Restaurant rating lister."""


# put your code here

# create dictionary where ratings will be stored
from os import sep


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


def alph_sort():
    # stores key value pairs as tuples in a list
    x = ratings.items()
    # print(x)

    ratings_sorted = sorted(x)
    # print(ratings_sorted)

    # loops through each index and access the index of each tuple
    for i in ratings_sorted:
        print(i[0], ' is rated at ', i[1], '.', sep='')


alph_sort()


def add_ratings():
    new_res = input('add restaurant name\n')
    new_score = input('add restaurant score\n')
    ratings[new_res] = new_score
    alph_sort()
    # add_ratings()


add_ratings()
