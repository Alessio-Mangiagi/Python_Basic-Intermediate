import MZ_utils

def average_calculation():
     print("---------------------------\nWelcome to the average calculator!\n---------------------------\n")

     while True:
        operation = input("---------------------------\nChoose the action:\n1. Average calculation between three numbers\nE. Exit\nSelected operation: ")
        if operation == "E":
               break
        if operation != "1":
                MZ_utils.print_error("Invalid operation")
                continue
        f1 = input("First number: ")
        if MZ_utils.is_input_float(f1) == False:
               continue
        f1_f = MZ_utils.to_float(f1)
        f2 = input("Second number: ")
        if MZ_utils.is_input_float(f2) == False:
               continue
        f2_f = MZ_utils.to_float(f2)
        f3 = input("Third number: ")
        if MZ_utils.is_input_float(f3) == False:
               continue
        f3_f = MZ_utils.to_float(f3)
        p = input("Precision (number of decimal cipher): ")
        if MZ_utils.is_input_int(p) == False:
               continue
        p_i = MZ_utils.to_int(p)
        
        result = get_average(f1_f, f2_f, f3_f, p_i)

        MZ_utils.print_result(f"The result is {result}")

def get_average(f1, f2, f3, precision):
       return round((f1 + f2 + f3) / 3, precision)
                         
average_calculation()