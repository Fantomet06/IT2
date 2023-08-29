def count_letters(text):
    letter_counts = {}
    for letter in text:
        if letter.isalpha():  # Ignorerer ikke-bokstavtegn
            letter = letter.lower()  # Konverterer til små bokstaver
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return letter_counts

norwegian_alphabet = 'abcdefghijklmnopqrstuvwxyzæøå'
input_text = input("Skriv inn en tekst: ")

letter_occurrences = count_letters(input_text)

print("Antall forekomster av bokstaver i det norske alfabetet:")
for letter in norwegian_alphabet:
    count = letter_occurrences.get(letter, 0)
    print(f"{letter}: {count}")
