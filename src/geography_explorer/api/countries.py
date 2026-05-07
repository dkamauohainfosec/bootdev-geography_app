import requests

### Base URL for REST Countries API ###
base_url = "https://restcountries.com/v3.1"



def get_countries():
  fields = "name,capital,region,subregion,population,flags,cca3"

  ## Sets the URL appropriately to run the query to get those fields for each country ##
  url = f"{base_url}/all?fields={fields}"

  ## Sends the request ##
  response = requests.get(url, timeout=10)
  response.raise_for_status()

  return response.json()