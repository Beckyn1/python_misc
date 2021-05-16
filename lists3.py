def find_an_item():
    item = get_string("who do you want to find?")
    if item in L:
        index_num = L.index(item)
        output = "{} has been found and is at index number {}".format(L[index_num],index_num)
        print(output)
    else:
        print("{} is not in the list".format(item))
              
def remove_item(L):
    item= get_string("who do you want to remove")
    if item in L:
        L.remove(item)
        output= "{} has been removed from the list".format(item)
        print(output)
    else:
        output = "{} could not be found, so was not in the list anyway".format(item)
        print(output)

#L.sort() to sort list in alphabetical order
#L.shuffle() to shuffle list

#import random
#def shuffle_list(L):
#   random.shuffle(L)
