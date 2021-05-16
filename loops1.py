# loops
# loops are repeated actions (iterations)

# loop with a counter (will run a certain number of times)
def loop_with_counter():
    c = 0
    while c < 10:
        print("yuh c is now {}".format(c))
        # increment c
        c += 1
    return None

# indefinite loop
def indefinite_loop():
    run = True
    while run == True:
        user_choice= input("Press 'w' to stop the loop \w or anything else to stay in the loop")
        if user_choice == "w":
            print("Loop will stop")
            run = False
        else:
            print("You are still in the loop")
def for_in_range_loop():
    # this has a built in counter
    # can be anything but we generally use i or j or k
    # can add steps
    for i in range(6, 50):
        print(i)

def double_loop():
    for i in range(0,5):
        for j in range(0,6):
            print("({},{})".format(i,j), end="")
        print()
    
#loop_with_counter()
#indefinite_loop()
#for_in_range_loop()
double_loop()
