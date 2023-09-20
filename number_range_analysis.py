#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):
    """
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.

    # create a variable with tha equals 0
    total_sum = 0
    #using a for loop itirate through each number in the range.
    for x in range(start, end +1):
        #add 1 to total sum.
        total_sum += x 

    # TODO: Return the calculated sum.
    # return the calcualted sum.
    return total_sum

def find_smallest_number(start, end):
    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.

    # create a variable named smallest_number that equals the start value

    smallest_number = start
    # create a loop that loops through all the numbers in the range and update the smallest_number variable if necessary using an f statement. 
    for x in range(start, end +1):
        if x < smallest_number:
            smallest_number = x

    # TODO: Return the found smallest number.
    return smallest_number

def find_largest_number(start, end):
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.

    # create a variable that is equal to the end value

    largest_number = end

    # using a for loop loop thourgh the range and update the largest_number variable if necessary using and f statement.
    for x in range(start, end + 1):
        if x > largest_number:
            largest_number = x
    # TODO: Return the found largest number.
    return largest_number

def count_even_numbers(start, end):
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    #create a variable equal to 0 to store the count of even numbers.
    even_num = 0
    #using a for loop itirate thourgh the numbers in the range.
    for x in range(start, end +1):
        #using an if statatement check if x is divisible by 2 and if its is add one to the even_num variable.
        if x % 2 == 0:
            even_num = even_num + 1
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.

    return even_num

def count_odd_numbers(start, end):
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.

    #create a variable equal to 0 to store the count of odd numbers in the range.

    odd_num = 0

    #use a for loop and an f statement to loop through the numbers in the range and determine the amount of odd numbers by adding one to the odd_sum.

    for x in range(start, end + 1):
        if x % 2 != 0:
            odd_num = odd_num + 1


    # TODO: Return the count of odd numbers.
    return odd_num