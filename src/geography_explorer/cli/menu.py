from geography_explorer.services.country_service import (
  search_country_by_name,
  show_countries_by_region,
  show_countries_by_subregion
)
from geography_explorer.services.quiz_service import play_capitals_quiz

def display_menu():
  print("\nGEOGRAPHY EXPLORER")
  print("1. Search for a country")
  print("2. View countries by continent")
  print("3. Geography Quiz")
  print("4. Exit")

def get_menu_choice():
  return input("Choose an option: ").strip()

def display_region_menu():
  print("\nPick a Region:")
  print("1. Africa")
  print("2. North America")
  print("3. South America")
  print("4. Asia")
  print("5. Europe")
  print("6. Oceania")
  print("7. Back")

def get_region_choice():
  return input("Choose a region: ").strip()

def run_menu():
  while True:
    display_menu()
    choice = get_menu_choice()

    match choice:
      case "1":
        search_country_by_name()

      case "2":
        run_region_menu()

      case "3":
        play_capitals_quiz()
      
      case "4":
        print("Goodbye.")
        break

      case _:
        print("Invalid option. Please choose 1, 2, or 3")

def run_region_menu():
  while True:
    display_region_menu()
    choice = get_region_choice()

    match choice:
      case "1":
        show_countries_by_region("Africa")
      case "2":
        show_countries_by_subregion("Americas", "North America")
      case "3":
        show_countries_by_subregion("Americas", "South America")
      case "4":
        show_countries_by_region("Asia")
      case "5":
        show_countries_by_region("Europe")
      case "6":
        show_countries_by_region("Oceania")
      case "7":
        break
      case _:
        print("Invalid input.")
