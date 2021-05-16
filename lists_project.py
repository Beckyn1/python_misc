N = []
A= []

def get_string(m):
    my_string= input(m)
    return my_string


def add_names_age(N,A):
    my_item = int(input("How many names and ages would you like to add?"))
    for i in range(my_item):
        name = get_string("Please enter name: ")
        N.append(name)
        age = int(input("Please enter age: "))
        A.append(age)
        output = "{} aged {} has been added to the list.".format(name,age)
        print(output)
 

def review(N,A):
    column = "\n".join("{}  {}".format(x, y) for x, y in zip(N, A))
    print("Name - Age")
    print(column)

def main():
    my_main= '''
    A: Add
    R: Review
    Q: Quit
    '''

    run = True
    while run == True:
        print(my_main)
        choice = get_string("Please select your option: ->")
        print("."*100)
        if choice == "A":
            add_names_age(N,A)
        elif choice == "R":
            review(N,A)
        elif choice == "Q":
            print("Thank you")
            run = False

main()
