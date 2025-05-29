import MZ_utils

def print_first_N_numbers():
     print("---------------------------\nWelcome to the print first N numbers script!")

     while True:
        operation = input("---------------------------\nChoose the operation:\n1. Print first N numbers\nE. Exit\nSelected operation: ")
        if operation == "E":
               break
        if operation != "1" and operation != "2":
                MZ_utils.print_error("Invalid operation")
                continue
        n = input("How many numbers do you want to print? ")
        if MZ_utils.is_input_int(n) == False:
               continue
        n_i = MZ_utils.to_int(n)

        MZ_utils.print_result("Theese are the numbers to print (one for each line): ")
        for i in range(n_i):
                MZ_utils.print_result(i)

        out = ""
        for i in range(n_i):
                out += str(i)
                if (i < n_i - 1):
                       out += ", "

        MZ_utils.print_result(f"Theese are the numbers to print (one for each line): {out}")
                  
print_first_N_numbers()