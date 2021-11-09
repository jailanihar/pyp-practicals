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
        
def ask_specific_generation():
    min_generation = df['generation'].min()
    max_generation = df['generation'].max()
    while True:
        user_generation = input(f'Type pokemon generation between {min_generation} to {max_generation}: ')
        if user_generation.isdigit():
            user_generation = int(user_generation)
            if user_generation >= min_generation and user_generation <= max_generation:
                return user_generation
            else:
                print(f'Error: Invalid generation value, must be between {min_generation} to {max_generation}')
        else:
            print(f'Error: Generation must be number between {min_generation} to {max_generation}')

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
against_columns = [col for col in df if col.startswith('against')]

main_menu = ('(1) Total number of pokemon',
             '(2) List of pokemon',
             '(3) List of legendary pokemon',
             '(4) List of pokemon from specific generation',
             '(5) List of legendary pokemon from specific generation',
             '(6) Average against score from strong to weak',
             '(7) Average and standard deviation of pokemon against all types',
             '(8) Average attack, defense and hp for each pokemon generation',
             '(9) Average attack, defense and hp for each pokemon type',
             '(10) List of all pokemon strong against specific pokemon',
             '(q) Quit application')

while True:
    for menu in main_menu:
        print(menu)
    user_menu = input('Choose menu: ')
    if user_menu == '1':
        print(f'Total number of pokemon is {df.shape[0]}')
    elif user_menu == '2':
        pagination(df.loc[:, usual_columns], 20)
    elif user_menu == '3':
        pagination(df.loc[(df['is_legendary'] == 1), usual_columns])
    elif user_menu == '4':
        user_generation = ask_specific_generation()
        pagination(df.loc[(df['generation'] == user_generation), usual_columns])
    elif user_menu == '5':
        user_generation = ask_specific_generation()
        pagination(df.loc[(df['is_legendary'] == 1) & (df['generation'] == user_generation), usual_columns])
    elif user_menu == '6':
        print(df.loc[:, against_columns].mean().sort_values())
    elif user_menu == '7':
        df_usual_columns = df.loc[:, usual_columns]
        df_mean_against = df.loc[:, against_columns].mean(axis=1)
        df_std_against = df.loc[:, against_columns].std(axis=1)
        df_combined = df_usual_columns.assign(average_againsts=df_mean_against.values).assign(std_againsts=df_std_against.values)
        pagination(df_combined)
    elif user_menu == '8':
        print(df.groupby('generation')[['attack', 'defense', 'hp']].mean())
    elif user_menu == '9':
        print(df.groupby('type1')[['attack', 'defense', 'hp']].mean())
    elif user_menu == '10':
        while True:
            user_pokemon = input('Type pokemon name: ')
            df_pokemon_name = df.loc[(df['name'] == user_pokemon)]
            if df_pokemon_name.shape[0] > 0:
                break
            else:
                print('Error: Invalid pokemon name.')
        type1 = df.loc[(df['name'] == user_pokemon), 'type1'].iloc[0]
        type2 = df.loc[(df['name'] == user_pokemon), 'type2'].iloc[0]
        if pd.isna(type2):
            df_type = df.loc[(df[f'against_{type1}'] < 1) & (df['name'] != user_pokemon), ['name', f'against_{type1}']]
        else:
            df_type = df.loc[(df[f'against_{type1}'] < 1) & (df[f'against_{type2}'] < 1) & (df['name'] != user_pokemon),
                             ['name', f'against_{type1}', f'against_{type2}']]
        pagination(df_type)
    elif user_menu == 'q':
        quit()
    else:
        print('Error: Invalid menu chosen.')