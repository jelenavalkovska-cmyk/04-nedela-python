import sys
import storage
import utils

def main():

    if len(sys.argv) < 2:
        return

    command = sys.argv[1].lower()
    items = storage.load_list()
    prices = storage.load_prices()

    price = None

    if command == "add":

        name = sys.argv[2]
        qty = int(sys.argv[3])
            
        if name in prices:
            known_price = prices[name]
            choice = input(f"Atrasta cena: {known_price:.2f} EUR. [A]kceptēt / [M]ainīt? ").lower()
            if choice == 'm':
                    price = float(input("Ievadi jaunu cenu: "))
                    storage.save_price(name, price)
            else:
                    price = known_price
        else:
                price = float(input(f"Cena produktam '{name}' nav zināma. Ievadi: "))
                storage.save_price(name, price)



        #price = float(sys.argv[4])
        items.append({"name": name, "qty": qty, "price": price})
        storage.save_list(items)
        line_total = utils.calc_line_total(items)
        print(f"✓ Pievienots: {name} × {qty} ({price:.2f} EUR/gab.) = {line_total:.2f} EUR")

    elif command == "list":
        print("Iepirkumu saraksts:")
        for i, item in enumerate(items, 1):
            line_sum = utils.calc_line_total(item)
            print(f" {i}. {item['name']} × {item['qty']} — {item['price']:.2f} EUR/gab. — {line_sum:.2f} EUR")

    elif command == "total":
        total = utils.calc_grand_total(items)
        units = utils.count_units(items)
        print(f"Kopā: {total:.2f} EUR ({units} vienības, {len(items)} produkti)")

    elif command == "clear":
        storage.save_list([])
        print("Saraksts notīrīts.")

if __name__ == "__main__":
    main()