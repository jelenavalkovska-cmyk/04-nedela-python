import sys
import storage

def main():

    if len(sys.argv) < 2:
        return

    command = sys.argv[1].lower()
    items = storage.load_list()

    if command == "add" and len(sys.argv) == 4:
        name = sys.argv[2]
        price = float(sys.argv[3])
        items.append({"name": name, "price": price})
        storage.save_list(items)
        print(f"✓ Pievienots: {name} ({price:.2f} EUR)")

    elif command == "list":
        print("Iepirkumu saraksts:")
        for i, item in enumerate(items, 1):
            print(f" {i}. {item['name']} — {item['price']:.2f} EUR")

    elif command == "total":
        total = sum(item['price'] for item in items)
        print(f"Kopā: {total:.2f} EUR ({len(items)} produkti)")

    elif command == "clear":
        storage.save_list([])
        print("Saraksts notīrīts.")

if __name__ == "__main__":
    main()