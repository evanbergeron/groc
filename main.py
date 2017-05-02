import csv
import sys
from pprint import pprint
from collections import namedtuple
class Grocery(object):
    def __init__(self, name, price, store, calories):
        self.name = name
        self.price = float(price)
        self.store = store
        self.calories = int(calories)

def parse_groceries(filename):
    result = []
    with open(filename, mode='rb') as infile:
        reader = csv.reader(infile)
        for row in reader:
            try:
                (name, price, store, calories) = tuple(row)
            except ValueError:
                print row
                sys.exit(1)
            try:
                item = Grocery(name, price, store, calories)
            except ValueError:
                # Ignore things with TODO in csv right now
                continue
            result.append(item)
    return result

def order_by_cost_per_calories(groceries):
    return [('%0.2f' % round(100*cost,2), name) for cost, name in sorted([ \
        (grocery.price / grocery.calories, grocery.name) \
        for grocery in groceries]
        )]

if __name__ == '__main__':
    csv_file = 'groceries.csv'
    groceries = parse_groceries(csv_file)
    for item in order_by_cost_per_calories(groceries):
        print item
