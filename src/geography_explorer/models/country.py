def normalize_country(country):
  return {
    "Name": country[0]["name"]["common"],
    "Continent(s)": country[0]["continents"],
    "Subregion": country[0]["subregion"],
    "Capital": country[0]["capital"],
    "Population": country[0]["population"],
    "Official Languages": country[0]["languages"]
  }

def display_country(country):
  print("*********************************")
  print("COUNTRY INFO")
  print("*********************************")
  print(f"\nName: {country.get('Name')}")
  print(f"Capital(s): {', '.join(country.get('Capital', []))}")
  print(f"\nContinent(s): {', '.join(country.get('Continent(s)', []))}")
  print(f"Subregion: {country.get('Subregion')}")

  print(f"\nPopulation: {country.get('Population'):,}")

  languages = country.get("Official Languages", {})
  print(f"\nOfficial Languages: {', '.join(languages.values())}")

def display_region_countries(countries):
    print("\nCOUNTRIES IN REGION")

    if not countries:
       print("No countries found.")
       return

    for country in countries:
      name = country.get("name", {}).get("common", "Unknown")
      capital = ", ".join(country.get("capital", ["N/A"]))
      population = country.get("population", 0)
      subregion = country.get("subregion", "N/A")

      print(f"\n{name}")
      print(f"  Capital: {capital}")
      print(f"  Population: {population:,}")
      print(f"  Subregion: {subregion}")
  