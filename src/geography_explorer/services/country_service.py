### IMPORTS ###
import requests

### REFERENCES ###
from geography_explorer.api.countries import get_country_by_name
from geography_explorer.models.country import normalize_country, display_country

def search_country_by_name():
  country_name = input("Enter a country name: ").strip()

  if not country_name:
    print("Please enter a country name.")
    return

  try:
    country = get_country_by_name(country_name)
    normalized_country = normalize_country(country)
    display_country(normalized_country)

  except requests.HTTPError:
    print(f"No country found for: {country_name}")

  except requests.RequestException as e:
    print(f"API request failed: {e}")