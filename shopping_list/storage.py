import json
import sys
import os


LIST_FILE = "shopping.json"

def load_list():
    """Nolasa kontaktus no JSON faila. Ja fails neeksistē, atgriež tukšu sarakstu."""
    if not os.path.exists(LIST_FILE):
        return []
    try:
        with open(LIST_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []
    
def save_list(contacts):
    """Saglabā sarakstu JSON failā."""
    with open(LIST_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)