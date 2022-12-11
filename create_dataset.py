import random
import pandas as pd
import time


def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def create_dataset():
    # Creation of the 4 columns
    # The first column contains the chemical formula of the molecule
    # The second column contains the trace of other molecules found in the same sample
    # The third column contains the state of the molecule (solid, liquid, gas, ...)
    # The fourth column contains the date when the molecule was found FORMAT: YYYY-MM-DD HH:MM:SS
    df = pd.DataFrame(columns=['Chemical Formula', 'Trace', 'State', 'Date'])
    # Creation of the 5000 rows
    for i in range(5000):
        # Creation of the chemical formula
        # The chemical formula is composed of 2 letters and 1 numbers
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        chemical_formula = letters[random.randint(0, len(letters) - 1)] + letters[random.randint(0, len(letters) - 1)] + numbers[random.randint(0, len(numbers) - 1)]
        chemical_formula = ''.join(random.sample(chemical_formula, len(chemical_formula)))

        trace = [''.join(random.sample(chemical_formula, len(chemical_formula))) for _ in range(random.randint(0, 3))]

        states = ['Solid', 'Liquid', 'Gas']
        state = states[random.randint(0, len(states) - 1)]
        if random.random() < 0.01:
            state = random.choice(['Plasma', 'Supercritical fluid'])
        date = str_time_prop('2010-01-01 00:00:00', '2022-01-01 00:00:00', '%Y-%m-%d %H:%M:%S', random.random())
        # Creation of the row
        df.loc[i] = [chemical_formula, trace, state, date]
    # set type of the columns
    df['Chemical Formula'] = df['Chemical Formula'].astype("string")
    df['Trace'] = df['Trace'].to_numpy()
    df['State'] = df['State'].astype("string")
    df['Date'] = df['Date'].astype("datetime64[ns]")

    print(df.dtypes)
    # Creation of the csv file
    df.to_csv('dataset.csv', index=False)
    return df


if __name__ == '__main__':
    create_dataset()