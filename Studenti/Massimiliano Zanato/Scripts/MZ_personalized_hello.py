import MZ_utils

def personalized_hello():
     print("---------------------------\nWelcome to the personalized hello application!")

     while True:
        operation = input("---------------------------\nChoose the action:\n1. Create personalized hello\nE. Exit\nSelected operation: ")
        if operation == "E":
               break
        if operation != "1":
                MZ_utils.print_error("Invalid operation")
                continue
        name = input("Enter your name: ")

        if MZ_utils.is_null_or_empty(name):
              MZ_utils.print_error("Invalid name");
              continue

        age = input("Enter your age: ")

        if MZ_utils.is_input_int(age) == False:
               continue
        
        result = f"Hello {name}! Your age is {age}!"

        MZ_utils.print_result(result)

                         
personalized_hello()