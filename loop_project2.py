def go_print():
    print("Welcome to Calculator")

def get_integer_input():
    my_input = int(input("Please enter a number: -> "))
    # the function terminates when a return is called
    return my_input

def main():
    go_print()
    run_program = True
    while run_program == True:
        my_menu = '''
        1 : square
        2 : cube
        0 : quit
        '''
        print(my_menu)
        
        user_choice = get_integer_input()
        if user_choice == 1:
             square_loop()
             
        elif user_choice == 2:
             cube_loop()
             
        elif user_choice == 0:
             print("Thank you")
             run_program = False
        else:
             print("Unrecognised entry")

def square_loop():
    w = int(input("Please enter a start number: -> "))
    x = int(input("Please enter an end number: -> "))
    for o in range(w,x):
            print("{} x {} = ".format(o,o), o ** 2)

def cube_loop():
    w = int(input("Please enter a start number: -> "))
    x = int(input("Please enter an end number: -> "))
    for p in range(w,x):
            print("{} x {} x {} = ".format(p,p,p), p ** 3)


main()
