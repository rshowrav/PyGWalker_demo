import pandas as pd
import pygwalker as pyg

# Gathering data for Demo

url='https://www.basketball-reference.com/leagues/NBA_2022_totals.html'

list = pd.read_html(url)
df = pd.DataFrame(list[0])


# Data cleanup as headers repeat and total lines not necessary under Tm Column

df = df[(df['Rk']!='Rk')&(df['Tm']!='TOT')]
df

# Converting variables of interest to integers

df['STL'].astype(int)
df['BLK'].astype(int)

# Creating UI for dataframe

gwalker = pyg.walk(df)

