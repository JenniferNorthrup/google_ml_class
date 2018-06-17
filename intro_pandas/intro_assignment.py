import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print(pd.__version__)

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

cities = pd.DataFrame({'City name': city_names, 'Population': population})
print(cities.describe())
print(cities.head())
print("---Type of cities' 'City Name'---")
print(type(cities['City name']))
print(cities['City name'])
print("---Type of the value of cities['City name'] at position 1---")
print(type(cities['City name'][1]))
print(cities['City name'][1])
print("---Type of cities from position 0 to position 2")
print(type(cities[0:2]))
print(cities[0:2])

#I can't get this to work for shit...
print("--- FOOBAR Double the population series (Does it affect cities dataframe?)---")
population*2
population.mul(2)
population.multiply(2)
population.rmul(2)
print(population)
print("-----")

print("---Log of population---")
print(np.log(population))
print("---Boolean array for cities with pop over 1,000,000")
highpop = population.apply(lambda val: val >1000000)
print(highpop)
print("---Add high pop, area, and pop density---")
cities['High population'] = highpop
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
#Use option_context to print non-standard display
with pd.option_context('display.max_rows', None, 'display.max_columns', 5):
    print(cities)
print("-----")

cali_housing_df = pd.read_csv("california_housing_train.csv", sep=",")
print(cali_housing_df.describe())
print(cali_housing_df.head())
print("-----")

#Won't print histogram, but indicates histogram was created
print(cali_housing_df.hist('housing_median_age'))



#Show matplotlib graphs in popup windows
#plt.show()

