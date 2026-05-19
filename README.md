# Geography Explorer

Geography Explorer is a Python command-line application for exploring country information using the REST Countries API.

## Features

- Search for a country by name
- View countries by continent or region
- View countries by subregion for North America and South America
- Play a capitals trivia quiz
- Handles countries with multiple capitals
- Accepts capital answers without accented characters, such as `male` for `Malé`

## Requirements

- Python 3.10 or newer
- Internet connection
- `requests`

## Installation

Clone the repository:

```bash
git clone https://github.com/dkamauohainfosec/bootdev-geography_app.git
cd bootdev-geography_app
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project:

```bash
pip install -e .
```

## Running the App

After installation, run:

```bash
geography-explorer
```

You should see the main menu:

```text
GEOGRAPHY EXPLORER
1. Search for a country
2. View countries by continent
3. Geography Quiz
4. Exit
```

## Menu Options

### 1. Search for a country

Enter a country name when prompted. The app will display information such as:

- Country name
- Capital city or cities
- Continent
- Subregion
- Population
- Official languages

### 2. View countries by continent

Choose a region from the menu:

```text
1. Africa
2. North America
3. South America
4. Asia
5. Europe
6. Oceania
7. Back
```

The app displays countries in the selected region, sorted alphabetically.

### 3. Geography Quiz

The capitals quiz randomly selects a country and asks for its capital.

Example:

```text
What is the capital of Maldives?
Type 'exit' to return to the main menu.
Your answer: male
Correct!
```

Type `exit` during the quiz to return to the main menu.

### 4. Exit

Exits the application.

## Project Structure

```text
src/geography_explorer/
├── api/
│   └── countries.py
├── cli/
│   ├── main.py
│   └── menu.py
├── models/
│   └── country.py
├── services/
│   ├── country_service.py
│   └── quiz_service.py
└── utils/
    └── text.py
```

## Notes

This project uses the REST Countries API, so API requests may fail if there is no internet connection or if the API is unavailable.