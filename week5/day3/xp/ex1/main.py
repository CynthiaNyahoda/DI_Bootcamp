def built_in_functions_demo():
    """
    This function demonstrates the usage of some of the Python built-in functions:
    - abs(): returns the absolute value of a number.
    - int(): converts a string or a float to an integer.
    - input(): reads a line from input and returns it as a string.
    """
    # absolute value of a number
    print("Absolute value of -3:", abs(-3))  # 3

    # converting string to integer
    str_num = input("Enter a number: ")
    num = int(str_num)
    print("Number entered:", num)

    # converting float to integer
    float_num = 3.14
    int_num = int(float_num)
    print("Integer equivalent of", float_num, "is", int_num)


# calling the function to demonstrate the built-in functions
built_in_functions_demo()