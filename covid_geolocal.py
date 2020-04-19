import matplotlib.pyplot as plt
import pandas as pd
import mplleaflet as mll

covid_info = pd.read_csv('covid19_df.csv')
covid_info.drop(['date', 'estimated_population_2019', 'confirmed_per_100k_inhabitants', 'death_rate'],
                axis=1, inplace=True)
covid_info = covid_info[covid_info.is_last == True]
covid_info.rename(columns={'city_ibge_code': 'codigo_ibge'}, inplace=True)

cities_info = pd.read_csv('municipios.csv')
cities_info.drop(['nome', 'codigo_uf', 'capital'],
                 axis=1, inplace=True)

merged_df = pd.merge(left=covid_info, right=cities_info, left_on='codigo_ibge', right_on='codigo_ibge')
merged_df = merged_df[merged_df.place_type == 'city']

plt.scatter(merged_df['longitude'], merged_df['latitude'], marker='.')
mll.show()
