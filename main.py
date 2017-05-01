from collections import namedtuple
def to_namedtuples(filename):
    result = []
    with open(filename, mode='rb') as infile:
        # wtf python namespaces
        print csv
        reader = csv.reader(infile)
        Data = namedtuple("Data", next(reader))
        result.append(Data)
    return result

if __name__ == '__main__':
    csv = 'groceries.csv'
    print to_namedtuples(csv)
