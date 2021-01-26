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

def Tests():
    print("Running Add() tests")
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
    print("Add() tests complete")

Tests()
