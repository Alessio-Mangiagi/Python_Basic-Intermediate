import MZ_utils

def personalized_hello():
     print("---------------------------\nWelcome to the personalized hello application!")

     while True:
        name = input("Enter your name: ")
        age = input("Enter your age: ")

        if MZ_utils.is_input_int(age) == False:
               continue
        
        result = f"Hello {name}! Your age is {age}!"

        MZ_utils.print_result(result)

                         
personalized_hello()