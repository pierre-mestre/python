import csv
import pandas as pd
import folium
import branca
import urllib.parse
import requests
import json
import math 
import numpy as np # import package
import matplotlib.pyplot as plt # import module


def get_code_iso(name):
	url = f"https://restcountries.eu/rest/v2/name/{name}"
	# print(url)
	reponse = requests.get(url)
	if reponse.status_code != 200 :
		print("...")
		return ""
	dico = json.loads(reponse.text)
	return dico[0]['alpha3Code']

df = pd.read_csv('donnee.csv', encoding = 'utf-8')
print("Chargement en cours veuillez patienter (environ 1 a 2 min)")

df[['country', 'Population density (per km2, 2017)']].hist(bins=50, color='red')
plt.xlabel('densité (nombre de personne / Km²')
plt.ylabel('nombre de pays conscerné')
plt.title('HISTOGRAMME: densité de population / Km² par pays du monde')

df['Population density (per km2, 2017)'] = np.log(df['Population density (per km2, 2017)'])
df[['country', 'Population density (per km2, 2017)']].hist(bins=50, color='green')
plt.xlabel('log(densité (nombre de personne / Km²)')
plt.ylabel('nombre de pays conscerné')
plt.title('HISTOGRAMME: LOG(densité de population) / Km² par pays du monde')
	# df.rename(columns={'Population density (per km2, 2017)': 'density'}, inplace=True )
	# df.drop(df[df.density > 500].index, inplace=True)
	# df.rename(columns={'density': 'Population density (per km2, 2017)'}, inplace=True )
#df.drop(df.loc[df['Population density (per km2, 2017)'] > 1000], inplace=True)
df['codeCountry'] = df['country'].apply(get_code_iso)

#print(df[['country','codeCountry', 'Population density (per km2, 2017)']])
# for row in df['country']:
	# print(get_iso(row))
# with open('coordonne.geo.json') as json_file:
#     data = json.load(json_file)
#     print(data['features'][0]['geometry'])

state_geo = 'coordonne.geo.json'

m = folium.Map(location=[10, 10], zoom_start=3)
m.choropleth(
 geo_data=state_geo,
 name='choropleth',
 data=df,
 columns=['codeCountry', 'Population density (per km2, 2017)'],
 key_on='feature.properties.iso_a3',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.2,
 legend_name='log(Population density (per km2, 2017))'
)
folium.LayerControl().add_to(m)
 
# Save to html
m.save('Population density (per km2, 2017).html')
print("Execution terminé")


plt.show()

