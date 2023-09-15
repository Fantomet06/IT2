def overlapp_intervall(a: int, b: int, c: int, d: int) -> bool:
    if a < c and b <= c:
        return False
    elif d <= a and b > d:
        return False
    else:
        return True


"""
a,b= input("Skriv inn intervall 1: ").split()
c,d= input("Skriv inn intervall 2: ").split()
if overlapp_intervall(int(a),int(b),int(c),int(d)): print("\nIntervallene overlapper") 
else: print("\nIntervallene overlapper ikke")
"""

def check_overlap(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4) -> bool:
    if x_3 > x_1 and y_3 > y_1 and x_4 < x_2 and y_4 < y_2:
        return False

    if x_2 < x_3 or x_1 > x_4 or y_2 < y_3 or y_1 > y_4:
        return False
    else:
        return True

def main():

    test_cases= [
        [1, 5, 3, 8],
        [1, 5, 2, 4],
        [4, 8, 2, 6],
        [1, 3, 4, 5]
    ]
    print("Test cases for intervaller: \n")  
    for i in test_cases:
        print(overlapp_intervall(i[0], i[1], i[2], i[3]))

    check = [
        [1, 1, 8, 6, 7, 5, 10, 9],
        [1, 1, 8, 6, 3, 0, 5, 9],
        [1, 1, 8, 6, 3, 3, 5, 5],
        [1, 1, 8, 6, 9, 9, 10, 10],
        [1, 1, 8, 6, 8, 0, 8, 7],
    ]
    print("\nTest cases for overlapping av rektangler: \n")  
    for i in check:
        print(check_overlap(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

if __name__ == "__main__":
    main()