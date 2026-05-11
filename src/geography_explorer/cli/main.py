## REFERENCES ##
from geography_explorer.api.countries import get_countries
from geography_explorer.models.country import normalize_country

def main():
  print("GEOGRAPHY EXPLORER")

  ### API Call to get list of countries
  countries = get_countries()

  ### Normalize countries
  normalized_countries = [normalize_country(country) for country in countries]

  country = [ c for c in normalized_countries if c.get("name",{}).get("common") == "Brunei"]
  print(country[0].get('capital'))
  


if __name__ == "__main__":
  main()