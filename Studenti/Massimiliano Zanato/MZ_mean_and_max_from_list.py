import MZ_utils
import statistics
import sys

def list_item_search():
     print("---------------------------\nWelcome to the list item search script!")

     list = []
     exit_script = False

     while exit_script == False:
        print("Insert numbers into list. Digit exit to end number insertion!")

        do_exit = False
        ROUND_CIPHER = 2

        while do_exit == False:
                e = input("Element to insert: ")
                if MZ_utils.is_null_or_empty(e):
                        continue
                elif e == "exit":
                        do_exit = True
                elif MZ_utils.is_input_float(e) == False:
                        continue
                else:
                        list.append(MZ_utils.to_float(e))

        if len(list) == 0:
                MZ_utils.print_error("List is empty. Cannot calculate statistics")
        else:
                v_max = 0.0
                v_min = sys.float_info.max
                for i in range(len(list)):
                        if list[i] > v_max:
                              v_max = list[i]
                        if list[i] < v_min:
                              v_min = list[i]

                v_max = round(v_max, ROUND_CIPHER)
                v_min = round(v_min, ROUND_CIPHER)
                median = round(get_median(list), ROUND_CIPHER)
                std_deviation = round(get_std_deviation(list), ROUND_CIPHER)

                f_max = round(max(list), ROUND_CIPHER)
                f_min = round(min(list), ROUND_CIPHER)
                statistics_median = round( statistics.median(list), ROUND_CIPHER)
                statistics_std_deviation = round(statistics.stdev(list), ROUND_CIPHER)

                MZ_utils.print_result("**** RESULTS ****")
                MZ_utils.print_result(f"Max calculated with for cyrcle         : {v_max}")
                MZ_utils.print_result(f"Max calculated with max function       : {f_max}")
                MZ_utils.print_result(f"Min calculated with for cyrcle         : {v_min}")
                MZ_utils.print_result(f"Min calculated with max function       : {f_min}")
                MZ_utils.print_result(f"Median calculated with formula         : {median}")
                MZ_utils.print_result(f"Median calculated with statistic module: {statistics_median}")
                MZ_utils.print_result(f"StdDev calculated with formula         : {std_deviation}")
                MZ_utils.print_result(f"StdDev calculated with statistic module: {statistics_std_deviation}")

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


               
def get_median(list):
        list.sort() 

        n = len(list)
        if n % 2 == 1:
                return list[n // 2]
        else:
                return (list[n // 2 - 1] + list[n // 2]) / 2
        
def get_std_deviation(list):
        mean = sum(list) / len(list)
        scarti_quad = [(x - mean) ** 2 for x in list]
        sum_of_deviations = sum(scarti_quad)
        return (sum_of_deviations / (len(list) - 1)) ** 0.5
       
                        
list_item_search()