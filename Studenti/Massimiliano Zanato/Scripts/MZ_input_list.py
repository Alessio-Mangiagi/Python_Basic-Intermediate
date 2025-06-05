# Scrivi un programma in python che chiede all' utente di inserire 5 nomi (uno per volta) 
# li memorizza in una lista e poi stampa tutti i nomi inseriti

import MZ_utils

def input_list():
        print("---------------------------\nWelcome to the input list items printer!")

        list = []
        NR_OF_ITEMS_TO_INSERT = 5

        while len(list) < NR_OF_ITEMS_TO_INSERT:
                n = input(f"Insert {str(NR_OF_ITEMS_TO_INSERT - len(list))} names into list. Name: ")
                list.append(n)

        
        for item in list:
                print(item, end=" ")

        do_continue = False

        while do_continue == False:
                i = input("Do you want to continue? y/n: ")
                match i:
                        case "n":
                                exit_script = True
                                do_continue = True
                        case "y":
                                do_continue = True
                        case _:
                                MZ_utils.print_error("Input value error")
                        
input_list()