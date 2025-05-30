import MZ_utils

def discount_price():
     print("---------------------------\nWelcome to the discount price calculator!")

     exit_script = False

     while exit_script == False:
        is_amount_valid = False

        while is_amount_valid == False:
                f = input("Insert an amount (Euro): ")

                if MZ_utils.is_input_float(f) == False:
                        continue
                n_f = MZ_utils.to_float(f)
                is_amount_valid = True

        is_discount_valid = False

        while is_discount_valid == False:
                f = input("Insert a discount (%): ")

                if MZ_utils.is_input_float(f) == False:
                        continue
                n_d = MZ_utils.to_float(f)

                if n_d < 0 or n_d > 100:
                        MZ_utils.print_error(f"Invalid input percent")
                else:
                        is_discount_valid = True

        discount = round(n_f * n_d / 100, 2)
        discounted_price = round(n_f - discount, 2)
        
        MZ_utils.print_result(f"The discount is {str(discount)}, the discounted price is Euro {str(discounted_price)}")
      
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
                        
discount_price()