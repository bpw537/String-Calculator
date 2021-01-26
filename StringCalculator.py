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
        # Removes any newlines then add the numbers
        i = i.strip('\n')
        sum += int(i)
    return sum

def Tests():
    print("Running Add() tests")
    # Testing version 1
    if Add("") != 0:
        print("Add() failed on empty string, got", Add(""))

    if Add("1") != 1:
        print("Add() failed on 1 number input, got", Add("1"))

    if Add("-1") != -1:
        print("Add() failed on -1 number input, got", Add("-1"))

    if Add("5,2,9") != 16:
        print("Add() failed on '5,2,9' number input, got", Add("5,2,9"))

    if Add("5,-2,9") != 12:
        print("Add() failed on '5,-2,9' number input, got", Add("5,-2,9"))

    # Testing version 2 (handles new lines)
    if Add("\n1") != 1:
        print("Add() failed on 1 number input with new line, got", Add("1"))

    if Add("\n-1\n") != -1:
        print("Add() failed on -1 number input with new lines, got", Add("-1"))

    if Add("5,2\n,\n9") != 16:
        print("Add() failed on '5,2,9' number input, got with new lines", Add("5,2,9"))

    if Add("5\n,-2,\n9") != 12:
        print("Add() failed on '5,-2,9' number input with new lines, got", Add("5,-2,9"))
    print("Add() tests complete")

Tests()
