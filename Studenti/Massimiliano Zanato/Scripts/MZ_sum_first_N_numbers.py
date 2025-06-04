import MZ_utils

def sum_first_N_numbers():
     print("---------------------------\nWelcome to the sum first N numbers script!")

     while True:
        operation = input("---------------------------\nChoose the operation:\n1. Sum first N numbers\nE. Exit\nSelected operation: ")
        if operation == "E":
               break
        if operation != "1" and operation != "2":
                MZ_utils.print_error("Invalid operation")
                continue
        n = input("How many numbers do you want to sum? ")
        if MZ_utils.is_input_int(n) == False:
               continue
        n_i = MZ_utils.to_int(n)

        sum = 0

        for i in range(1, n_i + 1):
                sum += i

        math_sum = math_sum_first_N_numbers(n_i)

        if sum != math_sum:
               MZ_utils.print_error(f"Mathematical sum is different from your sum: sum: {sum}, math_sum: {math_sum}")
               continue
        else:
               MZ_utils.print_result(f"The sum is: {sum}")                 

def math_sum_first_N_numbers(n):
       return n * (n + 1) / 2

sum_first_N_numbers()