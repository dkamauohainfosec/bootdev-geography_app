def normalize_country(country):
  return {
    "code": country.get("cca3"),
    "name": country.get("name"),
    "capital": country.get("capital"),
    "region": country.get("region"),
    "population": country.get("population")
  }