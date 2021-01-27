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

    # Finds any custom delimiters
    delimiter = ","
    if len(numbers) > 4:
        if numbers[0:2] == "//":
            delimiter = numbers[2:numbers.index("\n")]
            numbers = numbers[numbers.index("\n"):]

    # Get each number and add them together
    list = numbers.split(delimiter)
    sum = 0
    negatives = []
    for i in list:
        # Removes any newlines then add the numbers
        i = int(i.strip('\n'))
        # Add negatives numbers to own list
        if i < 0:
            negatives.append(i)
        if i <= 1000:
            sum += i

    # If any negatives inputted then throw exception
    if len(negatives) > 0:
        raise Exception("Negatives not allowed", negatives)
    return sum


def Tests():
    print("Running Add() tests")
    # Testing version 1
    if Add("") != 0:
        print("Add() failed on empty string, got", Add(""))

    if Add("1") != 1:
        print("Add() failed on 1 number input, got", Add("1"))

    if Add("5,2,9") != 16:
        print("Add() failed on '5,2,9' number input, got", Add("5,2,9"))

    # Testing version 2 (handles new lines)
    if Add("\n1") != 1:
        print("Add() failed on 1 number input with new line, got", Add("\n1"))

    if Add("5,2\n,\n9") != 16:
        print("Add() failed on '5,2,9' number input, got with new lines", Add("5,2\n,\n9"))

    # Testing version 3 (custom delimiter)
    if Add("//;\n1") != 1:
        print("Add() failed on 1 number input with custom delimiter, got", Add("//;\n1"))

    if Add("//$@\n1") != 1:
        print("Add() failed on 1 number input with custom delimiter longer than 1 character, got", Add("//$@\n1"))

    if Add("//;\n5;2;9") != 16:
        print("Add() failed on '5,2,9' number input with custom delimiter, got", Add("//;\n5;2;9"))

    if Add("//$@\n5$@2$@9") != 16:
        print("Add() failed on '5,2,9' number input with custom delimiter longer than 1 character, got", Add("//$@\n5$@2$@9"))

    # Testing version 4 (throw exception on negatives)
    try:
        Add("-1")
    except:
        pass
    else:
        print("Add() failed on -1 number input, got", Add("-1"))

    try:
        Add("5,-2,-9")
    except:
        pass
    else:
        print("Add() failed on '5,-2,-9' number input, got", Add("5,-2,-9"))

    try:
        Add("\n-1\n")
    except:
        pass
    else:
        print("Add() failed on -1 number input with new lines, got", Add("\n-1\n"))

    try:
        Add("5\n,-2,\n9")
    except:
        pass
    else:
        print("Add() failed on '5,-2,9' number input with new lines, got", Add("5\n,-2,\n9"))

    try:
        Add("//;\n-1")
    except:
        pass
    else:
        print("Add() failed on -1 number input with custom delimiter, got", Add("//;\n-1"))

    try:
        Add("//$@\n-5$@-2$@-9")
    except:
        pass
    else:
        print("Add() failed on '-5,-2,-9' number input with custom delimiter longer than 1 character, got", Add("//$@\n-5$@-2$@-9"))

    # Testing version 5 (numbers larger than 1000 ignored)
    if Add("1000") != 1000:
        print("Add() failed on 1000 number input, got", Add("1000"))

    if Add("1001") != 0:
        print("Add() failed on 1001 number input, got", Add("1001"))

    if Add("5,25,2005") != 30:
        print("Add() failed on '5,25,2005' number input, got", Add("5,25,2005"))

    print("Add() tests complete")


Tests()
