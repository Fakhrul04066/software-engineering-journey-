import pandas as pd
import numpy as np


# ============================
# 1. Creating DataFrame
# ============================

data = {
    "Name":["Karim","Jamal","Mia","Akip","Sara"],
    "Age":[20,22,25,23,21],
    "Marks":[90,80,70,75,95],
    "Department":["IT","HR","IT","Finance","HR"]
}

df = pd.DataFrame(data)

print(df)


# ============================
# 2. Understanding Data
# ============================

# First 5 rows
print(df.head())


# Last 3 rows
print(df.tail(3))


# Shape
print(df.shape)


# Column names
print(df.columns)


# Data types
print(df.dtypes)


# Complete information
df.info()


# Statistical summary
print(df.describe())



# ============================
# 3. Selecting Data
# ============================


# Select one column

print(df["Name"])



# Select multiple columns

print(
    df[
        ["Name","Marks"]
    ]
)



# Select row using loc

print(df.loc[0])



# Select multiple rows

print(
    df.loc[0:2]
)



# Select row using iloc

print(
    df.iloc[0]
)



# Select rows and columns

print(
    df.iloc[0:3,0:2]
)



# ============================
# 4. Filtering Data
# ============================


# Marks greater than 75

result = df[
    df["Marks"] > 75
]

print(result)



# Age greater than 22

print(
    df[
        df["Age"] > 22
    ]
)



# Between condition

print(
    df[
        df["Marks"].between(70,90)
    ]
)



# AND condition

print(
    df[
        (df["Marks"] > 75)
        &
        (df["Age"] > 20)
    ]
)



# OR condition

print(
    df[
        (df["Marks"] > 90)
        |
        (df["Age"] == 20)
    ]
)



# isin()

print(
    df[
        df["Department"].isin(
            ["IT","HR"]
        )
    ]
)



# String filtering

print(
    df[
        df["Name"].str.contains("a")
    ]
)