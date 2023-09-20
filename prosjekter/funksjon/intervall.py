def overlap_interval(a: int, b: int, c: int, d: int) -> bool:
    """
    Check if two intervals overlap.

    Parameters:
    ----------
    a (int): start of first interval
    b (int): end of first interval
    c (int): start of second interval
    d (int): end of second interval

    Return:
    -------
    (bool): True if overlap, False if not.
    """
    if a < c and b <= c:
        return False
    elif d <= a and b > d:
        return False
    else:
        return True

def overlap_rectangles(x_1: int, y_1: int, x_2: int, y_2: int, x_3: int, y_3: int, x_4: int, y_4: int) -> bool:
    """
    Check if two rectangles overlap.
    
    Parameters:
    ----------
    First rectangle:
        x_1 (int): bottom left corner x-coordinate
        y_1 (int): bottom left corner y-coordinate
        x_2 (int): top right corner x-coordinate
        x_2 (int): top right corner y-coordinate

    Second rectangle:
        x_3 (int): bottom left corner x-coordinate
        y_3 (int): bottom left corner y-coordinate
        x_4 (int): top right corner x-coordinate
        x_4 (int): top right corner y-coordinate

    Return:
    -------
    (bool): True if overlap, False if not.
    """
    if x_3 > x_1 and y_3 > y_1 and x_4 < x_2 and y_4 < y_2:
        return False

    if x_2 < x_3 or x_1 > x_4 or y_2 < y_3 or y_1 > y_4:
        return False
    else:
        return True

def main():
    """
    Function for testing the functions in this file.

    First check: overlapp_intervall
    Second check: overlapp_rektangler
    """

    """First check: overlap_interval"""
    test_cases= [
        [1, 5, 3, 8],
        [1, 5, 2, 4],
        [4, 8, 2, 6],
        [1, 3, 4, 5]
    ]
    print("\nTest cases for intervaller: \n")  
    for i in test_cases:
        print(overlap_interval(i[0], i[1], i[2], i[3]))

    """Second check: overlap_rectangles"""
    check = [
        [1, 1, 8, 6, 7, 5, 10, 9],
        [1, 1, 8, 6, 3, 0, 5, 9],
        [1, 1, 8, 6, 3, 3, 5, 5],
        [1, 1, 8, 6, 9, 9, 10, 10],
        [1, 1, 8, 6, 8, 0, 8, 7],
    ]
    print("\nTest cases for overlapping av rektangler: \n")  
    for i in check:
        print(overlap_rectangles(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

if __name__ == "__main__":
    main()