import MZ_utils

def check_prime_number():
     print("---------------------------\nWelcome to the check prime number script!")

     exit_script = False

     while exit_script == False:
        n = input("Insert an integer number > 1: ")

        if MZ_utils.is_input_int(n) == False:
               continue
        n_i = MZ_utils.to_int(n)

        if n_i <= 1:
              MZ_utils.print_error(f"{n} is not a valid input number")
        elif is_odd(n_i) == False:
              MZ_utils.print_result(f"The number {n} is not prime, it can be divided by 2") 
        else:
             is_prime = True
             can_be_divided_by = 0
             for i in range(3, sqrt(n_i) + 1, 2):
                  if n_i % i == 0:
                        is_prime = False
                        can_be_divided_by = i
                        break
            
             if is_prime:
                  MZ_utils.print_result(f"The number {n} is prime")
             else:
                  MZ_utils.print_result(f"The number {n} is not prime, it can be divided by {str(can_be_divided_by)}")   

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

def is_odd(n):
     return n % 2 != 0

def sqrt(n):
     return int(n ** 0.5)
       
                        
check_prime_number()