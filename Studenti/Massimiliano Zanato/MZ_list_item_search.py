import MZ_utils

def list_item_search():
     print("---------------------------\nWelcome to the list item search script!")

     list = []

     while True:
        operation = input("---------------------------\nChoose the operation:\n1. Insert item into list (insert exit to return to main menu)\n2. Check item exisence\nE. Exit\nSelected operation: ")
        if operation == "E":
               break
        if operation != "1" and operation != "2":
                MZ_utils.print_error("Invalid operation")
                continue

        do_exit = False

        match operation:
                case "1":
                        while do_exit == False:
                                e = input("Element to insert: ")
                                if MZ_utils.is_null_or_empty(e):
                                        continue
                                elif e in list:
                                        MZ_utils.print_error("Input element is already contained into list")
                                elif e == "exit":
                                        do_exit = True
                                else:
                                        list.append(e)
                
                case "2":
                        e = input("Element to search: ")
                        if list.__contains__(e):
                               MZ_utils.print_result(f"__contains__ functions reveals that {e} is contained into list")
                        if e in list:
                               MZ_utils.print_result(f"e in list reveals that {e} is contained into list")
                        i = 0
                        for element in list:
                               if element == e:
                                     MZ_utils.print_result(f"{e} is the element n.{str(i)} of the list")
                                     break
                               i += 1 
                               
                case _:
                        break
                        
list_item_search()