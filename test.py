def single_loop_print(L):
    for i in range(0,len(L)):
        output="{:0} --- {:10} --- {:<10}".format(L[i][0], L[i],[1], L[i],[2])
        print(output)

def print_with_indexes(L):
    for i in range(0, len(L)):
        output="{} {} {} {}".format(i,L[i][0], L[i],[1], L[i],[2])
        print(output)

def main():
    my_L =[
        ["Alice", "Blond", 12],
        ["Cathy", "Blond", 15],
        ["Dan","Black", 10],
        ["Bob", "Brown", 13],
        ["Joe", "Green", 13]
    ]

    single_loop_print(my_L)
#print_with_indexes(my_L)
