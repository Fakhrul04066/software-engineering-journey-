import pandas as pd
import numpy as np
data ={
    "Name":["Karim","Jamal","Mia","Akip"],
    "Age": [20,22,25,23],
    "Marks": [90,80,70,75]
}

df = pd.DataFrame(data)
print(df)
print()
print(df.head(2))
print()
print(df.tail(2))

print()
print()
print(df.describe())