import pandas as pd
df = pd.read_csv(r'C:\Users\aadya\Downloads\bestsellers.csv')
df.drop_duplicates(inplace=True)
df.rename(columns={"Name":"title", "User Rating":"rating"},inplace="True")
print(df.head(10))

author_counts = df['Author'].value_counts()
print(author_counts)
print(df['Genre'].value_counts())
print(df['rating'].value_counts())
print(df['Year'].value_counts())
highest_idx = df['rating'].idxmax()
print("Highest Rated Book:")
print(df.loc[highest_idx])
highest_idx = df['rating'].idxmin()
print("Lowest Rated Book:")
print(df.loc[highest_idx])

avg_rating_by_genre = df.groupby("Genre")["rating"].mean()
print(avg_rating_by_genre)


author_counts.head(10).to_csv("top_authors.csv")
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
