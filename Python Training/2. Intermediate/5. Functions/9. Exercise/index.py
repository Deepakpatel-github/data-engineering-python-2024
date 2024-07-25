# # Challenge 1
# def addition(x, y=10):
#     return x+y
#
#
# print(addition(5, 6))
# print(addition(5))  # Default parameter
#
#
# def area_rectangle(width, height):
#     area = width * height
#     return area
#
#
# print("Area of rectangle:", area_rectangle(height=5, width=6))
#
#
# def calculate_average(numbers_list) -> float:
#     # Docstrings and Return Statements
#     """
#     To calculate the average of list elements
#
#     Parameters:
#         numbers_list(list): a list of integers.
#
#     Return:
#         float: return the average of numbers in list.
#     """
#     total = sum(numbers_list)
#     count = len(numbers_list)
#     average = total/count
#     return average
#
#
# numbers = [1, 2, 3, 4, 5]
# result = calculate_average(numbers)
# print("Average:", result)
# print(type(result))


# Challenge 5
def outer_factorial(x):
    def inner_factorial(k):
        if k == 0 or k == 1:
            return 1
        else:
            return k * inner_factorial(k - 1)

    if x < 0:
        return "Factorial is not defined for negative numbers."
    elif not isinstance(x, int):
        return "Factorial is only defined for positive integers."
    else:
        return inner_factorial(x)


print(outer_factorial(5))


# Challenge 6
square = lambda x: x * x
print("Square:", square(6))
