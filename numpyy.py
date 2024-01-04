import numpy as np
import pandas as pd
matrix = np.array([[10,20,30,40,50,60],[10,90,120,110,130,150]])
print(matrix)
dic = {
    "car":["venue","creta","thar"],
    "brand":["Hyundai","Maruti","Honda"],
    "cost":[9000,1000,7600],
    "year":[20,21,19]
}
print(pd.DataFrame(dic))
data = pd.read_csv("diabetes.csv")
print(data.head())
# print(data['Age'].value_counts)

