def list_sum(list: list) -> int:
    """
    Returns the sum of all the elements in a list.

    Parameters:
    ----------
    list (list): list of integers.

    Return:
    -------
    (int): sum of all the elements in the list.
    """
    sum = 0
    for i in list:
        sum += i
    return sum

def avg_list(list: list) -> float:
    """
    Returns the average value of all the elements in a list.

    Parameters:
    ----------
    list (list): list of integers.

    Return:
    -------
    (float): average value of all the elements in the list.
    """
    return list_sum(list) / len(list)

def max_list(list: list) -> int:
    """
    Returns the maximum value of all the elements in a list.

    Parameters:
    ----------
    list (list): list of integers.

    Return:
    -------
    (int): maximum value of all the elements in the list.
    """
    return max(list)

def min_list(list: list) -> int:
    """
    Returns the minimum value of all the elements in a list.

    Parameters:
    ----------
    list (list): list of integers.

    Return:
    -------
    (int): minimum value of all the elements in the list.
    """
    return min(list)

def main():
    """Test for the functions in this file."""
    list = [1,2,3,4,5,6,7,8,9,10]
    print(list_sum(list))
    print(avg_list(list))
    print(max_list(list))
    print(min_list(list))

if __name__ == "__main__":
    main()