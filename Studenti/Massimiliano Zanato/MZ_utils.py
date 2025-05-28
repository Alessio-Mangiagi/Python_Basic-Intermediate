def to_float(s):
    try:
        return float(s)
    except ValueError:
        return None
    
def to_int(s):
    try:
        return int(s)
    except ValueError:
        return None
    
def print_error(e):
       print(f"\033[91m{e}\033[0m")

def print_result(r):
       print(f"\033[92m{r}\033[0m")

def is_input_float(s):
        r = to_float(s)
        if r == None:
                print(f"Invalid input, is not a real number: {s}")
                return False
        return True

def is_input_int(s):
        r = to_int(s)
        if r == None:
                print(f"Invalid input, is not an integer: {s}")
                return False
        return True

def is_null_or_empty(value):
    return value is None or value == ""