#Lag en funksjon som teller og returnerer antall ord i en tekst.

def count_words(text: str) -> int:
    count = 0
    for i in text:
        if i == " ":
            count += 1
    return count + 1

def main():
    print(count_words("Dette er en tekst."))

if __name__ == "__main__":
    main()