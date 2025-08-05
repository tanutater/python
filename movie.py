import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("movie analytics/merged_dataset.csv")

# # genre 
# df['genres'] = df['genres'].str.split(';')
# df = df.explode('genres')

# df['genres'] = df['genres'].str.strip()


# top10 = df['genres'].value_counts().head(10)

# # Make labels (Genre + Count) using a simple loop
# labels = []
# for i in range(len(top10)):
#     genre = top10.index[i]
#     count = top10.values[i]
#     labels.append(f"{genre} ({count})")

# # Plot pie chart
# plt.figure(figsize=(10,10))
# plt.pie(top10, labels=labels, autopct='%1.1f%%', startangle=90)
# plt.title("Top 10 Genres")


# year wise movie count
# movie_count = df['year'].value_counts().sort_index()
# last15years=movie_count.tail(15)
# plt.bar(last15years.index, last15years.values, label='Movie Count')

# # Add labels
# plt.xlabel('Year')
# plt.ylabel('Number of Movies')
# plt.title('last 15 years Movie Count')
# plt.legend()


# rating vs num_reviews
review=df['num_reviews']
rating=df['rating']
plt.scatter(rating,review,label='rating vs rating')
plt.title('rating vas review') 

plt.legend()
plt.show()