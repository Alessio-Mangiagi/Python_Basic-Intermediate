import MZ_utils

def print_even_numbers():
     print("---------------------------\nWelcome to even number printer!")

     exit_script = False

     while exit_script == False:
        n = input("Insert an integer number for upper bound limit: ")

        if MZ_utils.is_input_int(n) == False:
               continue
        n_i = MZ_utils.to_int(n)

        range_with_step_method(n_i)
        module_filter_method(n_i)
        list_comprehension_method(n_i)
        function_method(n_i)

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

def range_with_step_method(n):
        MZ_utils.print_result("*** Method 1: range with step ***")
        for i in range(2, n + 1, 2):
                print_n(i)

def module_filter_method(n):
        MZ_utils.print_result("*** Method 2: module filter ***")
        for i in range(1, n + 1):
               if i % 2 == 0:
                      print_n(i)

def list_comprehension_method(n):
        MZ_utils.print_result("*** Method 3: list comprehension ***")
        even_list = [k for k in range(1, n + 1) if k % 2 == 0]
        for i in even_list:
                print_n(i)

def function_method(n):
       MZ_utils.print_result("*** Method 4: function method ***")
       for i in range(1, n + 1):
              if is_even(i):
                print_n(i)

def is_even(n):
       return n % 2 == 0
                      
def print_n(n):
       MZ_utils.print_result(str(n))
                        
print_even_numbers()