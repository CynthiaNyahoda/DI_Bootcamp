def calculate_age(age_in_seconds):
    earth_year = 31557600  # seconds in an Earth year
    planets = {
        "Earth": 1,
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132
    }
    age_on_earth = age_in_seconds / earth_year
    age_on_other_planets = {planet: round(age_on_earth / orbital_period, 2) for planet, orbital_period in planets.items()}
    return age_on_other_planets

age_in_seconds = 1000000000
age_on_planets = calculate_age(age_in_seconds)
print(age_on_planets)
