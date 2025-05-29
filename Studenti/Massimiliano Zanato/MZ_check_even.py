import MZ_utils

def check_even():
     print("---------------------------\nWelcome to check even number application!")

     while True:
        operation = input("---------------------------\nChoose the action:\n1. Check number\nE. Exit\nSelected operation: ")
        if operation == "E":
               break
        if operation != "1":
                MZ_utils.print_error("Invalid operation")
                continue
        n = input("Enter an integer number: ")

        if MZ_utils.is_input_int(n) == False:
               continue

        n_i = MZ_utils.to_int(n)
        
        r = n_i % 2
        s = ""
        if r != 0:
              s = "Odd"
        else:
              s = "Even"
        
        result = f"Your number {n} is {s}!"

        MZ_utils.print_result(result)

                         
check_even()