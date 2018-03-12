# Brics countries 
# Brazil, Russi, India, China, South Africa

import pandas as pd
dict = {
	"country":["Brazil", "Russia", "India", "China", "South Africa"],
	"capital":["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
	"area":[8.516, 17.10, 3.286. 9.597, 1.221],
	"population:[200.4, 143.5, 1252, 1357, 52.98]	
	}

brics = pd.dataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]

#or 
brics = pd.read_csv("path/to/brics.csv", index_col = 0)

type(brics["country"]) # series
type(brick[["country"]]) dataframe

brick[["country", "capital"]] # column access

brics[1:4] # row access only through splicing, not ""

# loc - label-based
# iloc - integer position-based

brics.loc["RU"] # returns as a column
brics.loc[["RU"]] # returns as a row

brics.loc[["RU", "IN", "CH"], ["country", "capital"]]
brics.loc[:,["country", "capital"]]

brics.iloc[["RU"]]
brics.iloc[[1]]

brics.iloc[[1,2,3],[0,1]]
brics.iloc[:,0,1]]
