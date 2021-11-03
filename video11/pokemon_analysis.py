import pandas as pd

check_file = True
file_name = 'pokemon.csv'
while check_file:
    try:
        df = pd.read_csv(file_name)
        check_file = False
    except:
        print('Error: File does not exist')
        file_name = input('Type pokemon dataset file: ')
print(df)
print(df.iloc[:5])
print(df.iloc[-5:, 0:5])
print(df.iloc[[0, 100, 700], [30, 40]])
print(df.loc[[0, 100, 700], ['name', 'is_legendary', 'type1', 'type2']])