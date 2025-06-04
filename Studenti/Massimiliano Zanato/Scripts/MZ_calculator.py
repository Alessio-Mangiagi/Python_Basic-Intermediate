import MZ_utils

def calculator():
     print("---------------------------\nWelcome to the calculator!")

     while True:
        operation = input("---------------------------\nChoose the operation:\n1. Sum\n2. Subtraction\n3. Multiplication\n4. Real division\n" \
                "5. Integer division\n6. Remainder of the division\nE. Exit\nSelected operation: ")
        if operation == "E":
               break
        if operation != "1" and operation != "2" and operation != "3" and operation != "4" and operation != "5" and operation != "6":
                MZ_utils.print_error("Invalid operation")
                continue
        a = input("First number: ")
        b = input("Second number: ")
        if MZ_utils.is_input_float(a) == False:
               continue
        n_a = MZ_utils.to_float(a)
        if MZ_utils.is_input_float(b) == False:
               continue
        n_b = MZ_utils.to_float(b)
        if (operation == "4" or operation == "5" or operation == "6") and n_b == 0.0:
                print(f"Invalid operation, cannot divide by zero")
                continue
        
        result = ""

        match operation:
                case "1":
                        result = n_a + n_b
                
                case "2":
                        result = n_a - n_b
                
                case "3":
                        result = n_a * n_b

                case "4":
                        result = n_a / n_b

                case "5":
                        result = n_a // n_b

                case "6":
                        result = n_a % n_b

                case _:
                        break

        MZ_utils.print_result(f"The result is {result}")

                         
calculator()