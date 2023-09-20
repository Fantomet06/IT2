def double_list(liste: list) -> list:
    new_list = []
    for i in liste:
        new_list.append(i*2)
    return new_list

def main():
    print(double_list([1,2,3,4,5,6,7,8,9,10]))

if __name__ == "__main__":
    main()