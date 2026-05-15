## IMPORTS ##
import json
import requests

## REFERENCES ##
from geography_explorer.api.countries import get_countries, get_country_by_name
from geography_explorer.models.country import normalize_country, display_country

def main():
  print("GEOGRAPHY EXPLORER")

  while True:
    country_name = input("Enter a country name: ").strip()

    try:
      country = get_country_by_name(country_name)
      display_country(normalize_country(country))
      break
    except requests.HTTPError:
      print(f"No country found for: {country_name}")
      print("Please try again.\n")
    except requests.RequestException as e:
      print(f"API request failed: {e}")
      print("Please try again.\n")

  

  


if __name__ == "__main__":
  main()