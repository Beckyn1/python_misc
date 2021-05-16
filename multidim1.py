def get_string(m):
    my_string = input(m)
    return my_string


def get_integer(w):
    my_integer = int(input(w))
    # the function terminates when a return is called
    return my_integer


def single_loop_print(l):
    for i in range(0, len(l)):
        output = "{:10} --- {:10} ---  {:<10}".format(l[i][0], l[i][1], l[i][2])
        print(output)


def print_with_indexes(l):
    for i in range(0, len(l)):
        output = "{:3} : {:10} {:10} {:10}".format(i, l[i][0], l[i][1], l[i][2])
        print(output)


def add_new_entry(l):
    print("start adding new entry")
    name = get_string("please enter name")
    hair_colour = get_string("please enter hair colour")
    age = get_integer("please enter age")
    new_list = [name, hair_colour, age]
    l.append(new_list)


def update_name(l):
    print_with_indexes(l)
    my_index = get_integer("Choose index number")
    print(l[my_index])
    new_name = get_string("what is name")
    old_name = l[my_index][0]
    l[my_index][0] = new_name
    print("The name {} has been updated to {}".format(old_name, new_name))


def main():
    my_l = [
        ["Alice", "Blond", 12],
        ["Cathy", "Blond", 15],
        ["Dan", "Black", 10],
        ["Bob", "Brown", 13],
        ["Joe", "Green", 13]
    ]
    add_new_entry(my_l)
    # single_loop_print(my_l)
    update_name(my_l)


main()
# print_with_indexes(my_l)
