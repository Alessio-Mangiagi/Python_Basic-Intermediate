import MZ_utils

def conditional_counter():
     print("---------------------------\nWelcome to the conditional counter script!")

     exit_script = False

     while exit_script == False:
        count = 0
        s = input("Insert a string: ")

        if MZ_utils.is_null_or_empty(s) == False:
                is_c_valid = False
                c = ""

                while is_c_valid == False:
                        c = input("Insert the character or substring to count: ")
                        if MZ_utils.is_null_or_empty(c) == False:
                                is_c_valid = True

                if len(c) <= len(s):
                        for i in range(0, len(s) - len(c) + 1):
                                sub = s[i : i + len(c)]
                                print(f"Substring iter n.{str(i)}: {sub}")
                                if sub == c:
                                        count += 1

                MZ_utils.print_result(f"The number of occurrence of {c} in {s} is {str(count)}")

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
       
                        
conditional_counter()