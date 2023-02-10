
import random

def get_season(month):
    if month >= 3 and month <= 5:
        return "spring"
    elif month >= 6 and month <= 8:
        return "summer"
    elif month >= 9 and month <= 11:
        return "autumn"
    elif month == 12 or month >= 1 and month <= 2:
        return "winter"

def get_random_temp(season):
    if season == "summer":
        return random.uniform(24, 40)
    elif season == "autumn" or season == "fall":
        return random.uniform(16, 23)
    elif season == "winter":
        return random.uniform(-10, 16)
    elif season == "spring":
        return random.uniform(0, 32)

def main():
    month = int(input("Enter the number of the month (1 = January, 12 = December): "))
    season = get_season(month)
    temperature = get_random_temp(season)
    print(f"The temperature right now is {temperature:.2f} degrees Celsius.")
    
    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today")
    elif temperature >= 0 and temperature <= 16:
        print("Quite chilly! Don't forget your coat")
    elif temperature > 16 and temperature <= 23:
        print("It's pleasant outside.")
    elif temperature > 23 and temperature <= 32:
        print("It's warm outside.")
    elif temperature > 32 and temperature <= 40:
        print("It's hot outside.")

main()
