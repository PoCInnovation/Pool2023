import random
import csv

header = ['O2', 'CO2', 'breathable']


def generate_data(x, y):
    result = x * 2 - 10 * y - x
    if result > 0:
        return 1
    else:
        return 0


with open('air_quality_train.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    for i in range(10000):
        x = random.randint(10, 100)
        y = random.randint(0, 10)
        res = generate_data(x, y)
        data = [x, y, res]

        writer.writerow(data)
