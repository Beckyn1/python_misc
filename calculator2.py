
def go_print():
    print("Welcome to Calculator")

def get_integer_input():
    my_input = int(input("Please enter a number: -> "))
    # the function terminates when a return is called
    return my_input

def menu():
    my_menu = '''
    1 : addition
    2 : subtraction
    3 : multiplication
    4 : division
    0 : quit
    '''
    print(my_menu)
    user_choice = get_integer_input()
    if user_choice == 1:
         go_print_var()
         
    elif user_choice == 2:
         go_print_var2()
         
    elif user_choice == 3:
         go_print_var3()
         
    elif user_choice == 4:
         go_print_var4()
         
    elif user_choice == 0:
         print("Thank you")
    else:
         print("Unrecognised entry")
    
def go_print_var():
    print("Addition")
    my_input = int(input("Please enter a number: -> "))
    my_input2 = int(input("Please enter a number: -> "))
    my_sum = my_input + my_input2
    my_string = "{} + {} = {}".format(my_input, my_input2, my_sum)
    print(my_string)

def go_print_var2():
    print("Subtraction")
    my_input = int(input("Please enter a number: -> "))
    my_input2 = int(input("Please enter a number: -> "))
    my_sum = my_input - my_input2
    my_string = "{} - {} = {}".format(my_input, my_input2, my_sum)
    print(my_string)

def go_print_var3():
    print("Multiplication")
    my_input = int(input("Please enter a number: -> "))
    my_input2 = int(input("Please enter a number: -> "))
    my_sum = my_input / my_input2
    my_string = "{} / {} = {}".format(my_input, my_input2, my_sum)
    print(my_string)

def go_print_var4():
    print("Division")
    my_input = int(input("Please enter a number: -> "))
    my_input2 = int(input("Please enter a number: -> "))
    my_sum = my_input * my_input2
    my_string = "{} x {} = {}".format(my_input, my_input2, my_sum)
    print(my_string)

go_print()
menu()
