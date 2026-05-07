## REFERENCES ##
from geography_explorer.api.countries import get_countries
from geography_explorer.models.country import normalize_country

def main():
  print("GEOGRAPHY EXPLORER")

  ### API Call to get list of countries
  countries = get_countries()

  ### Normalize countries
  normalized_countries = [normalize_country(country) for country in countries]

  print(normalized_countries[7])
  


if __name__ == "__main__":
  main()