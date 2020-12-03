# DOCTOR WINDROL'SAMPLE CODE FROM ALGORITHMIC MIND

# This function takes input from the user and checks if the input is whether an integer or not
# Returns an array of isInt bool value and the taken value
def enter_num(number_in_order):
    num = 0
    is_int = True
    try:
        num = int(input("Enter " + number_in_order + " integer: "))

    except ValueError:
        is_int = False
    return [is_int, num]


# This function reruns enter_num function if it finds non-integer input and informs the user of the error


def rerun_if_error(number_in_order):
    num = 0
    # runs as long as you put non-integer value
    while num == 0:
        is_int_and_num = enter_num(number_in_order)
        is_int = is_int_and_num[0]
        num = is_int_and_num[1]

        # check if is an integer
        if is_int:
            break
        else:
            print("Ooops! Wrong input.... Please enter an integer value")
    return num


# assign integer inputs from the user to our variables
num1 = rerun_if_error("first")
num2 = rerun_if_error("second")

# product function to return the product of the 2 operands


def product(operand1, operand2):
    return operand1 * operand2


# print the answer to the user
print("The product is: " + str(product(num1, num2)))
print("\n\n-----------Algorithmic Mind East Africa 2020----------")
