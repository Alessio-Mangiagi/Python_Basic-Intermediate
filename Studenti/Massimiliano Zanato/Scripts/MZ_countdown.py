import MZ_utils
import time

def countdown():
     print("---------------------------\nWelcome to the countdown script!")

     while True:
        operation = input("---------------------------\nChoose the operation:\n1. Start countdown\nE. Exit\nSelected operation: ")
        if operation == "E":
               break
        if operation != "1" and operation != "2":
                MZ_utils.print_error("Invalid operation")
                continue
        n = input("Insert an integer number for countdown start value: ")
        if MZ_utils.is_input_int(n) == False:
               continue
        n_i = MZ_utils.to_int(n)
        i = n_i

        while i > 0:
              MZ_utils.print_result(f"Value: {str(i)}")
              i -= 1
              time.sleep(1)

        MZ_utils.print_result("Countdown expired!")       

countdown()