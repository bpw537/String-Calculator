# Blake Williams
# bpw537@usask.ca

"""
Purpose: Take in a string of numbers and commas and add the numbers together

Pre-conditions:
    :param numbers: A string made of only numbers separated by commas

Return: A integer that is the initial numbers added together
"""
def Add(numbers):
    # If string is empty return 0
    if numbers == "":
        return 0

    # Get each number and add them together
    list = numbers.split(',')
    sum = 0
    for i in list:
        sum += int(i)
    return sum
