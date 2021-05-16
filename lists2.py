import random 
def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string= input(m)
    return my_string

def print_at_index(L):
    my_index = get_integer("Please enter index number:->")
    output = "The value -- {} -- at index {} in the list".format(L[my_index], my_index)
    print(output)

def print_list(L):
    for x in L:
        print(x)

def print_list_indexes(L):
    for i in range(0,len(L)):
        print( "{}:{}".format(i,L[i]))

def add_item(L):
    my_item = get_string("Please enter new item: ->")
    L.append(my_item)

def find_an_item(L):
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

def shuffle_list(L):
    random.shuffle(L)
    print(L)
    

def sort_list(L):
    L.sort()
    print(L)


def menu():
    my_list1 = ["Mary", "Patsy", "Jean", "Constantine", "Pierre"]
    my_list2 = ["Becky", "Maya", "Grace", "Eleanor", "Anita"]
    my_list = my_list2 
    print("My list is currently set to {}".format(my_list))
    my_menu= '''
    A: print the list
    B: print the list with indices
    C: add item to list
    D: print at index number
    E: find an item
    F: remove item
    G: shuffle list
    H: sort list
    I: choose list 1
    J: choose list 2
    Q: Quit
    '''

    print(id(my_list1))
    print(id(my_list2))
    print(id(my_list)

    run = True
    while run == True:
        print(my_menu)
        choice = get_string("Please select your option: ->")
        print("."*100)
        if choice == "A":
            print_list(my_list)
        elif choice == "B":
            print_list_indexes(my_list)
        elif choice == "C":
            add_item(my_list)
        elif choice == "D":
            print_at_index(my_list)
        elif choice == "E":
            find_an_item(my_list)
        elif choice == "F":
            remove_item(my_list)
        elif choice == "G":
            shuffle_list(my_list)
        elif choice == "H":
            sort_list(my_list)
        elif choice == "Q":
            print("Thank you")
            run = False


menu()
#print_at_index(my_list)
#print_list_indexes(my_list)
#print_list(my_list)
#add_item(my_list)
#print_list(my_list)
