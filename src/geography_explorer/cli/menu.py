from geography_explorer.services.country_service import search_country_by_name

def display_menu():
  print("\nGEOGRAPHY EXPLORER")
  print("1. Search for a country")
  print("2. Compare two countries")
  print("3. Exit")

def get_menu_choice():
  return input("Choose an option: ").strip()

def run_menu():
  while True:
    display_menu()
    choice = get_menu_choice()

    match choice:
      case "1":
        search_country_by_name()

      case "2":
        print("Under construction")
      
      case "3":
        print("Goodbye.")
        break

      case _:
        print("Invalid option. Please choose 1, 2, or 3")

