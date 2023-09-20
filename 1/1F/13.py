#Lag en funksjon som teller antall forekomster av et tegn i en tekst. (Altså én parameter for tegnet og én for teksten.)

def count_char(char: str, text: str) -> int:
    count = 0
    for i in text:
        if i == char:
            count += 1
    return count

def main():
    print(count_char("a", "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"))

if __name__ == "__main__":
    main()