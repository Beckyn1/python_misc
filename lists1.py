#print(len(my_list)) for list length
#access item
#print list
#add to list
#update to list
#remove from list
#sort list

my_list = ["Mary", "Patsy", "Jean", "Constantine", "Pierre"]
print(my_list[2])

def print_at_index(L):
    my_index=get_integer("please choose index")
    print(L[my_index])
print_at_index(my_index)

def print_list(L):
    for x in L:
        print(x)

def print_list_indexes(L):
    for i in range(0,len(L)):
        print("{}:{}".format(i,L[i]))
print_list_indexes(my_list)

#add to list
my_list.append("Damian")

def add_item(L):
    new_item= get_string("Please senter new item")
    L.append(new_item)
    add_item(my_list)
        
