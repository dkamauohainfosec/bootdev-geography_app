import unicodedata

def normalize_text(text):
  normalized = unicodedata.normalize("NFKD", text)

  return "".join(
    char for char in normalized
    if not unicodedata.combining(char)
  ).lower()