def go_print():
    print("Hi, welcome to calculator")

def go_print_var():
    my_input = int(input("Please enter a number: -> "))
    my_input2 = int(input("Please enter a number: -> "))
    my_sum = my_input + my_input2
    my_string = "{} + {} = {}".format(my_input, my_input2, my_sum)
    print(my_string)

def go_print_var2():
    my_input = int(input("Please enter a number: -> "))
    my_input2 = int(input("Please enter a number: -> "))
    my_sum = my_input - my_input2
    my_string = "{} - {} = {}".format(my_input, my_input2, my_sum)
    print(my_string)

def go_print_var3():
    my_input = int(input("Please enter a number: -> "))
    my_input2 = int(input("Please enter a number: -> "))
    my_sum = my_input / my_input2
    my_string = "{} / {} = {}".format(my_input, my_input2, my_sum)
    print(my_string)

def go_print_var4():
    my_input = int(input("Please enter a number: -> "))
    my_input2 = int(input("Please enter a number: -> "))
    my_sum = my_input * my_input2
    my_string = "{} x {} = {}".format(my_input, my_input2, my_sum)
    print(my_string)

go_print()
#go_print_var()
#go_print_var2()
#go_print_var3()
go_print_var4()
