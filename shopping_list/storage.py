import json
import sys
import os


LIST_FILE = "shopping.json"
PRICE_FILE = "prices.json"

def load_list():
    """Nolasa no JSON faila. Ja fails neeksistē, atgriež tukšu sarakstu."""
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
        json.dump(contacts, f, ensure_ascii=False, indent=5)


def load_prices():
    if not os.path.exists(PRICE_FILE):
        return {}
    with open(PRICE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_price(name, price):
    prices = load_prices()
    prices[name] = price
    with open(PRICE_FILE, "w", encoding="utf-8") as f:
        json.dump(prices, f, ensure_ascii=False, indent=4)