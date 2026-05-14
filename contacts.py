import json
import sys
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Nolasa kontaktus no JSON faila. Ja fails neeksistē, atgriež tukšu sarakstu."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    try:
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_contacts(contacts):
    """Saglabā kontaktu sarakstu JSON failā."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)

def add_contact(kontaktu_saraksts):
    """Pievieno jaunu kontaktu un saglabā."""
    name = input("Ievadiet kontakta vārdu: ")
    phone = input("Ievadiet kontakta telefona numuru: ")
    kontaktu_saraksts.append({"name": name, "phone": phone})
    save_contacts(kont_saraksts)
    print(f"Kontakts '{name}' pievienots!")
    return True

def list_contacts():
    """Izvada visus kontaktus."""
    contacts = load_contacts()
    if not contacts:
        print("Kontaktu saraksts ir tukšs.")
        return
    
    print("\nVisi kontakti:")
    for idx, c in enumerate(contacts, 1):
        print(f"{idx}. {c['name']} - {c['phone']}")

def search_contacts(query):
    """Meklē kontaktus pēc vārda daļas."""
    contacts = load_contacts()
    results = [c for c in contacts if query.lower() in c['name'].lower()]
    
    if not results:
        print(f"Nav atrasts neviens kontakts, kas atbilstu '{query}'.")
    else:
        print(f"\nMeklēšanas rezultāti ('{query}'):")
        for c in results:
            print(f"- {c['name']}: {c['phone']}")


if __name__ == "__main__":
    kont_saraksts = load_contacts()
    add_contact(kont_saraksts)
    save_contacts(kont_saraksts)
    list_contacts()
    search_contacts("Anna")



