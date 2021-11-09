import pandas as pd
import math

def pagination(df, data_in_page = 10):
    first_data_in_page = 0
    last_data_in_page = data_in_page
    current_page = 1
    get_max_rows = df.shape[0]
    last_page = math.ceil(get_max_rows / data_in_page)
    while True:
        print(f'Currently in {current_page} out of {last_page}')
        print(df.iloc[first_data_in_page:last_data_in_page])
        print('(n) next page', end='/')
        print('(p) previous page', end='/')
        print('(f) first page', end='/')
        print('(l) last page', end='/')
        print('(q) Back to main menu')
        action = input('Type command: ')
        if action.lower() == 'q':
            break
        elif action.lower() == 'n':
            if current_page < last_page:
                first_data_in_page = last_data_in_page
                last_data_in_page = first_data_in_page + data_in_page
                if last_data_in_page > get_max_rows:
                    last_data_in_page = get_max_rows
                current_page += 1
        elif action.lower() == 'p':
            if current_page > 1:
                last_data_in_page = first_data_in_page
                first_data_in_page = last_data_in_page - data_in_page
                if first_data_in_page < 0:
                    first_data_in_page = 0
                current_page -= 1
        elif action.lower() == 'f':
            current_page = 1
            first_data_in_page = 0
            last_data_in_page = data_in_page
        elif action.lower() == 'l':
            current_page = last_page
            last_data_in_page = get_max_rows
            if get_max_rows % data_in_page > 0:
                first_data_in_page = get_max_rows - (get_max_rows % data_in_page)
            else:
                first_data_in_page = last_data_in_page - data_in_page
        else:
            print('Invalid commands.')
        

columns_list = pd.Index(['abilities', 'against_bug', 'against_dark', 'against_dragon',
       'against_electric', 'against_fairy', 'against_fight', 'against_fire',
       'against_flying', 'against_ghost', 'against_grass', 'against_ground',
       'against_ice', 'against_normal', 'against_poison', 'against_psychic',
       'against_rock', 'against_steel', 'against_water', 'attack',
       'base_egg_steps', 'base_happiness', 'base_total', 'capture_rate',
       'classfication', 'defense', 'experience_growth', 'height_m', 'hp',
       'japanese_name', 'name', 'percentage_male', 'pokedex_number',
       'sp_attack', 'sp_defense', 'speed', 'type1', 'type2', 'weight_kg',
       'generation', 'is_legendary'],
      dtype='object')
check_file = True
file_name = 'pokemon.csv'
while check_file:
    try:
        df = pd.read_csv(file_name)
        if df.columns.sort_values().equals(columns_list.sort_values()):
            check_file = False
        else:
            print('Error: File structure not supported')
            file_name = input('Type pokemon dataset file: ')
    except:
        print('Error: File does not exist')
        file_name = input('Type pokemon dataset file: ')
        
df.set_index(df['pokedex_number'], inplace=True)
usual_columns = ['name', 'type1', 'type2', 'attack', 'defense', 'hp', 'generation']
# print(df.loc[:, usual_columns])
# print(df.loc[(df['generation'] == 1), usual_columns])
# pagination(df.loc[:, usual_columns], 20)
pagination(df.loc[(df['generation'] == 1), usual_columns], 20)