import pandas as pd 

cities_df = pd.read_csv('Resources/cities.csv')
cities_df.to_html('data.html', index=False)
table = cities_df.to_html()
print(table)