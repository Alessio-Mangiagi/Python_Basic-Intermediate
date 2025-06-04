import MZ_utils

def times_table():
     print("---------------------------\nWelcome to the times table printer!")

     while True:
        operation = input("---------------------------\nChoose the operation:\n1. Print the times table\nE. Exit\nSelected operation: ")
        if operation == "E":
               break
        if operation != "1" and operation != "2":
                MZ_utils.print_error("Invalid operation")
                continue
        n = input("Insert an integer number: ")
        if MZ_utils.is_input_int(n) == False:
               continue
        n_i = MZ_utils.to_int(n)

        MZ_utils.print_result(f"The times table of {n_i} is: ")
        for i in range(1, 11):
                MZ_utils.print_result(f"{n} * {i}: {str(n*i)}");            

times_table()