#A
def calculate_sum_and_average(n):
    total_sum = sum(range(1, n + 1))
    average = total_sum / n
    return total_sum, average

number = int(input("Skriv inn et heltall: "))
sum_result, avg_result = calculate_sum_and_average(number)
print(f"Summen av positive heltall opp til {number} er {sum_result}")
print(f"Gjennomsnittet av positive heltall opp til {number} er {avg_result}")

#B
numbers = []
while True:
    new_number = float(input("Skriv inn et tall: "))
    if new_number > 10:
        break
    numbers.append(new_number)

if numbers:
    min_number = min(numbers)
    max_number = max(numbers)
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    print(f"Minste tall: {min_number}")
    print(f"Største tall: {max_number}")
    print(f"Summen av tallene: {total_sum}")
    print(f"Gjennomsnittet av tallene: {average}")
else:
    print("Ingen tall ble skrevet inn.")

#C
import random

def roll_dice(n):
    rolls = [random.randint(1, 6) for _ in range(n)]
    total_sum = sum(rolls)
    average = total_sum / n
    return total_sum, average

num_rolls = int(input("Hvor mange terningkast vil du gjøre? "))
sum_result, avg_result = roll_dice(num_rolls)
print(f"Summen av terningkastene er {sum_result}")
print(f"Gjennomsnittet av terningkastene er {avg_result}")

#D
import random

def roll_two_dice(n):
    rolls = [(random.randint(1, 6), random.randint(1, 6)) for _ in range(n)]
    total_sum = sum([sum(roll) for roll in rolls])
    average = total_sum / n
    return total_sum, average

num_rolls = int(input("Hvor mange ganger vil du kaste to terninger? "))
sum_result, avg_result = roll_two_dice(num_rolls)
print(f"Summen av terningkastene er {sum_result}")
print(f"Gjennomsnittet av terningkastene er {avg_result}")
