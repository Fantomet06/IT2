def chars(text: str) -> int:
    count = 0
    for i in text:
        count += 1
    return count

def middle_char(text: str) -> str:
    if chars(text) % 2 == 0:
        return text[chars(text) // 2 - 1:chars(text) // 2 + 1]
    else:
        return text[chars(text) // 2]

def palindrome(text: str) -> bool:
    if text == text[::-1]:
        return True
    else:
        return False

def main():
    text = input('Skriv inn en tekst: ')
    print(f'Antall tegn: {chars(text)}')
    print(f'Midterste tegn: {middle_char(text)}')
    print(f'Palindrom: {palindrome(text)}')

if __name__ == "__main__":
    main()