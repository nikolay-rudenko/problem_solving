import csv

def proces_csv(path):
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            print(row)

if __name__ == '__main__':
    proces_csv('data/books.csv')