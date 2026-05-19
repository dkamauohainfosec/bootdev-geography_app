### IMPORTS ###
import requests

### REFERENCES ###
from geography_explorer.api.countries import get_country_by_name, get_countries_by_region
from geography_explorer.models.country import normalize_country, display_country, display_region_countries

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

def show_countries_by_region(region):
  try:
    countries = get_countries_by_region(region)
    sorted_countries = sorted(
      countries,
      key=lambda country: country.get("name", {}).get("common", "")
    )
    display_region_countries(sorted_countries)
  except requests.HTTPError:
    print(f"No countries found for region: {region}")
  except requests.RequestException as e:
    print(f"Api request failed: {e}")

def show_countries_by_subregion(region, subregion):
  try:
    countries = get_countries_by_region(region)

    filtered_countries = [
      country for country in countries
      if country.get("subregion", "").lower() == subregion.lower()
    ]

    sorted_countries = sorted(
      filtered_countries,
      key=lambda country: country.get("name", {}).get("common", "")
    )

    display_region_countries(sorted_countries)

  except requests.HTTPError:
    print(f"No countries found for subregion: {subregion}")

  except requests.RequestException as e:
    print(f"API request failed: {e}")