import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import csv
import plotly.express as px

data = pd.read_csv("final.csv")


rows = []

with open("final.csv","r") as f:
  csvreader = csv.reader(f)
  
  for row in csvreader:
    rows.append(row)

headers = rows[0]
stars_data_rows = rows[1:]

stars_data_rows[1:3]

graph = px.scatter (data, x = data["Distance"] , y=["Gravity"] )
graph.show()

star = []

for d in data.Distance:
    if d == 100:
        star.apppend(True)
    else:
        star.append(False)


   
is_dist = pd.Series(star)
star_dist = data[is_dist]

star_dist.reset_index(inplace=True,drop=True)

print(star_dist.head())

print(star_dist.shape)

gravity_star=[]

for i in star_dist.Gravity:
  if i>=150 and i<=350:
    gravity_star.append(True)
  else:
    gravity_star.append(False)
    
print( len(gravity_star))
gravity_star = pd.Series(gravity_star)
final_stars = star_dist[gravity_star]
final_stars.head()

data.to_csv("Filter_stars.csv")















