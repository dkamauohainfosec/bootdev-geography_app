### IMPORTS ###
import random
import requests
import unicodedata

### REFERENCES ###
from geography_explorer.api.countries import get_countries

def normalize_text(text):
  normalized = unicodedata.normalize("NFKD", text)
  return "".join(char for char in normalized if not unicodedata.combining(char)).lower()

def play_capitals_quiz():
  try:
    countries = get_countries()

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

  except requests.RequestException as e:
    print(f"API request failed: {e}")