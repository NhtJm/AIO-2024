import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset_path = "/Users/nhatnguyen/Documents/GIT/AIO2024/module3/week1/data/IMDB-Movie-Data.csv"
data = pd.read_csv(dataset_path)


# Read data with specified explicit index.
# We will use this later in our analysis
data_indexed = pd.read_csv(dataset_path, index_col="Title")

# Preview top 5 rows
print(data.head())

# info
print(data.info())
print(data.describe())

# Extract data as series
genre = data["Genre"]
print(genre)

print(data[["Genre"]])

some_cols = data[['Title', 'Genre', 'Rating', 'Actors', 'Director']]

print(data.iloc[10:15][['Title', 'Rating', 'Revenue (Millions)']])

print(data[((data['Year'] >= 2010) & (data['Year'] <= 2015)) & (data['Rating'] < 6.0) & (
    data['Revenue (Millions)'] > data['Revenue (Millions)'].quantile(0.95))])

print(data.groupby('Director')[['Rating']].mean().head())

print(data.groupby('Director')[['Rating']].mean().sort_values(
    by='Rating', ascending=False).head())

print(data.isnull().sum())

print(data.drop('Metascore', axis=1).head())

revenue_mean = data_indexed['Revenue (Millions)'].mean()
print("The mean revenue is: ", revenue_mean)
# We can fill the null values with this mean revenue
data_indexed['Revenue (Millions)'].fillna(revenue_mean, inplace=True)

# Classify movies based on ratings


def rating_group(rating):
    if rating >= 7.5:
        return 'Good'
    elif rating >= 6.0:
        return 'Average'
    else:
        return 'Bad'


# Lets apply this function on our movies data
# creating a new variable in the dataset to hold the rating category
data['Rating_category'] = data['Rating'].apply(rating_group)
print(data[['Title', 'Director', 'Rating', 'Rating_category']].head(5))
