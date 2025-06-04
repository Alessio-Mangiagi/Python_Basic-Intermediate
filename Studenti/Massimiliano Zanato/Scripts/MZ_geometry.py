import MZ_utils
import math


def geometry_calculator():
     print("---------------------------\nWelcome to the program for calculating areas and perimeters!")

     while True:
        operation = input("---------------------------\nChoose the geometric figure:\n1. Rectangle\n2. Circle\n3. Triangle\nE. Exit\nSelected operation: ")
        if operation == "E":
               break
        if operation != "1" and operation != "2" and operation != "3":
                MZ_utils.print_error("Invalid operation")
                continue
       
        area = ""
        perimeter = ""

        match operation:
                case "1":
                        base = input("Base: ")
                        if MZ_utils.is_input_float(base) == False:
                                continue
                        height = input("Height: ")
                        if MZ_utils.is_input_float(height) == False:
                                continue
                        base_f = MZ_utils.to_float(base)
                        height_f = MZ_utils.to_float(height)
                        area = get_rectangle_area(base_f, height_f)
                        perimeter = get_rectangle_perimeter(base_f, height_f)
                
                case "2":
                        radius = input("Radius: ")
                        if MZ_utils.is_input_float(radius) == False:
                                continue
                        radius_f = MZ_utils.to_float(radius)
                        area = get_circle_area(radius_f)
                        perimeter = get_circle_perimeter(radius_f)
                
                case "3":
                        side_1 = input("Side 1: ")
                        if MZ_utils.is_input_float(side_1) == False:
                                continue
                        side_2 = input("Side 2: ")
                        if MZ_utils.is_input_float(side_2) == False:
                                continue
                        side_3 = input("Side 3: ")
                        if MZ_utils.is_input_float(side_3) == False:
                                continue
                        side_1_f = MZ_utils.to_float(side_1)
                        side_2_f = MZ_utils.to_float(side_2)
                        side_3_f = MZ_utils.to_float(side_3)
                        if is_valid_triangle(side_1_f, side_2_f, side_3_f) == False:
                                continue
                        area = get_triangle_area(side_1_f, side_2_f, side_3_f)
                        perimeter = get_triangle_perimeter(side_1_f, side_2_f, side_3_f)

                case _:
                        break

        MZ_utils.print_result(f"The area is {area}")
        MZ_utils.print_result(f"The perimeter is {perimeter}")

def get_rectangle_area(b,h):
        return b * h    

def get_rectangle_perimeter(b,h):
        return 2 * (b + h)      

def get_circle_area(r):
        return  math.pi * r ** 2

def get_circle_perimeter(r):
        return 2 * math.pi * r

def is_valid_triangle(s1, s2, s3):
        if s1 + s2 <= s3:
                MZ_utils.print_error("The given sides do not form a valid triangle. Case: s1 + s2 <= s3. Suggestion: use s1 = 5, s2 = 7 and s3 = 10")
                return False     
        elif s1 + s3 <= s2:
                MZ_utils.print_error("The given sides do not form a valid triangle. Case: s1 + s3 <= s2. Suggestion: use s1 = 5, s2 = 7 and s3 = 10")
                return False
        elif s2 + s3 <= s1:
                MZ_utils.print_error("The given sides do not form a valid triangle. Case: s2 + s3 <= s1. Suggestion: use s1 = 5, s2 = 7 and s3 = 10")
                return False
        return True

def get_triangle_area(s1, s2, s3):
        p = get_triangle_perimeter(s1, s2, s3)
        semi_p = p / 2
        # Heron's formula
        math.sqrt(semi_p * (semi_p - s1) * (semi_p - s2) * (semi_p - s3))

def get_triangle_perimeter(s1, s2, s3):
        return s1 + s2 + s3
         
geometry_calculator()