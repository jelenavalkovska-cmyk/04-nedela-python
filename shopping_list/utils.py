def calc_line_total(item):
    return item['qty'] * item['price']

def calc_grand_total(items):
    return sum(calc_line_total(item) for item in items)

def count_units(items):
    return sum(item['qty'] for item in items)