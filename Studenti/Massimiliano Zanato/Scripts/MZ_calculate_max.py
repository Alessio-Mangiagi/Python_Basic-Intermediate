import MZ_utils

def calculate_max():
     print("---------------------------\nWelcome to the detector of the maximum between three numbers!")

     while True:
        operation = input("---------------------------\nChoose the operation:\n1. Detect maximum number\nE. Exit\nSelected operation: ")
        if operation == "E":
               break
        if operation != "1" and operation != "2":
                MZ_utils.print_error("Invalid operation")
                continue
        n1 = input("First number: ")
        if MZ_utils.is_input_float(n1) == False:
               continue
        n1_f = MZ_utils.to_float(n1)

        n2 = input("Second number: ")
        if MZ_utils.is_input_float(n2) == False:
               continue
        n2_f = MZ_utils.to_float(n2)

        n3 = input("Third number: ")
        if MZ_utils.is_input_float(n3) == False:
               continue
        n3_f = MZ_utils.to_float(n3)

        max = 0.0

        if n1_f > n2_f and n1_f > n3_f:
                max = n1_f
        elif n2_f > n3_f:
                max = n2_f
        else:
                max = n3_f

        MZ_utils.print_result(f"The maximum number is {max}")
                        
calculate_max()