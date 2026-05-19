### IMPORTS ###
import random

### REFERENCES ###
from geography_explorer.utils.text import normalize_text

def play_capitals_quiz(countries):
  countries_with_capitals = [
    country for country in countries
    if country.get("capital")
  ]

  while True:
    country = random.choice(countries_with_capitals)

    country_name = country.get("name", {}).get("common", "Unknown")
    correct_capitals = country.get("capital", ["Unknown"])

    print(f"\nWhat is the capital of {country_name}?")
    print("Type 'exit' to return to the main menu.")

    user_answer = input("Your answer: ").strip()

    if user_answer.lower() == "exit":
      print("Returning to main menu...")
      break
    
    normalized_user_answer = normalize_text(user_answer)

    valid_answers = [normalize_text(capital) for capital in correct_capitals]

    if normalized_user_answer in valid_answers:
      print("Correct!")
    else:
      capitals_string = ", ".join(correct_capitals)

      if len(correct_capitals) == 1:
        print(f"Incorrect. The correct capital is {capitals_string}.")
      else:
        print(f"Incorrect. The correct capitals are: {capitals_string}.")

