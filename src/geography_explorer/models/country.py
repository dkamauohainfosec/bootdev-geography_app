def normalize_country(country):
  return {
    "Name": country[0]["name"]["common"],
    "Continent(s)": country[0]["continents"],
    "Subregion": country[0]["subregion"],
    "Capital": country[0]["capital"],
    "Population": country[0]["population"]
  }