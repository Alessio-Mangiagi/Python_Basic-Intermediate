import MZ_utils

def temperature_convertitor():
     print("---------------------------\nWelcome to the temperature convertitor!")

     while True:
        operation = input("---------------------------\nChoose the operation:\n1. From Celsius to Fahrenheit\n2. From Fahrenheit to Celsius\nE. Exit\nSelected operation: ")
        if operation == "E":
               break
        if operation != "1" and operation != "2":
                MZ_utils.print_error("Invalid operation")
                continue
        t = input("Input temperature: ")
        if MZ_utils.is_input_float(t) == False:
               continue
        t_f = MZ_utils.to_float(t)

        p = input("Precision (number of decimal cipher): ")
        if MZ_utils.is_input_int(p) == False:
               continue
        p_i = MZ_utils.to_int(p)
        
        result = ""

        match operation:
                case "1":
                        result = to_fahrenheit(t_f, p_i)
                
                case "2":
                        result = to_celsius(t_f, p_i)
                
                case _:
                        break

        MZ_utils.print_result(f"The result is {result}")

def to_fahrenheit(c, precision):
       return round(c * 9 / 5 + 32, precision)

def to_celsius(f, precision):
       return round((f - 32) * 5 / 9, precision)
                         
temperature_convertitor()